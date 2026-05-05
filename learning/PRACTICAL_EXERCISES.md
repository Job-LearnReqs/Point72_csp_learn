# CSP Practical Exercises

Use this file alongside the numbered topic folders. Each exercise gives you a
local artifact to build, then `learning/evaluate_exercises.py` checks whether the
artifact is present and has the expected structure.

Run one topic:

```bash
python learning/evaluate_exercises.py 03
```

Run all topics you have started:

```bash
python learning/evaluate_exercises.py --started
```

Skip executing Python practice files and run only static checks:

```bash
python learning/evaluate_exercises.py 03 --no-run
```

## Exercise Map

| # | Topic | Artifact | Practical Exercise |
| --- | --- | --- | --- |
| 00 | Orientation | `learning/00-orientation/summary.md` | Explain CSP in your own words, including events, graphs, adapters, simulation, and realtime reuse. |
| 01 | Installation and Environment | `learning/01-installation-and-environment/environment_check.py` | Import CSP, print Python/runtime details, and prove the local environment can run a CSP script. |
| 02 | First Steps | `learning/02-first-steps/practice.py` | Build constants, `add`, `subtract`, `multiply`, a graph, printed outputs, and a `csp.run` entrypoint. |
| 03 | Nodes | `learning/03-nodes/practice.py` | Demonstrate a stateless node, validity-gated node, stateful tick counter, and scalar-parameter node. |
| 04 | Graphs | `learning/04-graphs/practice.py` | Compose small graph helpers so wiring is visibly separate from event-time node logic. |
| 05 | Types, Structs, Data Modeling | `learning/05-types-structs-and-data-modeling/practice.py` | Define `Quote` and `Trade` structs and derive at least one stream from structured events. |
| 06 | Execution Modes and Time | `learning/06-execution-modes-and-time/practice.py` | Run the same graph with explicit `starttime` and `endtime` values. |
| 07 | Base Nodes | `learning/07-base-nodes/practice.py` | Demonstrate at least five built-in/base-node patterns before writing custom node logic. |
| 08 | Math, Logic, Functional Methods | `learning/08-math-logic-and-functional-methods/practice.py` | Compare generic math/logic transformations with one named domain node. |
| 09 | Statistical Nodes | `learning/09-statistical-nodes/practice.py` | Compute rolling or streaming metrics with explicit window/time semantics. |
| 10 | Baskets and Dynamic Graphs | `learning/10-baskets-and-dynamic-graphs/design.md` | Design a multi-symbol stream shape and explain why a basket differs from a list-valued stream. |
| 11 | Historical Buffers and Feedback | `learning/11-historical-buffers-and-feedback/practice.py` | Show a delayed dependency or historical lookup that avoids an instantaneous cycle. |
| 12 | Adapters Overview and IO | `learning/12-adapters-overview-and-io/adapter_plan.md` | Define the adapter boundary, graph contract, input schema, and output handoff. |
| 13 | Historical Input Adapters | `learning/13-historical-input-adapters/events.csv` | Create deterministic timestamped replay data with at least four rows. |
| 14 | Realtime Input Adapters | `learning/14-realtime-input-adapters/design.md` | Design connection, subscription, queue/threading, error, and shutdown behavior. |
| 15 | Output Adapters | `learning/15-output-adapters/output_contract.md` | Define output schema, sink semantics, side-effect boundary, and failure behavior. |
| 16 | Built-In Adapters | `learning/16-built-in-adapters/adapter_matrix.md` | Compare built-in adapter candidates against source, sink, schema, and operational fit. |
| 17 | Random Generators | `learning/17-random-generators/practice.py` | Generate a synthetic stream and explain how it supports simulation or tests. |
| 18 | Profiling and Debugging | `learning/18-profiling-and-debugging/profile_notes.md` | Separate event volume, node logic, adapter IO, output side effects, and graph shape costs. |
| 19 | Common Mistakes | `learning/19-common-mistakes/mistake_catalog.md` | Build a catalog with symptoms, causes, and fixes for type, validity, graph, and runtime mistakes. |
| 20 | Example Catalog Study | `learning/20-example-catalog-study/example_review_template.md` | Review one upstream example by classifying schemas, nodes, graphs, adapters, and outputs. |
| 21 | Capstone | `learning/21-capstone/README.md` | Define the end-to-end project scope and explain schema, input, graph, nodes, output, and run mode. |

## How To Use Each Exercise

1. Read the topic README.
2. Build or update the listed artifact.
3. Run the evaluator for that topic.
4. Fix failing checks until the artifact passes.
5. Compare your approach with [`SOLUTIONS.md`](SOLUTIONS.md).
6. Update [`PROGRESS.md`](PROGRESS.md) when the artifact works and you can
   answer the checkpoint without notes.

The evaluator is intentionally structural. Passing it means your artifact is a
reasonable practice attempt; it does not replace your checkpoint explanation.
