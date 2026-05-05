# CSP Practical Exercise Solutions

These are reference approaches, not the only valid answers. Try the exercise
first, run `python learning/evaluate_exercises.py <id>`, then compare your
artifact with the relevant notes below.

## 00 Orientation

A complete summary says CSP models event streams as typed time series, composes
calculations in graphs, isolates external systems behind adapters, and lets the
same core graph logic run in simulation and realtime modes.

## 01 Installation and Environment

The environment script should import `csp`, print the Python executable/version,
print the CSP package location or version if available, and optionally run a tiny
constant graph to prove execution works.

## 02 First Steps

The reference shape is:

- `@csp.node` functions named `add`, `subtract`, and `multiply`
- each node accepts `ts[int]` inputs and checks `csp.valid(left, right)`
- one `@csp.graph` creates constants, wires derived streams, and prints inputs
  and outputs
- the `if __name__ == "__main__"` block calls `csp.run`

## 03 Nodes

Use separate nodes for separate ideas: a pure formula, an all-inputs-valid gate,
a counter using `with csp.state`, and a node that combines a scalar threshold or
factor with a time-series input. The graph should make it obvious which inputs
tick and which values are fixed scalar configuration.

## 04 Graphs

A good answer keeps `@csp.node` functions focused on runtime calculations and
uses one or more `@csp.graph` helpers to compose them into a pipeline. The
top-level graph should read like wiring: create inputs, call graph helpers, then
print or return outputs.

## 05 Types, Structs, Data Modeling

Define `Quote(csp.Struct)` and `Trade(csp.Struct)` with domain fields. Use nodes
that accept structured events and derive values such as spread, midprice, or
trade distance from mid. Structs are appropriate when fields belong to one event
schema and should move together.

## 06 Execution Modes and Time

The solution should make time explicit at the `csp.run` boundary. Keep the graph
and node logic independent from whether the run is historical or realtime; only
the run configuration and eventually the adapters should change.

## 07 Base Nodes

Show built-in operations for common stream behavior before writing custom nodes.
Valid examples include filtering, merging, sampling, delaying, counting,
flattening, or other base nodes supported by your installed CSP version.

## 08 Math, Logic, Functional Methods

Use generic helpers for generic arithmetic or boolean transformations, then add a
small custom node where a domain name makes the formula clearer. The explanation
should distinguish reuse of general helpers from domain-specific intent.

## 09 Statistical Nodes

The important part is bounded history. A complete answer names the window or
time horizon and computes metrics such as rolling mean, min/max, standard
deviation, or variance in a deterministic way over event time.

## 10 Baskets and Dynamic Graphs

The design should use one stream per symbol/key when each symbol can tick
independently. A list-valued stream is one stream whose whole list value ticks at
once; a basket preserves per-key timing and graph structure.

## 11 Historical Buffers and Feedback

Use delayed or historical values so the current output depends on a previous
tick/window, not on itself at the same instant. The reference explanation calls
out why immediate feedback creates an invalid cycle.

## 12 Adapters Overview and IO

A good adapter plan defines source schema, output stream types, lifecycle
responsibility, error behavior, and the boundary where external IO ends. Core
nodes and graph wiring should not know whether data came from a file, database,
or live feed.

## 13 Historical Input Adapters

The replay data should have a timestamp column and deterministic rows. Include
enough fields to reconstruct domain events, such as symbol, bid, ask, price, or
quantity. Keep values small enough to inspect manually.

## 14 Realtime Input Adapters

The design should cover connect, subscribe, transform external messages into
typed events, publish ticks into CSP, handle reconnect/error cases, and shut down
cleanly. Mention any queue, thread, process, or callback boundary.

## 15 Output Adapters

The output contract should state what event leaves the graph, where it goes, how
failures are handled, and what delivery semantics are expected. Side effects
belong at the output boundary rather than inside calculation nodes.

## 16 Built-In Adapters

The matrix should compare each candidate by source/sink system, schema support,
batch versus realtime behavior, operational requirements, and why it does or
does not fit the current use case.

## 17 Random Generators

The solution should generate synthetic ticks with repeatable configuration where
possible. Explain what behavior the generated stream is meant to test: load,
edge cases, distribution assumptions, or downstream graph behavior.

## 18 Profiling and Debugging

Separate likely cost sources: event volume, expensive node logic, adapter IO,
output side effects, and graph structure. A useful note records the command or
method used, the observation, and the next experiment.

## 19 Common Mistakes

Catalog each mistake with symptom, cause, fix, and a tiny example. Cover type
confusion, missing validity checks, doing runtime work at graph construction
time, and confusing historical/realtime behavior.

## 20 Example Catalog Study

For one upstream example, identify schemas, raw inputs, adapters, custom nodes,
graph helpers, execution mode, outputs, and one pattern you would reuse. The goal
is to learn how to read unfamiliar CSP programs systematically.

## 21 Capstone

The capstone scope should name the domain, event schemas, input source, output
sink, graph modules, node responsibilities, run modes, test strategy, and
profiling/debugging risks. Keep it small enough to finish end to end.
