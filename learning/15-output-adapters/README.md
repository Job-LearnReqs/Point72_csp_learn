# 15 Output Adapters

## Read

- <https://github.com/Point72/csp/wiki/Write-Output-Adapters>
- <https://github.com/Point72/csp/wiki/IO-with-Adapters>
- <https://github.com/Point72/csp/wiki/Base-Adapters-API>

## Concepts

- sinks
- publishing derived values
- side effects outside core calculation nodes
- output schema design
- separating computation from persistence

## Practice Setup

Create `practice.py` with:

- a graph that computes quote metrics
- one printed output
- one planned output adapter boundary documented in comments

Create `output_contract.md` with output event fields, destination, delivery
expectations, and failure behavior.

## Checkpoint

You can explain why database writes or message publishes should not be buried in
ordinary calculation nodes.
