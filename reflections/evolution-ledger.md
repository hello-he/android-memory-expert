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

### Day 27 -> Day 28
- Applied reflection: carried forward Day 27's PSS/RSS/USS boundary from single-process `dumpsys meminfo` into `procrank` process ranking and `showmap`/`smaps` per-mapping attribution.
- Visible change: added three Mermaid diagrams, procrank field table, showmap mapping matrix, low-memory triage flow, capture template, combined diagnosis matrix, and AOSP source-search commands because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real low-memory snapshots, vendor/version field validation, a parser joining procrank/showmap/meminfo, and deeper dma-buf ownership examples.

## Next Run: Day 29
- Keep the visual-first format.
- Focus on JNI Local/Global Reference and cross-boundary leaks.
- Carry forward Day 28's system/mapping view by correlating Java retained paths, JNI reference tables, native owner lifetime, `meminfo`, `showmap`, and HPROF evidence.
- Explain local references, global references, weak global references, reference table overflow, `DeleteLocalRef`, `DeleteGlobalRef`, thread attach/detach, native owner cleanup, and before/after validation.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 28 -> Day 29
- Applied reflection: carried forward Day 28's system/mapping view into JNI by correlating Java retained paths, JNI reference tables, native owner lifetime, `meminfo`, `showmap`, HPROF, and heapprofd/fd evidence.
- Visible change: added three Mermaid diagrams, JNI reference lifecycle table, cross-boundary leak matrix, code red-line repair table, before/after validation chain, command templates, and ART/app source-search paths because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real HPROF JNI global-root examples, ART branch validation, heapprofd correlation, and a runnable NDK leak/fix sample.

## Next Run: Day 30
- Keep the visual-first format.
- Focus on `NewByteArray`, `GetPrimitiveArrayCritical`, `GetByteArrayElements`, release modes, and `DirectByteBuffer` memory ownership.
- Carry forward Day 29's JNI boundary by distinguishing Java array retention, copied native buffers, pinned/critical arrays, direct buffer native memory, release timing, and `meminfo`/`showmap`/HPROF evidence.
- Explain where bytes live, who owns release, how stalls or GC blocking can happen, and how to validate before/after.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 29 -> Day 30
- Applied reflection: carried forward Day 29's JNI boundary into byte-transfer APIs by distinguishing Java arrays, copied buffers, critical/pinned access, DirectByteBuffer wrappers, native memory ownership, release timing, and `meminfo`/`showmap`/HPROF evidence.
- Visible change: added three Mermaid diagrams, JNI byte API ownership table, release mode matrix, DirectByteBuffer split, troubleshooting flow, command templates, acceptance matrix, and AOSP/app source-search paths because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real Perfetto critical-section traces, ART branch validation, runnable NDK samples, and heapprofd/showmap/HPROF DirectByteBuffer artifacts.

## Next Run: Day 31
- Keep the visual-first format.
- Focus on Native Heap allocators: jemalloc, Scudo, malloc debugging, arenas, fragmentation, and native allocation evidence.
- Carry forward Day 30's native byte ownership by showing how native buffers appear in malloc_debug, heapprofd, showmap, smaps, Native Heap, and allocator metadata.
- Explain allocator-level symptoms, leak versus fragmentation versus cache, and before/after validation.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 30 -> Day 31
- Applied reflection: carried forward Day 30's native byte ownership into Native Heap allocators by showing how buffers appear in malloc_debug, heapprofd, showmap, smaps, Native Heap, and allocator metadata.
- Visible change: added three Mermaid diagrams, allocator/tool comparison, leak-versus-fragmentation-versus-cache matrix, same-scenario evidence loop, command templates, diagnosis matrix, and AOSP/app source-search paths because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real heapprofd/malloc_debug traces, target allocator/version validation, runnable native samples, and a parser joining meminfo/showmap/smaps/heapprofd.

