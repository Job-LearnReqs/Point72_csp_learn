# 05 Types Structs And Data Modeling

## Read

- <https://github.com/Point72/csp/wiki/csp.Struct-API>
- <https://github.com/Point72/csp/wiki/CSP-Node>
- <https://github.com/Point72/csp/wiki/Input-Output-Adapters-API>

## Concepts

- Python primitive types in `ts[...]`
- structured events
- `csp.Struct`
- event schema design
- conversion to and from dictionaries
- stable domain schemas across adapters

## Practice Setup

Create `practice.py` with:

- a `Quote` struct containing `symbol`, `bid`, and `ask`
- a `Trade` struct containing `symbol`, `price`, and `size`
- nodes that consume `ts[Quote]` and `ts[Trade]`
- a node that emits a derived struct or scalar metric

## Checkpoint

You can decide when to pass separate streams such as `bid` and `ask` versus a
single structured quote event.
