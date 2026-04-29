# 12 Adapters Overview And IO

## Read

- <https://github.com/Point72/csp/wiki/Adapters>
- <https://github.com/Point72/csp/wiki/IO-with-Adapters>
- <https://github.com/Point72/csp/wiki/Base-Adapters-API>
- <https://github.com/Point72/csp/wiki/Input-Output-Adapters-API>

## Concepts

- adapters as system boundaries
- input adapters
- output adapters
- historical versus realtime input
- separating domain graph logic from infrastructure

## Practice Setup

Create `adapter_plan.md` with:

- one historical data source
- one realtime data source
- one output sink
- event schema for each stream
- graph code that should not change across sources

## Checkpoint

You can draw a boundary between CSP graph logic and external IO.
