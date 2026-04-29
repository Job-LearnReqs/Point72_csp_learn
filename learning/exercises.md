# CSP Exercises

Use these exercises while following [`README.md`](README.md). Keep changes small
and run the relevant sample after each step.

## Exercise 1: Arithmetic Nodes

Starting point: [`../samples/sum_constants.py`](../samples/sum_constants.py)

Tasks:

1. Add `subtract(left: ts[int], right: ts[int]) -> ts[int]`.
2. Add `multiply(left: ts[int], right: ts[int]) -> ts[int]`.
3. Print `difference` and `product`.
4. Change `left` and `right` to two other values.

Questions:

- What type does each node receive?
- Why is `csp.valid(left, right)` needed?
- Which lines execute during graph construction, and which logic executes during
  graph runtime?

## Exercise 2: Quote Metrics

Starting point: [`../samples/spread.py`](../samples/spread.py)

Tasks:

1. Add `trade_vs_mid(last_trade: ts[float], mid: ts[float]) -> ts[float]`.
2. Add a constant `last_trade`.
3. Print the new metric.
4. Add `is_wide_spread(spread_value: ts[float]) -> ts[bool]`.

Questions:

- Which nodes depend directly on `bid` and `ask`?
- Which nodes depend on another derived node?
- What happens if `mid` is zero?

## Exercise 3: Graph Sketch

Draw the graph for `samples/spread.py` in text:

```text
bid -----> spread ------> pct_spread
ask -----> spread
bid -----> midprice ----> pct_spread
ask -----> midprice
```

Tasks:

1. Update the sketch after adding `last_trade` and `trade_vs_mid`.
2. Mark each raw input.
3. Mark each derived time series.
4. Mark each printed output.

Questions:

- Which pieces are business logic?
- Which pieces are graph wiring?
- Which pieces are output behavior?

## Exercise 4: Adapter Design

Do not write adapter code yet. Design the boundary.

Scenario: bid/ask events arrive historically from a file today and from a live
feed later.

Tasks:

1. List the fields each quote event must contain.
2. Decide which nodes should not care whether input is historical or realtime.
3. Write a short adapter contract in `learning/notes.md`.

Questions:

- What should the adapter output type be?
- Which calculations should remain unchanged?
- Where should logging or publishing results happen?

## Exercise 5: Capstone Review

After building `samples/quote_monitor.py`, review it with this checklist:

- Inputs are easy to identify.
- Every custom node has type annotations using `ts[...]`.
- Nodes check validity before using inputs.
- Graph wiring is separate from node definitions.
- Printed outputs make it easy to verify behavior.
- Domain formulas are independent of input source.

Reflection:

- What would you test with historical replay?
- What would you monitor in realtime?
- What would be the first adapter you would build for your own use case?
