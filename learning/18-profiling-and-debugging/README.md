# 18 Profiling And Debugging

## Read

- <https://github.com/Point72/csp/wiki/Profile-CSP-Code>
- <https://github.com/Point72/csp/wiki/csp.profiler-API>
- <https://github.com/Point72/csp/wiki/Common-Mistakes>

## Concepts

- graph performance
- node-level cost
- event volume
- profiling output
- diagnosing slow graphs

## Practice Setup

Create `practice.py` with:

- a deliberately small graph
- a slightly heavier custom node
- profiler usage if supported by your installed CSP version

Create `profile_notes.md` with what was measured, what looked expensive, and
what you would optimize first.

## Checkpoint

You can describe whether a graph is slow because of event volume, node logic,
adapter IO, or output side effects.