## Next Run: Day 32
- Keep the visual-first format.
- Focus on `/proc/<pid>/maps`, `smaps`, `smaps_rollup`, and native memory mapping layout attribution.
- Carry forward Day 31's allocator evidence by mapping Native Heap, anon mmap, ashmem, memfd, stack, code, and file mappings to `meminfo`/`showmap`/`smaps` evidence.
- Explain mapping names, permissions, PSS/private dirty/swap fields, before/after mapping deltas, and owner evidence boundaries.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 31 -> Day 32
- Applied reflection: carried forward Day 31's allocator evidence into `/proc/<pid>/maps`, `smaps`, and `smaps_rollup` by mapping Native Heap, anon mmap, ashmem, memfd, stack, code, file-backed mappings, and dalvik spaces to `meminfo`/`showmap`/`smaps` evidence.
- Visible change: added three Mermaid diagrams, maps-line field table, permission table, smaps field table, mapping type table, mapping delta flow, tool-combination matrix, command templates, and AOSP/source searches because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real before/after maps/smaps artifacts, Android/version permission validation, a per-mapping delta parser, and detailed shared-buffer owner examples.

## Next Run: Day 33
- Keep the visual-first format.
- Focus on `mmap`, ashmem, memfd, and dma-buf accounting.
- Carry forward Day 32's mapping-name and owner-proof boundaries: mapping names narrow the search, but fd owner, producer-consumer ownership, dmabuf tools, and shared/private/PSS accounting decide the case.
- Explain file-backed versus anonymous mmap, ashmem versus memfd, dma-buf producer-consumer ownership, fd paths, shared/private/PSS accounting, and why process-local mapping views can miss real buffer owners.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 32 -> Day 33
- Applied reflection: carried forward Day 32's mapping-name and owner-proof boundaries into `mmap`, ashmem, memfd, and dma-buf accounting.
- Visible change: added three Mermaid diagrams, file-backed versus anonymous mmap table, ashmem/memfd/dma-buf comparison, producer-consumer dma-buf sequence, fd/dmabuf capture template, diagnosis matrix, and source-search commands because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real ashmem/memfd/dma-buf artifacts, version/permission validation, runnable shared-buffer leak samples, and a parser joining fd/smaps/dmabuf/meminfo.

## Next Run: Day 34
- Keep the visual-first format.
- Focus on Native memory leak tooling: heapprofd, malloc_debug, Perfetto, maps, smaps, meminfo, and fd evidence.
- Carry forward Day 33's owner-proof boundary by showing how native allocation stacks, shared mappings, fd diffs, and system buffer evidence are joined into one leak workflow.
- Explain when to use heapprofd versus malloc_debug, how to capture traces, how to connect stacks to `meminfo`/`showmap`, and how to validate fixes.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 33 -> Day 34
- Applied reflection: carried forward Day 33's owner-proof boundary into native leak tooling by joining heapprofd stacks, malloc_debug reports, Perfetto timelines, shared mappings, fd diffs, dmabuf/System buffer evidence, and `meminfo`/`showmap`/`smaps` bills.
- Visible change: added three Mermaid diagrams, tool responsibility table, tool-selection matrix, heapprofd/malloc_debug reading tables, before/after validation sequence, acceptance matrix, and source-search commands because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real heapprofd/malloc_debug/Perfetto artifacts, version-specific config validation, runnable leak samples, and automated stack/bucket/mapping/fd comparison.

## Next Run: Day 35
- Keep the visual-first format.
- Focus on Native Crash and tombstone: from signal to backtrace.
- Carry forward Day 34's memory ownership and native tool evidence by connecting signal, tombstone, fault address, registers, backtrace, memory map, allocator/sanitizer evidence, symbols, and ownership path.
- Explain how to decide whether the crash is null dereference, UAF, double free, buffer overflow, abort, or resource/lifetime misuse.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 34 -> Day 35
- Applied reflection: carried forward Day 34's native tool evidence into tombstone analysis by connecting signal, abort reason, fault address, registers, backtrace, memory map, allocator/sanitizer evidence, symbols, and ownership path.
- Visible change: added three Mermaid diagrams, tombstone section table, signal and fault-address matrices, tombstone-to-owner sequence, collection/symbolication commands, and source-search paths because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real tombstones, Android/ABI format validation, runnable crash samples, and full symbolication examples.

