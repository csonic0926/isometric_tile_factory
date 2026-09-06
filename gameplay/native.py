"""Native full-content projection. Reuses graph/surface/project validators."""
from factory_core.refs import read_json, resolve_ref

REQUIRED_SECTIONS = {'intent-scope', 'cycle-player-work', 'two-lap-difference',
                     'alternatives-costs-recovery', 'scene-map', 'time-branches',
                     'production-acceptance'}


def material_spec(roots, design, errors):
    sections = design['decision_sections']
    missing = REQUIRED_SECTIONS - {s['id'] for s in sections}
    if missing:
        errors.append('human view omits applicable gameplay composition: ' + ', '.join(sorted(missing)))
    # The Objective is the authored complete design, not a generated legacy
    # Markdown spec. All material sections must be bound in the human view.
    for section in sections:
        resolve_ref(roots, section['source'])
    return {s['id']: s['text'] for s in sections}, design['author_context_id']


def production_units(roots, design):
    """Compatibility row numbers are a view of sealed beats, not another spec."""
    contract = read_json(resolve_ref(roots, design['gameplay']['interaction_contract']))
    return [{'row': index, 'beat_id': beat['beat_id']} for index, beat in enumerate(contract['playable_beats'], 1)]
