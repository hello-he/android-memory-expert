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

### Day 13 -> Day 14
- Applied reflection: carried forward Day 13's branch/version boundary gap by treating ART generational GC as target-branch-specific instead of universal HotSpot-style Young/Old terminology.
- Visible change: added three Mermaid diagrams, a version/source validation table, young/full execution sequence, troubleshooting decision flow, and logcat/Perfetto/meminfo/dumpheap command templates because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; exact generational collector defaults, log fields, and pause behavior still need target-branch validation and a real Perfetto trace.

### Day 14 -> Day 15
- Applied reflection: carried forward Day 14's retained-path fallback by framing memory leaks as GC Root ownership-chain problems rather than collector or generational GC failures.
- Visible change: added three Mermaid diagrams, Root-owner-bridge-victim modeling, retained-path troubleshooting flow, leak-type/source/evidence matrices, and adb/logcat/dumpheap/maps/AOSP command blocks because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs a real HPROF and real LeakCanary trace decoded line by line.

---

### Day 15 -> Day 16
- Applied reflection: carried forward Day 15's Root-owner-bridge-victim model into concrete Activity and Fragment leak patterns, especially destroyed Activity, Fragment view binding, adapter callback, observer, and lifecycle-bound task paths.
- Visible change: added three Mermaid diagrams, Root-owner-bridge-victim mapping, lifecycle-boundary tables, high-frequency-pattern matrices, LeakCanary trace reading notes, and adb/logcat/dumpheap/dumpsys/AOSP/AndroidX command blocks because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs a real HPROF and real LeakCanary trace decoded line by line, plus AndroidX Fragment version validation.

---

## Next Run: Day 17
- Keep the visual-first format.
- Focus on Handler leaks, carrying forward Day 16's Thread / MessageQueue / Message / Runnable branch.
- Keep the engineering entry table pattern: source path, log signal, trace signal, and tool command.
- Expand source paths and verification around delayed messages, lifecycle cancellation, and `removeCallbacksAndMessages`.
- If GitHub Issues still cannot be read, record the auth blocker again in reflection and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

---

### Day 16 -> Day 17
- Applied reflection: carried forward Day 16's Thread / MessageQueue / Message / Runnable branch and made Handler leaks a concrete retained-path problem through `Message.callback`, `Message.target`, `Message.obj`, and HandlerThread ownership.
- Visible change: added three Mermaid diagrams, Root-owner-bridge-victim mapping, AOSP Handler/Looper/MessageQueue/Message/HandlerThread source paths, lifecycle cancellation tables, token-based cleanup guidance, and adb/logcat/dumpheap/thread commands because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs a real HPROF, real LeakCanary Handler trace, target AOSP branch validation, and live pending-message instrumentation.

---

## Next Run: Day 18
- Keep the visual-first format.
- Focus on static and singleton leaks by contrasting global owner fields with Day 17's queued Message owner model.
- Reuse Root-owner-bridge-victim tables, source paths, troubleshooting flow, and before/after evidence commands.
- Expand boundaries around `applicationContext`, process-lifetime caches, singleton registries, and static listener lists.
- If GitHub Issues still cannot be read, record the auth blocker again in reflection and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

---

### Day 17 -> Day 18
- Applied reflection: carried forward Day 17's request to contrast queued Message owners with global owner fields, then made static/singleton leaks a concrete retained-path problem through `ClassLoader`, `Class`, `static field`, singleton/cache/listener fields, and destroyed page victims.
- Visible change: added four Mermaid diagrams, Handler-owner versus global-owner comparison, Root-owner-bridge-victim mapping, AOSP Context/View/Activity/LruCache source paths, applicationContext boundaries, cache policy checks, and adb/logcat/dumpheap/MAT/source-search command blocks because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs a real HPROF, real LeakCanary static-field trace, target AOSP branch validation, and a concrete third-party SDK singleton example.

---

## Next Run: Day 19
- Keep the visual-first format.
- Focus on listener and inner-class leaks by expanding Day 18's static listener-list branch.
- Include anonymous inner classes, lambda captures, `this$0`, observer APIs, adapter callbacks, lifecycle unregister boundaries, and before/after verification.
- Reuse Root-owner-bridge-victim tables, source paths, troubleshooting flow, and evidence command blocks.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

---

