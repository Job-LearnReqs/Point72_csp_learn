# 14 Realtime Input Adapters

## Read

- <https://github.com/Point72/csp/wiki/Write-Realtime-Input-Adapters>
- <https://github.com/Point72/csp/wiki/Adapters>
- <https://github.com/Point72/csp/wiki/Execution-Modes>

## Concepts

- realtime event sources
- push-style input
- wall-clock behavior
- lifecycle management
- thread/process boundaries where applicable

## Practice Setup

Create `design.md` describing a realtime quote source:

- connection lifecycle
- subscription request
- event parsing
- error handling
- shutdown behavior

Then create `practice.py` with the smallest local realtime source you can build,
for example a timer or in-process generated event source.

## Checkpoint

You can describe what changes in the adapter layer when moving from replay to
live data, and what should not change in the graph.
