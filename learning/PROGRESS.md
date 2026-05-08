# CSP Learning Progress

Use this file as the source of truth for your CSP learning progress.

## Status Legend

- `Not Started`: no reading or practice yet
- `Reading`: reading is underway
- `Practicing`: practice artifact is being built
- `Review`: practice is done, checkpoint needs review
- `Done`: checkpoint answered and artifact works

## Confidence Scale

- `0`: I have not studied this yet
- `1`: I recognize the words
- `2`: I can explain the idea after looking at notes
- `3`: I can implement a basic example
- `4`: I can debug common mistakes
- `5`: I can use it in a real CSP design

## Concept Tracker

| # | Concept | Status | Confidence | Evidence | Next Action |
| --- | --- | --- | --- | --- | --- |
| 00 | Orientation | Done | 5 | `learning/00-orientation/summary.md` | Continue to 03 Nodes |
| 01 | Installation and Environment | Done | 5 | `learning/01-installation-and-environment/environment_check.py` | Continue to 03 Nodes |
| 02 | First Steps | Done | 5 | `learning/02-first-steps/practice.py` | Continue to 03 Nodes |
| 03 | Nodes | Review | 3 | `learning/03-nodes/practice.py` | Answer checkpoint: why reading `ts[float]` outside runtime is a category mistake |
| 04 | Graphs | Not Started | 0 | `learning/04-graphs/practice.py` | Compose smaller graphs |
| 05 | Types, Structs, Data Modeling | Not Started | 0 | `learning/05-types-structs-and-data-modeling/practice.py` | Define Quote and Trade structs |
| 06 | Execution Modes and Time | Not Started | 0 | `learning/06-execution-modes-and-time/practice.py` | Run graph with explicit times |
| 07 | Base Nodes | Not Started | 0 | `learning/07-base-nodes/practice.py` | Demonstrate five base nodes |
| 08 | Math, Logic, Functional Methods | Not Started | 0 | `learning/08-math-logic-and-functional-methods/practice.py` | Compare built-ins to custom nodes |
| 09 | Statistical Nodes | Not Started | 0 | `learning/09-statistical-nodes/practice.py` | Compute rolling metrics |
| 10 | Baskets and Dynamic Graphs | Not Started | 0 | `learning/10-baskets-and-dynamic-graphs/design.md` | Design multi-symbol streams |
| 11 | Historical Buffers and Feedback | Not Started | 0 | `learning/11-historical-buffers-and-feedback/practice.py` | Practice delayed dependency |
| 12 | Adapters Overview and IO | Not Started | 0 | `learning/12-adapters-overview-and-io/adapter_plan.md` | Draw IO boundary |
| 13 | Historical Input Adapters | Not Started | 0 | `learning/13-historical-input-adapters/events.csv` | Create replay data |
| 14 | Realtime Input Adapters | Not Started | 0 | `learning/14-realtime-input-adapters/design.md` | Design realtime source lifecycle |
| 15 | Output Adapters | Not Started | 0 | `learning/15-output-adapters/output_contract.md` | Define output contract |
| 16 | Built-In Adapters | Not Started | 0 | `learning/16-built-in-adapters/adapter_matrix.md` | Build adapter matrix |
| 17 | Random Generators | Not Started | 0 | `learning/17-random-generators/practice.py` | Generate synthetic stream |
| 18 | Profiling and Debugging | Not Started | 0 | `learning/18-profiling-and-debugging/profile_notes.md` | Profile a small graph |
| 19 | Common Mistakes | Not Started | 0 | `learning/19-common-mistakes/mistake_catalog.md` | Build mistake catalog |
| 20 | Example Catalog Study | Not Started | 0 | `learning/20-example-catalog-study/example_review_template.md` | Review first upstream example |
| 21 | Capstone | Not Started | 0 | `learning/21-capstone/README.md` | Define capstone scope |

## Weekly Review

Copy this block each week.

```text
## Week Of YYYY-MM-DD

Concepts studied:

Practice completed:

Commands run:

What I can explain now:

What still feels unclear:

Next three actions:
1.
2.
3.
```

## Completion Criteria

A concept is `Done` only when:

- The reading has been completed.
- The requested local artifact exists.
- Any runnable code executes successfully.
- The checkpoint question can be answered without reading the docs.
- Confidence is at least `3`.

The full path is complete when:

- Concepts `00` through `21` are `Done`.
- The capstone has separate schemas, nodes, graphs, input source, output boundary,
  and run instructions.
- You can explain how the same graph logic moves from historical replay to
  realtime execution.
