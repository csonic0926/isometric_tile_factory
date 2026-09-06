# GPT-6 adaptation implementation / verification — 2026-09-06

## Status and boundaries

Shared native workflow, explicit v3 opt-in, version-aware context/dependencies,
full decision-section projection, existing production/runtime consumer bridges,
standalone Story applicability and accepted branch-memory tooling implemented.
No benchmark runs/comparisons or token-savings claims. Existing result history
is unchanged. This is not a declaration that Empire or a whole virtual world is
delivered/accepted; real product work is tracked in the target project.

Stable main remains efb69db; its installed global skills still point there.
Adaptation changes live only in gpt-6-adaptation. Asset and Sound pipeline Python
files are byte-identical to stable main. No game repository/backup was copied.

## Actual test results

| Suite | Result |
| --- | --- |
| entry/setup unittest | 25 PASS |
| factory_core unittest | 106 PASS (74 existing + 32 adaptation cases) |
| Studio unittest | 144 PASS |
| Gameplay unittest | 207 PASS |
| Idea unittest | 29 PASS |
| Asset pytest | 37 PASS + 11 subtests PASS |

Total: 548 regular tests, plus Asset's 11 subtests. Shared-core tests include
real isolated Godot execution, repeated UI/state regression and the native
complete admission consumer chain. Fixture review/human records are synthetic
contract data, never actual USER acceptance. Sound trim/normalization and compact
provider-result contracts are included in shared-core tests. No new paid image
or audio generation was run, so no new real-media creative-quality claim.

Reproduction from the adaptation checkout:

```sh
for suite in tests factory_core/tests studio/tests gameplay/tests idea/tests; do
  python3 -m unittest discover -s "$suite" -q || exit $?
done
FACTORY_ASSET_REFERENCE_ROOT=<existing-generated-reference-png-directory> \
  PYTHONPATH=asset uv run --no-project --with pytest \
  --with-requirements asset/requirements.txt python -m pytest asset/tests -q
```

The first Asset invocation lacked pytest; the dependency-isolated uv invocation
then exposed missing untracked Blender reference PNGs in the new worktree (35
passed, missing-reference cases failed). Tests now accept an explicitly supplied
read-only reference directory. The final run above passed all 37 + 11; no fixture
was copied, no expected geometry loosened, and no provider implementation changed.
Pillow emitted deprecation warnings; these did not fail checks.

## Independent exact-design reviews

First design SHA256:
044e3f1253f33c017b2e397425da076c1d0ce719339aea18c4547328d6fad06c.
Independent contexts /root/adaptation_intent_review (PASS) and
/root/adaptation_completeness_review (FAIL). The latter required explicit v3
consumer dispatch, upgrade/history behavior, method/obligation inventory,
standalone applicability and branch-memory contracts. These were added, not
converted to an A/B/C project or another product approval gate.

Repaired design SHA256:
30fc5faa7fa4821d0b6a95a1a844792c37902933c83b04a9195deb0602864cfa.
Independent contexts /root/adaptation_review_r2_intent and
/root/adaptation_review_r2_completeness both returned PASS. Each received the
same exact design in a fresh non-author context without first-pass peer reports.
These were manual reusable-Factory Markdown design reviews, not fabricated
game-owned factory_review.v2 reports or invented dependency fingerprints.

Implementation defects identified and fixed:
- Exclude v3-only modules/schemas from v2 dependency sets.
- Permit standalone STORY_ROOT=<PROJECT_ROOT> without unsafe '.' references.
- Do not expose private incoming relationships merely because an NPC is involved;
  relationship changes name a fact, and the query requires acquired knowledge.

Their regressions are in test_gpt6.py and test_gpt6_story.py. Other new tests cover
activation-last recovery, conflict before activation, successive routing proofs,
historical task refusal, complete authority, exact human sections, no forced
Idea design, method selection, shared approval enforcement, native production
scope, no-engine COMPLETE, semantic failure despite technical success, monotonic
NPC time, observed/told provenance, idempotency, pinned branches and hidden future
knowledge. These prove mechanisms, not native prose quality or full-world scale.

## Remaining product validation

Empire migration/authority amendment, reference audit, runtime evidence and
production state must be read in Empire itself. Its old pending slice must not
be relabeled accepted. The revoked coastal prerequisite must not be restored.
Complete-campaign production, real-media fitness, real standalone-story creative
acceptance and USER feedback remain distinct from these engineering results.