## Next Run: Day 36
- Keep the visual-first format.
- Focus on memory corruption models: out-of-bounds, memory stomping, UAF, double free, stack corruption, and allocator metadata corruption.
- Carry forward Day 35's tombstone evidence by mapping each corruption type to signal, fault address, allocator/sanitizer clues, reproduction strategy, and fix pattern.
- Explain how ASan/HWASan/GWP-ASan/Scudo/malloc_debug evidence differs and when tombstone alone is insufficient.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 35 -> Day 36
- Applied reflection: carried forward Day 35's tombstone evidence by mapping signal, fault address, registers, backtrace, memory map, allocator messages, and sanitizer evidence to OOB, UAF, double free, stomping, stack corruption, mmap/fd lifecycle errors, and allocator metadata corruption.
- Visible change: added four Mermaid diagrams, corruption taxonomy, Day 35 evidence mapping flow, troubleshooting decision flow, UAF sequence, symptom-to-fix evidence loop, tool evidence matrix, repair matrix, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real sanitizer/allocator reports, version/ABI validation, runnable native corruption samples, and archived symbolized crash artifacts.

## Next Run: Day 37
- Keep the visual-first format.
- Focus on ASan detection of Native memory errors: build configuration, runtime setup, redzones, shadow memory, report fields, alloc/free/use stacks, symbolization, and validation.
- Carry forward Day 36's taxonomy by showing how ASan report fields confirm OOB, UAF, double free, invalid free, and stack/global overflow models.
- Explain Android app/native library setup, reproduction commands, report reading, false-boundary cases, and before/after acceptance.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 36 -> Day 37
- Applied reflection: carried forward Day 36's corruption taxonomy into ASan report reading by mapping OOB, UAF, double free, invalid free, stack overflow, and global overflow to ASan error type, redzone, shadow memory, access stack, allocation stack, and free stack evidence.
- Visible change: added four Mermaid diagrams, ASan runtime structure, report-to-model mapping, Android setup flow, UAF evidence sequence, report field tables, command templates, false-boundary matrix, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real device ASan reports, concrete Gradle/CMake flag validation, runnable NDK samples, and symbolization failure examples.

## Next Run: Day 38
- Keep the visual-first format.
- Focus on HWASan and Android whole-device or app-focused memory error detection.
- Carry forward Day 37's ASan workflow by comparing redzone/shadow evidence with HWASan tag mismatch, allocation tag, memory tag, stack traces, and Android 64-bit setup boundaries.
- Explain when HWASan finds UAF/OOB more effectively, how to read reports, and how to validate fixes against the Day 36 taxonomy.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 37 -> Day 38
- Applied reflection: carried forward Day 37's ASan workflow by replacing redzone/shadow evidence with HWASan pointer tag, memory tag, tag mismatch, access stack, allocation stack, and reuse clues.
- Visible change: added four Mermaid diagrams, ASan-versus-HWASan comparison, report-field table, Android support boundary table, decision flow, tool-selection matrix, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real HWASan reports, setup validation, compatibility notes, runnable paired ASan/HWASan samples, and overhead data.

## Next Run: Day 39
- Keep the visual-first format.
- Focus on GWP-ASan, Scudo, and MTE as low-overhead detection and runtime protection mechanisms.
- Carry forward Day 38's tool-boundary comparison by explaining overhead, coverage, sampled detection, allocator hardening, hardware tagging, deployment scope, and report interpretation.
- Compare these mechanisms against ASan/HWASan and explain where each fits in debug, dogfood, beta, production-adjacent, and platform builds.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 38 -> Day 39
- Applied reflection: carried forward Day 38's tool-boundary comparison into GWP-ASan, Scudo, and MTE by contrasting sampled detection, allocator hardening, hardware tagging, overhead, deployment scope, and report interpretation.
- Visible change: added four Mermaid diagrams, three-layer protection structure, decision flow, GWP-ASan sampled sequence, Scudo check flow, mechanism comparison tables, MTE mode table, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real GWP-ASan/Scudo/MTE artifacts, property/setup validation, overhead data, and rollout policy.

