# GPT-6 Astra adaptation — approved implementation plan

USER approved implementation on 2026-09-06. This replaces the earlier A/B/C
proposal. Git baseline: bad78613b57a6a6a7fc09f76c6a4b9d69d61f9b6; stable checkout
remains main. Work only in gpt-6-adaptation; no global skill reinstall, other
consumer relink, backup branch/file, or copied game repository.

## Intent and order

Factory encodes human creative experience, not a requirement to reproduce the
thinking choreography needed by older models. Keep the experience and quality
floor; let the continuing primary author jointly design and produce, using
methods when useful. Directly adapt, run real work, and revise from USER feedback.
No A/B/C experiments, token-comparison project, or token-reduction completion gate.
Existing benchmark CLI and historical failures remain intact, not relabeled.

1. Shared core and Idea/Gameplay/Studio; then existing Asset/Sound integration.
2. Opt-in Empire & Union and actual production/runtime verification.
3. Independent Story and virtual-world NPC capability; full regression.

## Implementation contract

- Explicit factory_project.v3 / workflow_version 3 selects Astra behavior.
  v1/v2 readers and specialist CLI arguments remain supported; no inferred upgrade.
- Add migrate --workflow gpt6 --check/--apply --expected; omitted workflow keeps
  existing behavior. Add --project-root as an alias of --game-repo and repeatable
  context --method <id>. No model API runner, daemon, or generic profile platform.
- Preserve state partitions, append-only/CAS checkpoints, exact source hashes,
  independent review identity, raw USER rulings and specialist acceptance.
- Use a versioned complete-design package; prose/diagrams/structured data can be
  multiple necessary artifacts, but each material fact is authored once. Human
  decisions and production views reference/project that package, not new authors.
- Catalog requirements separately from optional methods. Each moved obligation
  has source, new owner/location and tests. Do not silently remove requirements
  or leave consumers requiring supposedly optional step outputs.
- Context returns current task, complete applicable authority, work, questions
  and legal action; deduplicate sources, index methods, expand selected methods.
  Unclassified authority remains full text. Reviewers get all applicable sources,
  not an author-selected subset. Blind observers never receive generic context.
- Bind validity to related code/schema/rules, authority, inputs and actually
  selected methods. Unused optional-method edits do not invalidate work; unknown
  dependencies block rather than permit a fabricated refresh.
- Migration previews the whole routing/pointer/metadata write set, checks source
  fingerprints before publication, activates last, recovers/repeats safely and
  rejects concurrent edits. Historical rulings are not imported as new approval.
- Project routing resolves the selected checkout before its skill/workflow;
  ordinary relink does not change workflow. Stable installed skills stay on main.

## Capability behavior

Idea progressively establishes shared product understanding through references,
questions and proposals; save settled decisions, reasons/differences and unknowns.
Exploration can remain open/no-fit; commissioning remains USER-owned.

Gameplay/Studio jointly design causal loops, actual player work, responses,
carry-forward, alternatives, costs, recovery, two-lap difference and concrete
scene/time composition. Multiple system transitions can correspond to one actual
work beat; automatic feedback is not fake player work. Required scene maps and
material consequences must appear in the checked human projection. Execution
plans add details only. Existing authorized mechanical fixes reuse authority;
changed gameplay/meaning/scope reopens the design boundary.

Asset/Sound keep generation, cleanup, geometry/alpha validation, trim and
normalization providers. The author supplies one context-aware brief and reads
compact results/errors. Mocks certify routing only, not visual/audio quality.

Story is independent of games. World/character/cast/chapter/branch/craft/beat-sheet/
delivery/twin/rules remain available. Replace fixed step workers, file handoffs
and paragraph lengths with full jointly authored outputs and optional methods.
Persistent world events, knowledge provenance, relations, time and branch memory
support relevant-NPC updates rather than rewriting the whole population.
Pure Story needs neither Godot, a commissioned game nor a playable baseline;
engine staging/landing is a separate applicable adapter. Preserve full prose,
voice, emotional pacing, world sovereignty, terms, all shipped locales, bounded
clean-room fluency, canon backcheck and exact-output semantic QA. The kinship
USER ruling stays a semantic blocker, not a universal word blacklist.

## Review, authority and stopping

Two fresh independent reviewers examine the same complete-design version without
first-pass peer conclusions: intent/experience and completeness/project. The
primary author repairs FAILs within authority and reruns reviews on the exact new
version. No generic review for each reply, no restart merely for mechanical
implementation failure. Continue until the boundary passes, a new USER decision
is required, inputs/tools are unavailable, or no useful new repair can be made;
report that precise checkpoint, never claim completion to escape a blocker.

USER owns product adoption, material design approval and actual gameplay
acceptance. Blind runtime observation and informed comparison remain isolated.
Tests/screenshots/AI PASS do not constitute gameplay acceptance. Accepted baseline
promotion still requires new-play acceptance, applicable predecessor regression
and no blockers; absent predecessor is recorded, not fabricated.

## Empire pilot and exclusions

Continue /Users/hunglingki/git_projects/Godot/Empire_and_Union in place. Preserve
its existing dirty project.godot edit. Banner is read-only compatibility/known-
failure context: do not relink or edit its E1, runtime, untracked files or baseline.

USER ruling in the planning question: "解除切片前置限制". This expressly removes
coastal-slice human acceptance as the prerequisite to full-campaign production.
Record this new authority and supersede conflicting current brakes explicitly;
do not rewrite historical documents or mark the old slice accepted.

