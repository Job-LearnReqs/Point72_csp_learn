# 06 Execution Modes And Time

## Read

- <https://github.com/Point72/csp/wiki/Execution-Modes>
- <https://github.com/Point72/csp/wiki/Historical-Buffers>
- <https://github.com/Point72/csp/wiki/Feedback-and-Delayed-Edge>

## Concepts

- simulation mode
- realtime mode
- start time and end time
- event time
- replaying historical data
- deterministic testing

## Practice Setup

Create `practice.py` that runs the same graph with:

- an explicit `starttime`
- an explicit `endtime` if the chosen input source supports it
- a short note printed before each run describing what changed

Use constants first. Revisit this folder after adapter work and replace
constants with historical input.

## Checkpoint

You can explain what should remain unchanged when moving from simulation to
realtime execution.
