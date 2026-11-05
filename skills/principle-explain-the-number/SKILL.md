---
name: principle-explain-the-number
description: Examine measured performance or evaluation claims for completed work, fair comparisons, uncertainty, and causal evidence before reporting conclusions or selecting an option.
---

# Explain the number

Define the claim, unit, population, and timed boundary. Inspect the measurement code. Verify successful work completed, including asynchronous consumers; distinguish attempted, queued, received, applied, and rendered work where relevant. Count failures and discarded results.

Compare equivalent workloads, builds, tuning, concurrency, cache states, and environments. Repeat and interleave trials. Preserve raw observations and report sample count and spread; justify exclusions. Follow required methodology without treating an arbitrary repetition count as sufficient precision.

Locate the limiting resource through a separate profile or counters, then connect the evidence to code. Reading code proposes a limiter; it does not measure one. Check bandwidth/capacity bounds and whether savings exceed the changed work's original share.

Investigate load-generator limits, skipped execution, stale binaries, overhead, and caching. Relate isolated improvements to the end-to-end outcome users experience. Keep rate-governed latency checks distinct from uncapped throughput experiments.

State the observed difference separately from its causal explanation. A credible observation may remain reproducible while its cause is unknown. Label unresolved mechanisms or an adoption comparison without comparable tuning as inconclusive. Keep assumptions and inference visible beside the numbers.

Adapted from pstack's [explain the number](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-explain-the-number/SKILL.md) and [benchmark checklist](https://github.com/cursor/plugins/blob/main/pstack/skills/benchmark-checklist/SKILL.md).