Keep Empire's adopted product and approved campaign intent. Phase one references
PS1 Zeon no Keifu mechanics/process, with the existing original expression/data/
balance boundaries. Start from public manual/guides, record located source,
behavior, Empire mapping, authorized differences, unknowns and test. Never invent
reference evidence or download game images as a default.

Audit the existing P01-P10 design, preserve valid USER decisions, review necessary
changed/new design and produce along its dependencies: state/catalogs; map/turn;
economy/research; personnel/intel/diplomacy; operations/supply; hex combat; complete
content; AI/endgame; UI/saves; integration. Run real tests/interaction each batch;
batching does not restore the revoked coastal acceptance brake. A two-lap slice
is not the complete campaign. Reference uncertainties requiring material product
choices return to USER; already settled product questions do not.

## Verification and honest completion

Run entry/core/Studio/Gameplay/Idea/Asset suites and relevant Story/Sound checks.
Add v3/v2 isolation, interrupted/repeated migration, concurrent write, immutable
history, checkpoint restart, complete context, blind isolation, dependency and
unauthorized-production regressions. Gameplay covers fake work, shared clock,
delay knowledge, real scene work and omitted decision surface. Story tests multi-
NPC/multi-day propagation, branch isolation, restart, voice/meaning and no-engine
operation; a small fixture is not proof of full-world scale. Provider mocks do
not replace actual media review. Empire runs Godot state, UI/interaction, cross-
turn, save/load, filtered-AI and regression checks.

Factory engineering, Empire production and accepted gameplay are separate status
claims. Completion requires usable new workflows with all capabilities, passing
checks, real Empire production/run, independent Story cases and resolved or
explicitly escalated blockers. Preserve evidence and report unfinished work;
never relabel old benchmark attempts as new validation.

## Design review repair: concrete consumer/state contracts

The first independent intent review passed; completeness requested the bridges
below. These are implementation detail within USER-approved intent, not new
product decisions or a reinstated test-comparison gate.

- Schema/dispatch: factory_project.v3 and factory_design.v3 are new; shared
  factory_checkpoint.v2, factory_review.v2 and factory_ruling.v2 stay unchanged.
  gameplay/v2.py dispatches native material sections to gameplay/native.py but
  retains graph/surface/project checks. gameplay/plan.py consumes that same
  checkpoint, enforces approved paths and derives compatibility row numbers from
  sealed playable beats (no extra numbered Markdown Objective). studio/v2.py and
  baseline.py retain factory_gameplay_acceptance_input.v2, exact-build human
  verdict and baseline admission checks. Positive native full admission and real
  Godot tests plus unauthorized path/missing human cases exercise the whole chain.
- Migration matrix: unversioned/v1 -> v3; v2 -> v3; exact v3 -> no-op; implicit
  downgrade and authority removal -> rejection. The v3 transaction hashes the
  complete before set and desired after outputs, blocks use while prepared,
  publishes routing/pointer/receipt before PROJECT activation and recovers only
  matching partial outputs. Routing receipt predecessor proofs contain hashes,
  not backup text. Old checkpoint task ids are historical-only; a new task cites
  those exact sources and gets current validation, not imported approval. Existing
  product/design USER decisions remain source authority, not a new review verdict.
- Method ownership: factory_core/knowledge.json binds every old Story step to its
  retained semantic owner in story/docs/WORKFLOW_GPT6.md, optional technique,
  full-artifact consumer and regression suite. Existing rule_map ids retain their
  reviewer owners. methods ids are frozen in the v3 design; their exact files
  join the shared reviewer fingerprint. Changing ids or content reopens design.
  Unused method content is excluded; catalog membership is a conservative resolver
  dependency. Removed/unknown selections fail closed. v2 dependencies stay v2.
- Standalone Story: PROJECT_PROFILE fields are PROJECT_ID, WORLD_NAME, STORY_ROOT,
  PRIMARY_LOCALE, SHIPPED_LOCALES, MEDIUM=standalone|game, plus explicit sovereignty
  files. story design binds spoken_output_paths, runtime_output_paths and exact
  scope_evidence. Standalone with no runtime works despite an inactive colocated
  product. story_output_acceptance.v3 / story_technical_evidence.v3 permit typed
  NOT_APPLICABLE only for staging fidelity/routing with profile+scope evidence;
  no executed command is claimed. All other semantic/locale/knowledge checks and
  applicable v2 clean-room/backcheck records remain. Tests run through COMPLETE
  with synthetic, explicitly non-human fixture rulings—not real creative approval.
- NPC state: existing twin entities/facts remain canonical. story/world_state.py
  stores append-only accepted event envelopes beside the twin, not a second
  mutable canon or scheduler. story_event_delta.v1 names event_id, branch, monotonic
  tick, Git-pinned canonical entity source, new event facts, ordered observed/told
  acquisitions, relation changes and optional exact ancestor event base. Observation
  references this event's fact; communication requires the speaker's already
  acquired branch-local knowledge. Only branch genesis may inherit an exact
  ancestor endpoint; later parent events do not leak. Publication consumes an
  exact current COMPLETE Story output under the project lock, with predecessor
  CAS and event-id idempotency. Replay/query are derived; npc query omits unknown
  world truth. Candidate preview is never canon. Existing twin CRUD is preserved.

Implementation tests: factory_core/tests/test_gpt6.py, test_gpt6_gameplay.py,
test_gpt6_story.py, plus all retained entry/specialist suites. No test fixture
PASS or synthetic USER transcript is presented as Empire/Story acceptance.
