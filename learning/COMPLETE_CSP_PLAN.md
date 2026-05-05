# Complete CSP Learning Plan

This is a concept-wise study plan for
[Point72/csp](https://github.com/Point72/csp), beyond the small samples in this
repository.

The upstream docs organize CSP around tutorials, concepts, how-to guides, API
references, and examples. This plan mirrors that structure: first understand the
stream-processing model, then nodes and graphs, then execution, data modeling,
built-ins, adapters, dynamic graphs, profiling, and finally complete example
study.

## How To Use This Plan

Work through the folders in numeric order. Each concept folder contains:

- official reading links
- concepts to extract
- a local practice setup
- a checkpoint to prove understanding

Track your status in [`PROGRESS.md`](PROGRESS.md). Update it after every study
session with the current status, confidence score, evidence artifact, and next
action.

For interactive sessions, follow [`SESSION_WORKFLOW.md`](SESSION_WORKFLOW.md)
and start with:

```bash
python learning/start_session.py
```

For code exercises, create a `practice.py` inside the concept folder unless the
folder asks for a different artifact.

```bash
python learning/<concept-folder>/practice.py
```

Each topic also has a practical exercise and evaluator. See
[`PRACTICAL_EXERCISES.md`](PRACTICAL_EXERCISES.md), then run:

```bash
python learning/evaluate_exercises.py <concept-id>
```

Reference solution approaches live in [`SOLUTIONS.md`](SOLUTIONS.md). Try the
exercise before reading the relevant solution section.

## Concept Directory Map

| Order | Folder | Concept |
| --- | --- | --- |
| 00 | [`00-orientation`](00-orientation/README.md) | What CSP is and when to use it |
| 01 | [`01-installation-and-environment`](01-installation-and-environment/README.md) | Installation, dev container, version checks |
| 02 | [`02-first-steps`](02-first-steps/README.md) | Smallest runnable CSP program |
| 03 | [`03-nodes`](03-nodes/README.md) | `@csp.node`, `ts[...]`, validity, ticks |
| 04 | [`04-graphs`](04-graphs/README.md) | `@csp.graph`, wiring, graph utilities |
| 05 | [`05-types-structs-and-data-modeling`](05-types-structs-and-data-modeling/README.md) | Types, `csp.Struct`, event schemas |
| 06 | [`06-execution-modes-and-time`](06-execution-modes-and-time/README.md) | Simulation, realtime, graph time |
| 07 | [`07-base-nodes`](07-base-nodes/README.md) | Core built-in nodes |
| 08 | [`08-math-logic-and-functional-methods`](08-math-logic-and-functional-methods/README.md) | Math, boolean, and functional helpers |
| 09 | [`09-statistical-nodes`](09-statistical-nodes/README.md) | Rolling and streaming statistics |
| 10 | [`10-baskets-and-dynamic-graphs`](10-baskets-and-dynamic-graphs/README.md) | Baskets and dynamic graph construction |
| 11 | [`11-historical-buffers-and-feedback`](11-historical-buffers-and-feedback/README.md) | Historical windows, feedback, delayed edges |
| 12 | [`12-adapters-overview-and-io`](12-adapters-overview-and-io/README.md) | Adapter architecture and IO boundaries |
| 13 | [`13-historical-input-adapters`](13-historical-input-adapters/README.md) | Historical input adapters |
| 14 | [`14-realtime-input-adapters`](14-realtime-input-adapters/README.md) | Realtime input adapters |
| 15 | [`15-output-adapters`](15-output-adapters/README.md) | Output adapters and sinks |
| 16 | [`16-built-in-adapters`](16-built-in-adapters/README.md) | Kafka, Parquet, DBReader, and related APIs |
| 17 | [`17-random-generators`](17-random-generators/README.md) | Random time-series generators |
| 18 | [`18-profiling-and-debugging`](18-profiling-and-debugging/README.md) | Profiling and diagnostics |
| 19 | [`19-common-mistakes`](19-common-mistakes/README.md) | FAQ and failure patterns |
| 20 | [`20-example-catalog-study`](20-example-catalog-study/README.md) | Reading upstream examples concept by concept |
| 21 | [`21-capstone`](21-capstone/README.md) | End-to-end project |

## Official Source Map

- Repository: <https://github.com/Point72/csp>
- Wiki home: <https://github.com/Point72/csp/wiki>
- Examples: <https://github.com/Point72/csp/tree/main/examples>
- Tutorials: Installation, First Steps, More with CSP, Build a Basic App, IO with Adapters
- Concepts: CSP Node, CSP Graph, Historical Buffers, Execution Modes, Adapters, Feedback and Delayed Edge, Common Mistakes
- How-to guides: Use Statistical Nodes, Create Dynamic Baskets, Write Historical Input Adapters, Write Realtime Input Adapters, Write Output Adapters, Profile CSP Code
- API references: Base Nodes, Base Adapters, Basket Nodes, Graph Utilities, Math and Logic Nodes, Statistical Nodes, Functional Methods, Input Output Adapters, Random Time Series Generators, `csp.Struct`, `csp.dynamic`, `csp.profiler`

## Study Cadence

1. Read the linked docs once without coding.
2. Write a short summary in [`notes.md`](notes.md).
3. Implement the practice setup.
4. Run the practice file or produce the requested design artifact.
5. Run `python learning/evaluate_exercises.py <concept-id>` and fix failures.
6. Answer the checkpoint before moving on.
7. Update [`PROGRESS.md`](PROGRESS.md).

The goal is not to memorize every API. The goal is to know where each concept
fits and to build a small local artifact for every major area of CSP.