## Next Run: Day 40
- Keep the visual-first format.
- Focus on KASAN and KFENCE for kernel memory out-of-bounds and UAF detection.
- Carry forward Day 39's low-overhead versus strong-detection comparison into kernel heap, slab, page allocator, reports, overhead, and deployment boundaries.
- Explain how kernel memory reports differ from user-space ASan/HWASan/GWP-ASan/Scudo/MTE evidence and how to preserve symbols, config, console logs, and repro steps.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 39 -> Day 40
- Applied reflection: carried forward Day 39's low-overhead versus strong-detection comparison into kernel memory debugging by contrasting KASAN strong instrumentation with KFENCE sampled guarded allocations.
- Visible change: added four Mermaid diagrams, kernel memory bug structure, KASAN-versus-KFENCE comparison flow, report-reading structure, troubleshooting flow, kernel object table, report field matrix, evidence checklist, repair matrix, commands, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real KASAN/KFENCE reports, validated kernel configs, runnable kernel samples, vmlinux/module symbolization, and overhead/stability data. Day 40 push was blocked after local commit because `git push` could not resolve `github.com`.

## Next Run: Day 41
- Keep the visual-first format.
- Focus on Bitmap memory model changes before and after Android 8.0.
- Carry forward Day 40's boundary discipline by separating Java object wrappers, native pixel storage, Graphics/dma-buf paths, allocator evidence, and Android version differences.
- Explain how Bitmap memory appears in Java Heap, Native Heap, Graphics, ashmem/dma-buf, meminfo, HPROF, and image library caches across versions.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 40 -> Day 41
- Applied reflection: carried forward Day 40's boundary discipline by separating Bitmap Java wrappers, native objects, pixel storage, Graphics/dma-buf buffers, caches, pools, and Android version differences.
- Visible change: added four Mermaid diagrams, Bitmap memory structure, Android 8.0 before/after accounting flow, troubleshooting flow, decode peak sequence, attribution tables, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real Android version samples, Skia/platform validation, runnable image-loading variants, and image-library cache artifacts.

## Next Run: Day 42
- Keep the visual-first format.
- Focus on Bitmap pixel data, Native Heap, Graphics, and dma-buf attribution.
- Carry forward Day 41's split between wrapper ownership and pixel accounting, adding stronger evidence paths for meminfo, showmap, smaps, heapprofd, HardwareBuffer, and dma-buf.
- Explain software versus hardware Bitmap bills, shared buffers, texture upload, decode temporary memory, and before/after attribution.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 41 -> Day 42
- Applied reflection: carried forward Day 41's split between Bitmap wrapper ownership and pixel accounting by joining HPROF, meminfo, showmap/smaps, heapprofd, Graphics, HardwareBuffer, and dma-buf evidence.
- Visible change: added four Mermaid diagrams, pixel attribution path, evidence stitching flow, troubleshooting flow, fix validation flow, pixel-size tables, tool-proof matrix, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real Bitmap artifacts, device/version validation, hardware Bitmap dmabuf examples, and automated delta calculations.

## Next Run: Day 43
- Keep the visual-first format.
- Focus on BitmapFactory.Options, inSampleSize, inBitmap, and decode peak control.
- Carry forward Day 42's attribution workflow by showing how sampling, reuse, temporary buffers, transforms, and cache insertion change Native Heap and Graphics peaks.
- Explain decode bounds pass, sample-size math, reuse constraints, hardware Bitmap limits, before/after meminfo, and HPROF validation.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 42 -> Day 43
- Applied reflection: carried forward Day 42's attribution workflow into BitmapFactory.Options by showing how bounds pass, inSampleSize, inBitmap reuse, temporary buffers, transforms, and cache insertion affect Native Heap and Graphics peaks.
- Visible change: added four Mermaid diagrams, decode peak path, inSampleSize decision flow, inBitmap reuse sequence, troubleshooting flow, option/evidence tables, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real decoder traces, compatibility validation, runnable samples, and image quality tradeoff data.

