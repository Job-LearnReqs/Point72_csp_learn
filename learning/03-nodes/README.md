# 03 Nodes

## Read

- <https://github.com/Point72/csp/wiki/CSP-Node>
- <https://github.com/Point72/csp/wiki/Common-Mistakes>
- <https://github.com/Point72/csp/wiki/Glossary>

## Concepts

- `@csp.node`
- `ts[T]`
- scalar arguments versus time-series arguments
- valid inputs
- ticking inputs
- return values
- state inside nodes
- alarms and timers where applicable

## Practice Setup

Create `practice.py` with nodes that demonstrate:

- a stateless calculation
- a node that only emits when all inputs are valid
- a node that keeps a running count of ticks
- a node with one scalar parameter and one time-series input

## Checkpoint

You can explain why reading a `ts[float]` outside CSP runtime is a category
mistake.
