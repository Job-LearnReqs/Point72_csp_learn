# 09 Statistical Nodes

## Read

- <https://github.com/Point72/csp/wiki/Statistical-Nodes-API>
- <https://github.com/Point72/csp/wiki/Use-Statistical-Nodes>
- <https://github.com/Point72/csp/wiki/Historical-Buffers>

## Concepts

- rolling statistics
- count, min, max, mean, and variance-style operations
- windows and horizons
- handling missing or non-overlapping data
- numerical stability and replay testing

## Practice Setup

Create `practice.py` that computes streaming metrics over a price series:

- rolling count
- rolling mean
- rolling min/max
- one volatility-like metric if supported by your installed version

Record in `notes.md` which stats require a window or horizon.

## Checkpoint

You can explain why rolling statistics need time/window semantics instead of a
plain list of all historical values.
