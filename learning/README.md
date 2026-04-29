# Complete CSP Learning Path

This directory now contains two layers:

- This file: the original quick path using the local samples.
- [`COMPLETE_CSP_PLAN.md`](COMPLETE_CSP_PLAN.md): the full concept-wise plan for learning all major concepts from the upstream Point72/csp repository and wiki.

Start with the complete plan if your goal is broad CSP fluency rather than only
understanding this repository's starter scripts.

---

# Local Starter Path

This learning path is for building a working mental model of
[Point72/csp](https://github.com/Point72/csp) using this repository's dev
container and local examples.

`csp` is a reactive stream processing library. You define typed time-series
inputs, compose them through nodes inside a graph, and run that graph in
simulation or realtime mode. The key habit to build is thinking in event ticks:
values appear over time, nodes react only when their inputs are valid/ticking,
and the graph describes dataflow rather than an imperative loop.

## Outcomes

By the end of this path, you should be able to:

- Explain what a `ts[T]` time series represents.
- Write small `@csp.node` functions with correct validity checks.
- Compose nodes in a `@csp.graph`.
- Run and inspect graph output from local scripts.
- Distinguish core calculation logic from input/output adapters.
- Extend the local examples into a small streaming-style application.
- Navigate the upstream docs and examples without getting lost.

## Prerequisites

- Comfortable with Python functions and type annotations.
- Comfortable running scripts from a terminal.
- Basic familiarity with market-data terms such as bid, ask, spread, and
  midprice is helpful for `samples/spread.py`, but not required.

## Phase 0: Environment Readiness

Goal: confirm that the local setup can run CSP examples.

Read:

- [`../README.md`](../README.md)
- [`.devcontainer/requirements.txt`](../.devcontainer/requirements.txt)

Run:

```bash
python -c "import csp; print(csp.__version__)"
python samples/sum_constants.py
python samples/spread.py
```

Checkpoint:

- You can explain why the dev container installs `csp==0.15.0`.
- You can run both local samples and identify the printed values.

## Phase 1: The Smallest Graph

Goal: understand the minimum useful CSP program.

Read:

- [`../samples/sum_constants.py`](../samples/sum_constants.py)
- Upstream wiki: [First Steps](https://github.com/Point72/csp/wiki/First-Steps)
- Upstream wiki: [CSP Node](https://github.com/Point72/csp/wiki/CSP-Node)
- Upstream wiki: [CSP Graph](https://github.com/Point72/csp/wiki/CSP-Graph)

Concepts:

- `ts[int]` means "a time-series stream of integer values", not a plain `int`.
- `@csp.node` declares event-driven computation.
- `@csp.graph` wires nodes together.
- `csp.const` creates a constant time-series input.
- `csp.run` executes the graph from a start time.

Practice:

1. Change the constants in `samples/sum_constants.py`.
2. Add a second node named `multiply`.
3. Print both `total` and `product`.
4. Predict output before running the script.

Checkpoint:

- You can point to the exact line where plain Python values become CSP time
  series values.
- You can explain why `add` checks `csp.valid(left, right)`.

## Phase 2: Validity, Ticks, and Node Behavior

Goal: learn how nodes decide when they can produce output.

Read:

- [`../samples/spread.py`](../samples/spread.py)
- Upstream wiki: [Common Mistakes / FAQ](https://github.com/Point72/csp/wiki/Common-Mistakes)
- Upstream wiki: [Glossary](https://github.com/Point72/csp/wiki/Glossary)

Concepts:

- Inputs may or may not be valid at a given graph time.
- A node can return only when it has enough valid input state.
- `csp.valid(...)` protects calculations from missing input values.
- A graph is declarative wiring; the engine manages execution order.

Practice:

1. Add a node named `is_wide_spread(spread_value: ts[float]) -> ts[bool]`.
2. Return `True` when spread is greater than `0.10`.
3. Print the result.
4. Change bid/ask values and confirm behavior.

Checkpoint:

- You can explain the difference between "a Python function was called while
  building the graph" and "a CSP node computes values while the graph runs".

## Phase 3: Composing Financial Calculations

Goal: build confidence composing multiple nodes.

Read:

- [`../samples/spread.py`](../samples/spread.py)
- Upstream examples directory:
  [Point72/csp examples](https://github.com/Point72/csp/tree/main/examples)

Concepts:

- Derived time series can feed later nodes.
- Small nodes are easier to test and reuse.
- Domain formulas should stay independent of where data comes from.

Practice:

Create `samples/quote_metrics.py` with:

- constant `bid`, `ask`, and `last_trade` inputs
- `spread`
- `midprice`
- `pct_spread`
- `trade_vs_mid`, returning `last_trade - mid`
- printed outputs for every metric

Checkpoint:

- You can draw the graph as arrows from inputs to derived metrics.
- You can identify which nodes are reusable if bid/ask later come from a file,
  database, Kafka topic, or live feed.

## Phase 4: Execution Modes and Time

Goal: understand why CSP supports both simulation and realtime workflows.

Read:

- Upstream wiki: [Execution Modes](https://github.com/Point72/csp/wiki/Execution-Modes)
- Upstream README section describing simulation/realtime reuse:
  [Point72/csp README](https://github.com/Point72/csp)

Concepts:

- The same graph logic can be tested offline and deployed realtime.
- Start time matters because graph execution is time-indexed.
- Historical data and realtime data should connect through adapters, not by
  rewriting calculation nodes.

Practice:

1. Run the existing samples multiple times.
2. Observe that printed timestamps change but formulas do not.
3. Write a short note in `learning/notes.md`: what is graph time, and why is it
   useful?

Checkpoint:

- You can explain why event-time/replay capability is valuable for testing
  streaming logic.

## Phase 5: Built-In Nodes and Utilities

Goal: avoid writing custom nodes for things CSP already provides.

Read:

- Upstream wiki: [Base Nodes API](https://github.com/Point72/csp/wiki/Base-Nodes-API)
- Upstream wiki: [Math and Logic Nodes API](https://github.com/Point72/csp/wiki/Math-and-Logic-Nodes-API)
- Upstream wiki: [Statistical Nodes API](https://github.com/Point72/csp/wiki/Statistical-Nodes-API)

Concepts:

- CSP includes built-in operations for common stream transformations.
- Prefer built-ins where they make intent clearer.
- Custom nodes are best for domain-specific calculations.

Practice:

1. Browse the built-in node docs.
2. Pick three operations that could replace custom code in a larger project.
3. Record them in `learning/notes.md` with one sentence each.

Checkpoint:

- You can decide when to write a custom `@csp.node` versus using a built-in.

## Phase 6: Adapters and Boundaries

Goal: understand how CSP connects graph logic to real input/output systems.

Read:

- Upstream wiki: [Adapters](https://github.com/Point72/csp/wiki/Adapters)
- Upstream wiki: [IO with Adapters](https://github.com/Point72/csp/wiki/IO-with-Adapters)
- Upstream wiki: [Write Historical Input Adapters](https://github.com/Point72/csp/wiki/Write-Historical-Input-Adapters)
- Upstream wiki: [Write Realtime Input Adapters](https://github.com/Point72/csp/wiki/Write-Realtime-Input-Adapters)
- Upstream wiki: [Write Output Adapters](https://github.com/Point72/csp/wiki/Write-Output-Adapters)

Concepts:

- Adapters are the boundary between the graph and external systems.
- Historical input adapters make replay/testing practical.
- Realtime input adapters let the same calculations process live events.
- Output adapters publish results without embedding side effects in core nodes.

Practice:

Design only, no implementation yet:

1. Sketch how bid/ask could arrive from a CSV or Parquet file.
2. Sketch how the same bid/ask could arrive from a realtime feed.
3. Identify which code should remain unchanged between both versions.

Checkpoint:

- You can separate calculation nodes from data-source integration.

## Phase 7: Capstone

Goal: build a small end-to-end CSP application in this repo.

Build:

- `samples/quote_monitor.py`

Suggested behavior:

- Input constants for `symbol`, `bid`, `ask`, and `last_trade`.
- Derived metrics: spread, midprice, percent spread, trade versus mid.
- Boolean alert: spread is wider than a chosen threshold.
- Printed output for raw inputs, derived metrics, and alert state.

Stretch goals:

- Replace constants with an upstream example adapter pattern.
- Add a second symbol using baskets after reading the basket docs.
- Profile the graph after reading the profiling docs.

Read if doing stretch goals:

- Upstream wiki: [Create Dynamic Baskets](https://github.com/Point72/csp/wiki/Create-Dynamic-Baskets)
- Upstream wiki: [Historical Buffers](https://github.com/Point72/csp/wiki/Historical-Buffers)
- Upstream wiki: [Profile CSP Code](https://github.com/Point72/csp/wiki/Profile-CSP-Code)

Final checkpoint:

- You can explain the application in terms of inputs, nodes, graph wiring,
  execution mode, and outputs.
- You can name what would change when moving from constant inputs to historical
  replay or realtime ingestion.

## Reference Map

- Project setup: [`../README.md`](../README.md)
- Local first example: [`../samples/sum_constants.py`](../samples/sum_constants.py)
- Local market example: [`../samples/spread.py`](../samples/spread.py)
- Upstream repository: <https://github.com/Point72/csp>
- Upstream wiki: <https://github.com/Point72/csp/wiki>
- Upstream examples: <https://github.com/Point72/csp/tree/main/examples>