### Day 18 -> Day 19
- Applied reflection: carried forward Day 18's static listener-list branch and expanded it into listener registries, observer callbacks, anonymous inner classes, Kotlin lambda captures, `this$0`, adapter callbacks, and lifecycle unregister boundaries.
- Visible change: added four Mermaid diagrams, Day 18 carry-forward table, Root-owner-bridge-victim mapping, capture-shape matrix, lifecycle-boundary table, source/evidence command blocks, LeakCanary trace cues, and before/after verification tables because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs a real HPROF, real LeakCanary listener trace, target AndroidX dependency validation, and live listener-count instrumentation.

---

## Next Run: Day 20
- Keep the visual-first format.
- Focus on resource-not-closed leaks by contrasting Java retained listener/reference leaks with native/file/socket/cursor handle lifetime.
- Carry forward Day 19's before/after verification, but add `close`, `finally`, Kotlin `use`, Java try-with-resources, StrictMode, CloseGuard, `/proc/<pid>/fd`, lsof-style evidence, CursorWindow, Stream, Socket, and file descriptor checks.
- Reuse Root-owner-bridge-victim only where Java references are involved; explicitly separate reachability leaks from resource lifetime leaks.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

---

### Day 19 -> Day 20
- Applied reflection: carried forward Day 19's before/after verification model while explicitly separating Java retained references from OS/native handle lifetime for Cursor, Stream, Socket, file descriptor, CursorWindow, and native resource leaks.
- Visible change: added four Mermaid diagrams, Day 19 carry-forward table, fd/CursorWindow/StrictMode/CloseGuard evidence tables, must-close resource matrix, source path table, adb `/proc/<pid>/fd` and `dumpsys meminfo` command blocks, and repair/acceptance matrices because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real device fd snapshots, real StrictMode/CloseGuard traces, target AOSP branch validation, and a runnable sample app with reproducible resource leaks.

---

## Next Run: Day 21
- Keep the visual-first format.
- Focus on LeakCanary source code and carry forward Day 20's boundary: LeakCanary proves Java retained paths, while fd/native resource lifetime still needs fd, meminfo, StrictMode, or native evidence.
- Decode retained paths for Activity/Fragment/listener/resource-wrapper cases, and show what LeakCanary can and cannot prove.
- Include source paths for ObjectWatcher, KeyedWeakReference, HeapAnalyzer, Shark, retained object reporting, and Android lifecycle watchers.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

---

### Day 20 -> Day 21
- Applied reflection: carried forward Day 20's Java reachability versus fd/native resource-lifetime boundary and made it the central LeakCanary limitation: LeakCanary proves retained Java paths, while resource lifetime still needs fd, meminfo, StrictMode, CloseGuard, or native evidence.
- Visible change: added four Mermaid diagrams, LeakCanary/Shark/source-entry tables, Root-Owner-Bridge-Victim trace decoding, Activity/Fragment trace matrices, and combined LeakCanary-plus-resource acceptance flow because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs a real HPROF, real LeakCanary reports with concrete app classes, dependency-version validation, and same-HPROF comparison with MAT and Android Studio Profiler.

---

## Next Run: Day 22
- Keep the visual-first format.
- Focus on Android Studio Memory Profiler core workflow.
- Compare profiler heap/allocation/class-instance views with Day 21 LeakCanary retained-path reports.
- Carry forward Day 21's boundary: Java heap charts do not prove fd/native resource release without fd, meminfo, StrictMode, or native evidence.
- Include source/tooling commands and at least two Mermaid diagrams: one profiler evidence workflow and one troubleshooting decision flow.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 21 -> Day 22
- Applied reflection: carried forward Day 21's comparison gap and boundary by placing Android Studio Memory Profiler beside LeakCanary/MAT/fd/meminfo evidence instead of treating heap charts as complete proof.
- Visible change: added four Mermaid diagrams, a Profiler/LeakCanary/MAT division-of-labor matrix, timeline-shape interpretation table, source/tooling commands, and resource-lifetime acceptance gates because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real Android Studio profiler captures, a same-HPROF comparison across Android Studio/Shark/MAT, and Android Studio version-specific UI validation.

## Next Run: Day 23
- Keep the visual-first format.
- Focus on Heap Dump and HPROF file structure.
- Carry forward Day 22's same-HPROF comparison gap by explaining records, classes, instances, references, GC roots, retained objects, and what Android Studio/LeakCanary/MAT each extract from the file.
- Include source/tooling commands and at least two Mermaid diagrams: one HPROF structure/parse path and one troubleshooting decision flow.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 22 -> Day 23
- Applied reflection: carried forward Day 22's same-HPROF comparison gap by treating HPROF as the shared object-graph source for Android Studio, LeakCanary/Shark, MAT, and raw/scripted checks.
- Visible change: added four Mermaid diagrams, HPROF record/sub-record/reference/root tables, same-dump tool comparison, MAT OQL starter commands, and before/after acceptance gates because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs a real target-app HPROF decoded across Android Studio, Shark, MAT, and a raw parser with target Android branch validation.

