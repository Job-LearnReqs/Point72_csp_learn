# 13 Historical Input Adapters

## Read

- <https://github.com/Point72/csp/wiki/Write-Historical-Input-Adapters>
- <https://github.com/Point72/csp/wiki/IO-with-Adapters>
- <https://github.com/Point72/csp/wiki/Input-Output-Adapters-API>

## Concepts

- replayable data
- timestamped events
- deterministic input
- file/database backed streams
- testability

## Practice Setup

Create:

- `events.csv` with timestamp, symbol, bid, and ask columns
- `practice.py` that sketches or implements historical ingestion depending on
  the adapter APIs available in your installed CSP version
- `expected_output.md` describing expected replay results

## Checkpoint

You can explain why historical adapters are the foundation of reproducible tests
for streaming code.