## Next Run: Day 44
- Keep the visual-first format.
- Focus on Glide memory cache architecture: LruCache, BitmapPool, EngineResource, ActiveResources, lifecycle, and trim behavior.
- Carry forward Day 43's decode peak controls by mapping Glide request, decode, transform, cache insertion, pool reuse, and lifecycle release to Java Heap, Native Heap, and Graphics evidence.
- Explain how to distinguish cache policy, pool reuse, lifecycle leak, and decode peak in Glide-based apps.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 43 -> Day 44
- Applied reflection: carried forward Day 43's decode peak controls into Glide by mapping request, decode, transform, cache insertion, pool reuse, lifecycle release, and trim behavior to Java Heap, Native Heap, and Graphics evidence.
- Visible change: added four Mermaid diagrams, Glide memory path, cache-versus-leak troubleshooting flow, BitmapPool reuse sequence, lifecycle/trim flow, role tables, validation matrix, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real Glide metrics, version-specific source validation, runnable feed samples, and Coil/Picasso comparison.

## Next Run: Day 45
- Keep the visual-first format.
- Focus on large image loading strategies: Region Decode, Tile loading, subsampling, viewport-driven memory, and peak control.
- Carry forward Day 44's cache/pool/lifecycle boundaries by showing how large image viewers avoid full decode and manage tiles, caches, and native/graphics memory.
- Explain tile lifecycle, visible-window decode, cache eviction, gestures/zoom, and before/after memory evidence.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 44 -> Day 45
- Applied reflection: carried forward Day 44's cache/pool/lifecycle boundaries into large image viewers by focusing on Region Decode, tiles, viewport/zoom budgets, cache eviction, decode cancellation, and native/graphics memory.
- Visible change: added four Mermaid diagrams, large-image memory structure, region-decode decision flow, tile lifecycle sequence, troubleshooting flow, budget table, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real pan/zoom traces, region decode compatibility validation, GPU/dma-buf evidence, and tile-size tradeoff data.

## Next Run: Day 46
- Keep the visual-first format.
- Focus on hardware acceleration, RenderThread, GPU memory, and dma-buf.
- Carry forward Day 45's CPU/GPU tile boundary by explaining texture upload, RenderThread ownership, SurfaceFlinger visibility, dma-buf producer-consumer ownership, and Graphics meminfo validation.
- Explain app process, RenderThread, GPU driver, SurfaceFlinger, HardwareBuffer, texture cache, and before/after evidence.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 45 -> Day 46
- Applied reflection: carried forward Day 45's CPU/GPU tile boundary into hardware acceleration by explaining texture upload, RenderThread ownership, SurfaceFlinger visibility, dma-buf producer-consumer ownership, and Graphics meminfo validation.
- Visible change: added four Mermaid diagrams, hardware acceleration memory path, Graphics evidence chain, troubleshooting flow, RenderThread/GPU/SurfaceFlinger sequence, evidence tables, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real SurfaceFlinger/fd/dmabuf/Perfetto artifacts, vendor GPU validation, runnable surface samples, and texture/layer cost data.

## Next Run: Day 47
- Keep the visual-first format.
- Focus on Android process memory limits: memoryClass, largeHeap, per-process ceilings, LMKD risk, and bucket-specific growth.
- Carry forward Day 46's Graphics/dma-buf boundary by explaining why largeHeap does not solve Graphics/native/shared-buffer pressure.
- Explain Java heap limit, native heap growth, graphics/shared buffers, process state, oom_score_adj, and before/after evidence.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 46 -> Day 47
- Applied reflection: carried forward Day 46's Graphics/dma-buf boundary into process memory limits by explaining why `largeHeap` only affects Java heap headroom and does not solve native, Graphics, shared-buffer, or LMKD pressure.
- Visible change: added four Mermaid diagrams, process memory bill, memoryClass/largeHeap flow, LMKD risk path, troubleshooting flow, bucket tables, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real memoryClass data, ActivityManager validation, LMKD logs, and largeHeap tradeoff measurements.