## Next Run: Day 24
- Keep the visual-first format.
- Focus on MAT intro and practical leak analysis.
- Carry forward Day 23's HPROF object graph foundation: records become classes, instances, references, GC roots, root paths, histograms, and retained-size evidence.
- Include histogram, Path To GC Roots, leak suspects, OQL, report export, and clear boundaries against Android Studio, LeakCanary/Shark, fd/native evidence.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 23 -> Day 24
- Applied reflection: carried forward Day 23's HPROF object graph foundation into a MAT workflow using Histogram, Path To GC Roots, Leak Suspects, Dominator Tree, OQL, and report export.
- Visible change: added four Mermaid diagrams, MAT view responsibility tables, Path To GC Roots option matrix, OQL starter queries, same-HPROF tool division, and before/after report gates because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs a real MAT report package and same-dump comparison across Android Studio, Shark, and MAT.

## Next Run: Day 25
- Keep the visual-first format.
- Focus on MAT Dominator Tree and Retained Heap.
- Carry forward Day 24's distinction between Root/Owner/Bridge/Victim ownership paths and retained-impact prioritization.
- Explain shallow heap, retained heap, immediate dominator, large owner/caches, Path To GC Roots cross-checking, and before/after retained-impact validation.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 24 -> Day 25
- Applied reflection: carried forward Day 24's distinction between ownership path and retained impact, making Dominator Tree a prioritization tool rather than a standalone leak verdict.
- Visible change: added four Mermaid diagrams, shallow/retained heap tables, immediate-dominator and dominance-frontier explanations, cache-versus-leak matrices, OQL helper checks, and retained-impact acceptance gates because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs a real MAT retained tree export, same-object Path To GC Roots comparison, and concrete cache trim-memory evidence.

## Next Run: Day 26
- Keep the visual-first format.
- Focus on Allocation Tracker and object allocation hotspots.
- Carry forward Day 25's boundary: allocation churn, retained heap, and leak ownership are different questions and need different evidence.
- Explain allocation recording, call stacks, object churn, cold-start/page-scroll spikes, before/after allocation budgets, and pairing Allocation Tracker with HPROF/MAT/Profiler evidence.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 25 -> Day 26
- Applied reflection: carried forward Day 25's boundary by separating allocation churn, allocation peaks, retained heap, and leak ownership into different evidence paths.
- Visible change: added four Mermaid diagrams, allocation evidence tables, call-stack interpretation, hotspot repair strategies, before/after allocation budgets, and HPROF/MAT/Profiler acceptance gates because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real Android Studio allocation recordings, Perfetto GC/frame correlation, and runnable sample-app allocation budgets.

## Next Run: Day 27
- Keep the visual-first format.
- Focus on `dumpsys meminfo` output fields: PSS/RSS/USS and process memory categories.
- Carry forward Day 26's allocation evidence by connecting Java Heap, Native Heap, Graphics, Stack, Code, Others, SQL/CursorWindow, Objects, fd, profiler, HPROF, MAT, and allocation recordings to process memory accounting.
- Include before/after meminfo validation for leak, peak, cache, resource, and native/graphics cases.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 26 -> Day 27
- Applied reflection: carried forward Day 26's request to connect allocation evidence with `dumpsys meminfo` Java Heap, Native Heap, Graphics, SQL, Objects, fd, and PSS/RSS/USS process accounting.
- Visible change: added three Mermaid diagrams, PSS/RSS/USS comparison, meminfo bucket attribution table, same-scenario before/after sequence, acceptance matrix, command templates, and AOSP source-search paths because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real device meminfo samples, vendor/version comparison, source-level libmeminfo validation, and an automated before/after parser.

## Next Run: Day 28
- Keep the visual-first format.
- Focus on `procrank`, `showmap`, and the system-wide memory view.
- Carry forward Day 27's PSS/RSS/USS boundary and compare process ranking, per-mapping attribution, shared/private accounting, `smaps`, `smaps_rollup`, and `dumpsys meminfo`.
- Explain how to move from one-process meminfo to system pressure: top PSS processes, shared libraries, ZRAM/swap hints, native mappings, ashmem/memfd/dma-buf candidates, and low-memory triage.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.
