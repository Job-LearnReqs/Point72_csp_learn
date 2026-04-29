# 21 Capstone

## Goal

Build a small end-to-end CSP application that uses the concepts from the full
learning path.

## Suggested Files

- `schemas.py`
- `nodes.py`
- `graphs.py`
- `historical_data.csv`
- `run_historical.py`
- `run_realtime_mock.py`
- `README.md`

## Requirements

- Define quote/trade schemas.
- Ingest historical quote events or a documented mock if adapter APIs are too
  version-sensitive.
- Compute spread, midprice, percent spread, rolling statistics, and alert flags.
- Keep calculation nodes independent of input source.
- Include at least one basket or multi-symbol design, even if implemented as a
  stretch goal.
- Include an output boundary, either printed or adapter-backed.
- Include profiling or performance notes.

## Review Checklist

- Inputs are timestamped and typed.
- Nodes use `ts[...]` annotations.
- Nodes check validity where needed.
- Graphs primarily compose nodes.
- Adapters or adapter plans are separated from calculation logic.
- Historical and realtime modes share core graph logic.
- The README explains how to run the app and what concepts it demonstrates.

## Final Checkpoint

You can explain your application in this order:

1. event schema
2. input adapter/source
3. graph wiring
4. node behavior
5. execution mode
6. output adapter/sink
7. profiling or operational risk