## Next Run: Day 48
- Keep the visual-first format.
- Focus on Android low-memory overview: RAM, ZRAM, kswapd, PSI, and LMKD.
- Carry forward Day 47's process bucket boundaries into system-wide pressure by connecting PSS/RSS, reclaim, swap, PSI, and kill decisions.
- Explain how app-local Java/Native/Graphics growth becomes system pressure and how to collect meminfo, vmstat, PSI, zram, and lmkd evidence.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 47 -> Day 48
- Applied reflection: carried forward Day 47's process bucket boundaries into Android low-memory overview by connecting Java Heap, Native Heap, Graphics, PSS/RSS, reclaim, ZRAM, PSI, and LMKD decisions.
- Visible change: added four Mermaid diagrams, low-memory system structure, app-to-system pressure flow, troubleshooting flow, VM/ZRAM/PSI/LMKD sequence, metric tables, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real low-memory artifacts, metric/log format validation, Perfetto traces, and device-class thresholds.

## Next Run: Day 49
- Keep the visual-first format.
- Focus on Linux Page Reclaim: file/anon pages, LRU, and MGLRU.
- Carry forward Day 48's system pressure chain by explaining how file and anon pages enter reclaim, how LRU/MGLRU selects pages, and how vmstat/Perfetto/PSI evidence proves reclaim cost.
- Explain clean file cache reclaim, dirty writeback, anon swap/ZRAM, kswapd/direct reclaim, and thrashing boundaries.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 48 -> Day 49
- Applied reflection: carried forward Day 48's system pressure chain into Linux page reclaim by separating file pages, anon pages, LRU/MGLRU selection, kswapd, direct reclaim, ZRAM, PSI, and refault evidence.
- Visible change: added four Mermaid diagrams, reclaim overview, LRU/MGLRU comparison, kswapd/direct reclaim sequence, evidence flow, metric tables, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real reclaim traces, MGLRU validation, controlled workloads, and practical thrashing thresholds.

## Next Run: Day 50
- Keep the visual-first format.
- Focus on memory watermarks: zone, min/low/high watermark, lowmem reserves, and allocation/reclaim triggers.
- Carry forward Day 49's reclaim model by showing how watermarks decide kswapd wakeup, direct reclaim, allocation failure, and LMKD pressure.
- Explain zone watermarks, watermark boost/scale, min_free_kbytes, reserves, vmstat evidence, and before/after tuning risks.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 49 -> Day 50
- Applied reflection: carried forward Day 49's reclaim model by showing how zone watermarks decide kswapd wakeup, direct reclaim, allocation failure, and LMKD pressure.
- Visible change: added four Mermaid diagrams, zone watermark structure, allocation decision flow, kswapd target sequence, tuning risk flow, evidence matrices, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real zoneinfo/vmstat/PSI samples, version-specific watermark sysctl validation, and measured tuning data.

## Next Run: Day 51
- Keep the visual-first format.
- Focus on low-end device jank caused by kswapd, direct reclaim, compaction, and allocation stalls.
- Carry forward Day 50's watermark boundaries by showing how low/min breaches become background reclaim, direct reclaim, compaction, PSI, and frame drops.
- Explain UI thread allocation, RenderThread stalls, order allocation, compaction cost, vmstat evidence, Perfetto alignment, and before/after validation.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 50 -> Day 51
- Applied reflection: carried forward Day 50's watermark boundaries by showing how low/min breaches become background reclaim, direct reclaim, compaction, PSI, and UI frame drops.
- Visible change: added four Mermaid diagrams, watermark-to-jank flow, UI/RenderThread sequence, reclaim-versus-compaction classifier, troubleshooting decision flow, evidence tables, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real Perfetto traces, device-specific vmstat validation, PSI thresholds, and runnable low-RAM workloads.

## Next Run: Day 52
- Keep the visual-first format.
- Focus on PSI memory pressure: `some/full`, `avg10/60/300`, stall interpretation, and thrashing judgment.
- Carry forward Day 51's jank model by using PSI to decide whether reclaim, compaction, or swap pressure is user-visible and sustained.
- Explain instantaneous versus averaged PSI, correlation with frame misses, reclaim/refault/swap evidence, and alert thresholds.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 51 -> Day 52
- Applied reflection: carried forward Day 51's jank model by using PSI `some/full` and `avg10/60/300` to decide whether reclaim, compaction, or swap pressure is user-visible and sustained.
- Visible change: added four Mermaid diagrams, PSI readout structure, stall-to-PSI sequence, thrashing decision flow, evidence graph, PSI pattern tables, command templates, and today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real PSI samples, RAM-class thresholds, vendor/version validation, and before/after traces.

