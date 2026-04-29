# 10 Baskets And Dynamic Graphs

## Read

- <https://github.com/Point72/csp/wiki/Basket-Nodes-API>
- <https://github.com/Point72/csp/wiki/Create-Dynamic-Baskets>
- <https://github.com/Point72/csp/wiki/csp.dynamic-API>

## Concepts

- baskets of time series
- keyed collections of streams
- dynamic graph behavior
- per-symbol or per-entity stream processing
- aggregation across many streams

## Practice Setup

Create `design.md` first:

- define three symbols
- define a quote stream per symbol
- define one per-symbol metric
- define one cross-symbol aggregate

Then create `practice.py` implementing the simplest basket example supported by
your installed CSP version.

## Checkpoint

You can explain why baskets are different from putting a Python list inside one
time-series value.
