#!/usr/bin/env python3
"""Branch-scoped accepted NPC memory beside the existing canonical Story twin.

No scheduler, model calls or second mutable canon. preview is pure candidate
replay; append consumes a COMPLETE Story checkpoint. query filters knowledge.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from factory_core.refs import (FactoryError, confined, digest, exclusive_json, fail,
                               game_root, read_json, reference, resolve_ref, sha)
from factory_core.state import identifier, keys, project, project_lock, text
from factory_core.story_profile import resolve


def empty_state():
    return {'tick': -1, 'facts': {}, 'knowledge': {}, 'relations': {}, 'events': []}


def replay_event(roots, state, delta):
    """Pure reducer: never let author/world omniscience become NPC knowledge."""
    import copy
    keys(delta, {'schema_version', 'event_id', 'branch', 'tick', 'entities', 'facts', 'knowledge', 'relations', 'base'})
    if delta['schema_version'] != 'story_event_delta.v1':
        fail('INVALID_STORY_EVENT', 'unknown event delta schema')
    identifier(delta['event_id']); identifier(delta['branch'])
    if type(delta['tick']) is not int or delta['tick'] < 0 or delta['tick'] < state['tick']:
        fail('INVALID_STORY_TIME', 'event time cannot run backwards')
    if delta['event_id'] in state['events']:
        fail('DUPLICATE_STORY_EVENT', 'event id already occurred in this branch ancestry')
    # Pin entity identities in normal Git history: later twin revisions cannot
    # rewrite what an earlier event was about. Canonical authoring remains twin.
    if delta['entities'].get('scope') != 'game_git':
        fail('INVALID_STORY_EVENT', 'entity source must be pinned Git history, not a second or mutable entity registry')
    entities = read_json(resolve_ref(roots, delta['entities'])).get('entities')
    if not isinstance(entities, list):
        fail('INVALID_STORY_EVENT', 'canonical twin needs entities')
    ids = {e['id'] for e in entities}
    if len(ids) != len(entities):
        fail('INVALID_STORY_EVENT', 'duplicate canonical entity ids')
    for field in ('facts', 'knowledge', 'relations'):
        if not isinstance(delta[field], list): fail('INVALID_STORY_EVENT', field + ' must be a list')
    result = copy.deepcopy(state)
    introduced = set()
    for fact in delta['facts']:
        keys(fact, {'id', 'statement'})
        identity = identifier(fact['id']); statement = text(fact['statement'])
        if identity in result['facts'] or identity in introduced:
            fail('CONFLICTING_STORY_FACT', 'facts are immutable event facts; use a new fact id for a changed condition')
        introduced.add(identity)
        result['facts'][identity] = {'statement': statement, 'event_id': delta['event_id'], 'tick': delta['tick']}
    for acquisition in delta['knowledge']:
        keys(acquisition, {'npc_id', 'fact_id', 'kind', 'from_npc'})
        npc, fact = acquisition['npc_id'], acquisition['fact_id']
        if npc not in ids or fact not in result['facts']:
            fail('UNKNOWN_STORY_REFERENCE', 'knowledge must name an existing entity and branch-local fact')
        known = result['knowledge'].setdefault(npc, {})
        if fact in known:
            fail('DUPLICATE_STORY_KNOWLEDGE', 'the same acquisition cannot be applied twice')
        if acquisition['kind'] == 'observed':
            if fact not in introduced or acquisition['from_npc'] is not None:
                fail('INVALID_STORY_KNOWLEDGE', 'direct observation requires a fact in this event, not arbitrary past world truth')
        elif acquisition['kind'] == 'told':
            source = acquisition['from_npc']
            if source not in ids or source == npc or fact not in result['knowledge'].get(source, {}):
                fail('INVALID_STORY_KNOWLEDGE', 'speaker has not acquired this fact in this branch/time')
        else:
            fail('INVALID_STORY_KNOWLEDGE', 'use observed or told provenance, never omniscient knowledge')
        known[fact] = {**acquisition, 'event_id': delta['event_id'], 'tick': delta['tick']}
    for relation in delta['relations']:
        keys(relation, {'from_npc', 'to_npc', 'kind', 'change', 'fact_id'})
        if relation['from_npc'] not in ids or relation['to_npc'] not in ids:
            fail('UNKNOWN_STORY_REFERENCE', 'relationship participants must exist')
        if relation['fact_id'] not in result['facts']:
            fail('UNKNOWN_STORY_REFERENCE', 'relation visibility needs an existing branch-local fact')
        identity = (relation['from_npc'], relation['to_npc'], text(relation['kind']))
        result['relations']['|'.join(identity)] = {'change': text(relation['change']), 'fact_id': relation['fact_id'],
                                                  'event_id': delta['event_id'], 'tick': delta['tick']}
    result['tick'] = delta['tick']; result['events'].append(delta['event_id'])
    return result


def event_root(roots):
    p = project(roots['game'])
    if p['workflow_version'] != 3:
        fail('MIGRATION_REQUIRED', 'branch event history requires explicit GPT-6 opt-in')
    profile = resolve(roots['game'], p['authority_paths'], roots['factory'])
    return profile['story_root'] / 'story_world/events'


def read_branch(roots, branch, through=None, visiting=()):
    identifier(branch)
    if branch in visiting:
        fail('INVALID_STORY_BRANCH', 'cyclic ancestry')
    directory = event_root(roots) / branch
    confined(roots['game'], directory.relative_to(roots['game']).as_posix())
    paths = sorted(directory.glob('*.json')) if directory.exists() else []
    if through:
        endpoint = resolve_ref(roots, through)
        if endpoint.parent != directory or endpoint not in paths:
            fail('INVALID_STORY_BRANCH', 'base must name an exact accepted ancestor event')
        paths = paths[:paths.index(endpoint) + 1]
    state, previous = empty_state(), None
    for generation, path in enumerate(paths, 1):
        record = read_json(confined(roots['game'], path.relative_to(roots['game']).as_posix()))
        if record.get('schema_version') != 'story_accepted_event.v1' or path.name != f'{generation:06d}.json' or record.get('previous') != previous:
            fail('BROKEN_STORY_HISTORY', 'event generation/predecessor mismatch')
        delta = read_json(resolve_ref(roots, record['delta']))
        if delta['branch'] != branch:
            fail('INVALID_STORY_BRANCH', 'cross-branch write')
        if generation == 1 and delta['base']:
            base = delta['base']; keys(base, {'branch', 'event'})
            state, _ = read_branch(roots, base['branch'], base['event'], (*visiting, branch))
        elif delta['base']:
            fail('INVALID_STORY_BRANCH', 'only branch genesis may name ancestry')
        # This is sealed accepted history. Future implementation revisions don't
        # erase canon; hashes prove exact historical output, not new acceptance.
        accepted = read_json(resolve_ref(roots, record['accepted_checkpoint']))
        if (accepted.get('schema_version') != 'factory_checkpoint.v2' or accepted.get('stage') != 'COMPLETE'
                or accepted.get('capability') != 'story' or record['delta'] not in accepted.get('artifacts', [])):
            fail('UNACCEPTED_STORY_EVENT', 'event source is not an exact accepted Story output')
        report = read_json(resolve_ref(roots, accepted['acceptance']))
        if (report.get('schema_version') not in ('story_output_acceptance.v2', 'story_output_acceptance.v3')
                or report.get('verdict') != 'PASS' or report.get('outputs') != accepted['artifacts']
                or report.get('design') != accepted['design']
                or report.get('dependency_fingerprint') != accepted['dependencies']['fingerprint']):
            fail('UNACCEPTED_STORY_EVENT', 'sealed historical acceptance does not match the event output')
        state = replay_event(roots, state, delta)
        previous = sha(path)
    return state, previous


def append(roots, delta_ref, accepted_ref, expected):
    from factory_core.state import latest, verify_record
    delta = read_json(resolve_ref(roots, delta_ref))
    branch = identifier(delta['branch'])
    with project_lock(roots['game']):
        state, previous = read_branch(roots, branch)
        directory = event_root(roots) / branch
        if delta['event_id'] in state['events']:
            for path in directory.glob('*.json'):
                old = read_json(path)
                if old['delta'] == delta_ref and old['accepted_checkpoint'] == accepted_ref:
                    return {'status': 'ALREADY_APPLIED', 'event': reference(roots['game'], path.relative_to(roots['game']).as_posix())}
            fail('DUPLICATE_STORY_EVENT', 'event id conflict; never overwrite history')
        if expected != previous:
            fail('CONCURRENT_WRITE', 'event predecessor changed')
        accepted = read_json(resolve_ref(roots, accepted_ref))
        current, current_sha = latest(roots['game'], accepted['task_id'])
        if (current_sha != accepted_ref['sha256'] or accepted.get('stage') != 'COMPLETE'
                or accepted.get('capability') != 'story' or delta_ref not in accepted.get('artifacts', [])):
            fail('UNACCEPTED_STORY_EVENT', 'publish only an exact current COMPLETE Story output')
        verify_record(roots, accepted)
        if previous is None and delta['base']:
            keys(delta['base'], {'branch', 'event'})
            if delta['base']['branch'] == branch: fail('INVALID_STORY_BRANCH', 'self ancestry')
            state, _ = read_branch(roots, delta['base']['branch'], delta['base']['event'], (branch,))
        elif delta['base']:
            fail('INVALID_STORY_BRANCH', 'only new branch genesis may name an ancestor')
        replay_event(roots, state, delta)  # complete validation before publication
        generation = len(list(directory.glob('*.json'))) + 1
        record = {'schema_version': 'story_accepted_event.v1', 'previous': previous,
                  'delta': delta_ref, 'accepted_checkpoint': accepted_ref}
        relative = (directory / f'{generation:06d}.json').relative_to(roots['game']).as_posix()
        resolve_ref(roots, delta_ref); verify_record(roots, accepted)
        exclusive_json(confined(roots['game'], relative), record)
        return {'status': 'STORY_EVENT_APPLIED', 'event': reference(roots['game'], relative)}


def npc_view(state, npc_id):
    known = state['knowledge'].get(npc_id, {})
    return {'npc_id': npc_id, 'tick': state['tick'],
            'known_facts': [{**state['facts'][fact], 'id': fact, 'acquisition': provenance} for fact, provenance in sorted(known.items())],
            'relations': {key: value for key, value in state['relations'].items()
                          if npc_id in key.split('|')[:2] and value.get('fact_id') in known}}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--project-root', '--game-repo', dest='root', required=True)
    sub = p.add_subparsers(dest='command', required=True)
    q = sub.add_parser('query'); q.add_argument('--branch', required=True); q.add_argument('--npc', required=True)
    q = sub.add_parser('preview'); q.add_argument('--input', required=True)
    q = sub.add_parser('append'); q.add_argument('--input', required=True); q.add_argument('--accepted-checkpoint', required=True); q.add_argument('--expected')
    args = p.parse_args(argv)
    try:
        factory = Path(__file__).resolve().parents[1]
        roots = {'factory': factory, 'game': game_root(args.root, factory)}
        if args.command == 'query':
            state, previous = read_branch(roots, args.branch)
            result = {'status': 'NPC_KNOWLEDGE_VIEW', 'authority': False, 'previous': previous, **npc_view(state, args.npc)}
        else:
            ref = reference(roots['game'], args.input)
            if args.command == 'append':
                result = append(roots, ref, reference(roots['game'], args.accepted_checkpoint), args.expected)
            else:
                delta = read_json(resolve_ref(roots, ref)); state, previous = read_branch(roots, delta['branch'])
                if delta['base']:
                    if previous is not None: fail('INVALID_STORY_BRANCH', 'only genesis may inherit')
                    state, _ = read_branch(roots, delta['base']['branch'], delta['base']['event'], (delta['branch'],))
                result = {'status': 'CANDIDATE_EVENT_PREVIEW', 'authority': False, 'previous': previous,
                          'state': replay_event(roots, state, delta)}
        print(json.dumps(result, ensure_ascii=False, indent=2)); return 0
    except (FactoryError, OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'status': getattr(exc, 'code', 'INVALID_INPUT'), 'message': str(exc)})); return 2


if __name__ == '__main__':
    raise SystemExit(main())
