# Orientation Summary

## Five Use Cases Where CSP Fits
1. Realtime market data calculations where every new quote or trade should update downstream analytics.
2. Historical replay of timestamped events using the same graph logic intended for live data.
3. Streaming alerting systems where only changed inputs should trigger dependent computations.
4. Pipelines that need external data sources or sinks connected through input and output adapters.
5. Stateful event processing where nodes maintain runtime state across ticks.

## Three use cases where A Batch Script is Simpler
1. One-time transformation of a static CSV with no event-time behavior.
2. A small report that can be computed after all data is already available.
3. Simple exploratory analysis where pandas operations over a fixed table are enough.

## My Explanation of CSP
CSP allows graph-based programming for event-driven computation over time-series data. Inputs enter the graph through adapters, nodes transform tick streams, and outputs leave through adapters. The same graph can be driven by historical data in simulation or by realtime data in production. This is useful because new ticks propagate only to the relevant dependent parts of the graph, so unrelated nodes do not need to be reevaluated.

## Checkpoint

Explain CSP without reducing it to "just a loop" or "just pandas".

CSP is not just a loop because the important model is a graph of time-series dependencies, where ticks propagate through connected nodes according to event time. It is not just pandas because it is built for streaming and realtime workflows, while still allowing the same graph logic to be tested on historical data.

