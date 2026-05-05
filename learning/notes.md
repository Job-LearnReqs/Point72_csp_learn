# CSP Notes

Use this file as a working notebook while progressing through the learning path.

## Environment

- CSP version: 0.15.0
- Python version: 3.12.3
- Commands run:
  - `python learning/start_session.py`
  - `python learning/01-installation-and-environment/environment_check.py`
- pandas: 3.0.2
- pyarrow: 23.0.1

## Mental Model

- `ts[T]`: a time series carrying values of type `T` through a CSP graph.
- Node: an event-driven computation that reacts to input ticks and can transform streams.
- Graph: the dependency network that wires adapters, nodes, and outputs together.
- Tick: an input or intermediate update at a specific time that propagates to dependent nodes.
- Valid input:
- Adapter: the boundary that connects external inputs or outputs to CSP time series.

## Phase Notes

### Phase 1

- Orientation checkpoint: CSP is graph-based stream processing for event-driven time-series computation.
- Key reuse idea: the same graph logic can run against historical data in simulation or realtime data in production.
- Installation checkpoint: learning from the installed package means using the current CSP API to build graphs with nodes, adapters, and event streams. Contributing from source means changing CSP's own implementation, build/test setup, docs, examples, or exported building blocks.

### Phase 2

### Phase 3

### Phase 4

### Phase 5

### Phase 6

### Phase 7

## Adapter Contract Draft

- Input event shape:
- Output time series:
- Historical source:
- Realtime source:
- Calculation nodes that stay unchanged:

## Open Questions
