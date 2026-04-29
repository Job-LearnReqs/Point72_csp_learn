# 16 Built In Adapters

## Read

- <https://github.com/Point72/csp/wiki/Input-Output-Adapters-API>
- <https://github.com/Point72/csp/wiki/IO-with-Adapters>
- <https://github.com/Point72/csp/tree/main/examples>

## Concepts

- Parquet adapter
- Kafka adapter
- DBReader style integration
- tabular data integration
- schema compatibility
- dependency-sensitive examples

## Practice Setup

Create `adapter_matrix.md` with columns:

- adapter
- input or output
- dependency
- expected event type
- local practice idea
- production use case

If pyarrow is available, create a small Parquet read/write experiment. If not,
document the missing dependency and continue.

## Checkpoint

You can choose between writing a custom adapter and using a built-in adapter.
