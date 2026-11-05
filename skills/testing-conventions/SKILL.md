---
name: testing-conventions
description: Build reliable test harnesses and integration checks with isolated fixtures, controlled subprocesses, bounded synchronization, and useful failure evidence. Use for process, filesystem, network, and CI test infrastructure.
---

# Testing conventions

Inspect the repository's runner and existing conventions. Use focused tests for pure logic and real boundary tests for configuration, filesystem, transport, and process behavior. Keep ordinary checks fast; isolate expensive stress runs explicitly.

Give tests private state directories, ports, environment changes, and process ownership. For Git fixtures, control inherited config, signing, and identity. Resolve real executables independently from fake commands on PATH. Preserve production behavior while isolating the test environment.

Use readiness predicates and monotonic deadlines instead of assuming startup duration. Propagate worker failures and capture output before teardown. Cleanup must handle partial initialization and release only owned processes, sockets, files, and environment changes. Never reap shared services by name.

Parallelize only independent fixtures, with justified resource limits. Prefer event/condition synchronization to arbitrary sleeps. Use injectable clocks for time logic and real clocks for transport observations. Reproduce timing failures before adding retries or extending deadlines.

Check platform-specific discovery, inherited handles, runtime paths, and shutdown behavior. Diagnose the expensive boundary before sharding CI or changing instrumentation. Retain exact configuration, seed, exit status, and relevant failure output. Upstream-specific toolchain workarounds are evidence to investigate, not universal settings.

Adapted from [no-mistakes testing conventions](https://github.com/kunchenguid/no-mistakes/blob/main/.agents/skills/testing-conventions/SKILL.md).
