# 11 Historical Buffers And Feedback

## Read

- <https://github.com/Point72/csp/wiki/Historical-Buffers>
- <https://github.com/Point72/csp/wiki/Feedback-and-Delayed-Edge>

## Concepts

- retaining prior values
- looking back over stream history
- delayed edges
- feedback loops
- avoiding accidental instantaneous cycles

## Practice Setup

Create `practice.py` with:

- one stream whose current output depends on a prior value
- one rolling or historical lookup behavior
- comments explaining why the dependency is delayed

## Checkpoint

You can explain the difference between a valid delayed feedback edge and an
invalid immediate cycle.