## Next Run: Day 53
- Keep the visual-first format.
- Focus on memory waterline growth attribution using `meminfo`, `vmstat`, slab, dma-buf, and memcg.
- Carry forward Day 52's PSI model by using pressure windows to decide which growing memory bucket is actually causing stalls.
- Explain bucket attribution, global versus per-process views, kernel slab growth, dma-buf producers/consumers, memcg evidence, and before/after validation.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 52 -> Day 53
- Applied reflection: carried forward Day 52's PSI model by making PSI `avg10/60/300` the window selector before attributing `meminfo`, `vmstat`, slab, dma-buf, or memcg growth.
- Visible change: added four Mermaid diagrams, bucket attribution matrices, source path tables, command templates, and a today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real synchronized device samples, cgroup version validation, dma-buf permission validation, and automated timestamp alignment.

## Next Run: Day 54
- Keep the visual-first format.
- Focus on lmkd architecture: PSI/vmpressure, kill strategy, and key properties.
- Carry forward Day 53's bucket attribution by showing which pressure signals lmkd observes and which source bucket evidence lmkd does not preserve by itself.
- Explain pressure monitor inputs, kill thresholds, victim selection boundaries, Android properties, log evidence, and before/after validation.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 53 -> Day 54
- Applied reflection: carried forward Day 53's bucket attribution boundary into lmkd by separating pressure response from root-cause attribution.
- Visible change: added four Mermaid diagrams, lmkd input/stage/property tables, common misread matrix, command templates, and a today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real lmkd logs, statsd examples, Android branch property validation, and vendor low-RAM behavior.

## Next Run: Day 55
- Keep the visual-first format.
- Focus on ActivityManager OomAdjuster: process state to `oom_score_adj`.
- Carry forward Day 54's lmkd dependency on `oom_score_adj` by explaining how adj is computed, propagated, and audited before blaming lmkd.
- Explain process states, binding relationships, foreground service boundaries, cached process ranking, procfs evidence, dumpsys output, and source paths.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 54 -> Day 55
- Applied reflection: carried forward Day 54's lmkd dependency on `oom_score_adj` by making AMS/OomAdjuster state computation and procfs propagation the central evidence chain.
- Visible change: added four Mermaid diagrams, adj input/output/category tables, source path tables, case audit matrix, command templates, and a today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real dumpsys samples, branch-specific adj constants, binding/provider examples, and foreground service transition logs.

## Next Run: Day 56
- Keep the visual-first format.
- Focus on why lmkd can kill a seemingly higher-priority process.
- Carry forward Day 55's adj audit plus Day 53's bucket attribution to distinguish real priority bugs from shared-pressure, stale-evidence, and normal policy cases.
- Explain pressure timing, stale screenshots, process-state races, shared buffer ownership, RSS/PSS confusion, kill reason logs, and validation.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.

### Day 55 -> Day 56
- Applied reflection: carried forward Day 55's adj audit and Day 53's bucket attribution by requiring pressure, priority, and source-bucket evidence at the same lmkd kill timestamp.
- Visible change: added four Mermaid diagrams, common misread tables, timestamp evidence matrix, source path table, fix direction matrix, command templates, and a today's checklist because of the more-diagrams-less-prose feedback.
- Unresolved: GitHub Issues still require `gh auth login` or `GH_TOKEN`; the article still needs real lmkd incidents, statsd records, vendor log field validation, a reusable pre-kill sampler, and measured victim effectiveness.

## Next Run: Day 57
- Keep the visual-first format.
- Focus on lmkd logs, statsd, and victim analysis from kill reason to adj and RSS.
- Carry forward Day 56's three-line evidence model by decoding kill-record fields and building a victim worksheet.
- Explain logcat fields, statsd atoms, kill reason categories, victim memory cost, adj state, pressure context, and report template.
- If GitHub Issues still cannot be read, record the gh auth login or GH_TOKEN blocker in reflection, ledger, and automation memory.
- Validate JSON before git operations, then attempt `git add`, `git commit`, and `git push` with exact blocker logging on failure.
