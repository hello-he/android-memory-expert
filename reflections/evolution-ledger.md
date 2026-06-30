# Evolution Ledger

This file records how each run should improve on the previous one. It is not part of the article body. Future runs must read this file and the latest dayXX reflection files before generating new content.

---

## Ongoing Issues
- GitHub Issues feedback is still blocked when `gh` is not authenticated. Do not claim issue feedback was incorporated unless `gh issue list` actually succeeds.
- Git operations have previously hit `.git/index.lock: Permission denied`. Every run should verify add, commit, and push instead of assuming git is healthy.
- The standing user preference is clear: more diagrams, less prose.

---

## Long-Term Writing Constraints
- Every article must land conclusions on observable evidence such as `dumpsys meminfo`, `/proc/<pid>/maps`, GC logs, heap dump views, Allocation views, and AOSP source paths.
- When discussing ART, prefer a `space + collector + allocator + root path` frame instead of importing HotSpot terms casually.
- Every article must visibly apply at least one prior reflection item from `shallow_points`, `knowledge_gaps`, `suggest_future_topics`, or `next_run_instructions`.
- Every article must include at least two Mermaid diagrams: one structure or execution-path view and one troubleshooting or decision-flow view.
- Any version differences, ROM differences, auth failures, or tooling limits must be written down explicitly as boundaries or blockers.

---

## Run History

### Day 01 -> Day 02
- Applied reflection: shifted from generic generation terminology to ART `space / collector` framing.
- Visible change: added Dalvik vs ART comparison structure.
- Unresolved: default collector and space combinations still need version-by-version confirmation.

### Day 02 -> Day 03
- Applied reflection: turned allocation-path theory into a practical investigation checklist.
- Visible change: centered the article on `TLAB / bump pointer / LOS` with tool-facing observation paths.
- Unresolved: TLAB refill, LOS thresholds, and region defaults still need version checks.

### Day 03 -> Day 04
- Applied reflection: connected allocation paths to reachability, stack roots, and JNI boundaries.
- Visible change: added stack and JNI structure diagrams plus troubleshooting flow.
- Unresolved: stack map and root enumeration details still vary by Android version.

### Day 04 -> Day 05
- Applied reflection: kept the evidence-chain writing style and grounded dex, oat, vdex, and JIT code cache in `meminfo` and `maps`.
- Visible change: added structure and decision diagrams plus concrete `maps` commands.
- Unresolved: `gh auth` and git write reliability remained open blockers.

### Day 05 -> Day 06
- Applied reflection: used heap dump and retained-size reasoning for String and intern analysis.
- Visible change: added InternTable structure and an intern decision flow.
- Unresolved: version boundaries around String storage and InternTable behavior remained open.

### Day 06 -> Day 07
- Applied reflection: clarified ART versus HotSpot terminology around object headers and lock words.
- Visible change: added ART object model, boundary, and troubleshooting diagrams plus AOSP entry paths.
- Unresolved: lock word encoding, read barrier details, and collector combinations still need branch-specific confirmation.

### Day 07 -> Day 08
- Applied reflection: connected object lifetime to reachability and reference strength.
- Visible change: added `ReferenceQueue` and reachability diagrams plus short comparison tables.
- Unresolved: `reference_processor` version differences and issue-feedback access remained open.

### Day 08 -> Day 09
- Applied reflection: enforced the multi-diagram, evidence-first format for GC algorithms.
- Visible change: added CMS vs CC execution-path and troubleshooting diagrams plus comparison matrices.
- Unresolved: issue access and possible `.git/index.lock` failures still required explicit checks.

### Day 09 -> Day 10
- Applied reflection: turned "low reclaim means strong reachability" into a root-evidence workflow.
- Visible change: added GC Roots structure, heap-dump evidence flow, troubleshooting flow, and MAT-focused tables.
- Unresolved: GitHub Issues remained unreadable and root-enumeration details still needed branch-specific validation.

### Day 10 -> Day 11
- Applied reflection: explicitly drew `heap -> collector -> root visitor -> reference processor` and converted the source article into a path index with commands and observation mapping.
- Visible change: added three Mermaid diagrams, a source-entry table, AOSP `rg` command blocks, an observation matrix, and boundary notes.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`, and collector defaults and phase details still need target-branch validation.

### Day 11 -> Day 12
- Applied reflection: split the previously shallow `heap.cc` trigger logic into alloc GC, background GC, and explicit GC with source paths, log signals, and troubleshooting branches.
- Visible change: added three Mermaid diagrams, trigger/source/evidence/scenario tables, AOSP `rg` commands, and logcat/meminfo/Perfetto/dumpheap command templates because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; exact `GcCause` names, log fields, and trigger call chains still need target-branch validation.

### Day 12 -> Day 13
- Applied reflection: carried forward Day 12's Perfetto gap by separating `paused`, `total time`, GC slice timing, Main Thread overlap, and scheduler contention.
- Visible change: added four Mermaid diagrams, pause/source/optimization matrices, AOSP `rg` commands, and logcat/Perfetto/meminfo/dumpheap command templates because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; exact pause phase names, collector defaults, and log fields still need target-branch and real-trace validation.

---

## Next Run: Day 14
- Keep the visual-first format.
- Focus on generational GC in ART, carrying forward Day 13's need for branch/version-specific boundaries and real trace evidence.
- Keep the engineering entry table pattern: source path, log signal, trace signal, and tool command.
- If GitHub Issues still cannot be read, record the auth blocker again in reflection and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.
