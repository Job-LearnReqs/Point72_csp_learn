# CSP Revision Log

## Session 2026-05-04 05:09:06 UTC

### 00 Orientation
- Score: 1/2
- Revision: `learning/00-orientation/README.md`
- Prompt:
  What problem is CSP designed to solve, and why is it useful for realtime systems?
- Answer summary:
  CSP is designed to implement graph based programming and handles event streaming where events from the environment or sources are connected to the graph using adapters. It is useful in realtime systems because of its reactive event handling functionality which only evaluates the graph which is impacted by the event that has been modified and not the full graph is reevaluated, so the analysis transformation and update of the analysis on the stream is very quick

## Session 2026-05-05 04:13:54 UTC

### 00 Orientation
- Score: 2/2
- Revision: `learning/00-orientation/README.md`
- Prompt:
  What problem is CSP designed to solve, and why is it useful for realtime systems?
- Answer summary:
  csp is event driven system using graph based programming to cater to streamed system. the same graph can be run with realtime as well as historical data. The realtime data is sourced into the graph using adapters and transformations in the graph are only applied based on what is updated for the time based triggered event allowing for stateful event processing and maintaining runtime state across ticks. results of the transformation are sent to external consumers again using adapters

### 01 Installation and Environment
- Score: 2/2
- Revision: `learning/01-installation-and-environment/README.md`
- Prompt:
  What is the difference between using the installed CSP package and building CSP from source?
- Answer summary:
  installed csp package makes available built csp utilities to create graphs and applications based on csp. building csp from source is to compile and build csp on local machine which allows for enhancement / customisation of the csp platform on local machine.

## Session 2026-05-05 05:24:13 UTC

### 00 Orientation
- Score: 2/2
- Revision: `learning/00-orientation/README.md`
- Prompt:
  What problem is CSP designed to solve, and why is it useful for realtime systems?
- Answer summary:
  CSP models event streams as typed time-series flowing through reusable graphs, with adapters isolating IO so the same logic can run in simulation and realtime.

### 02 First Steps
- Score: 2/2
- Revision: `learning/02-first-steps/README.md`
- Prompt:
  In a minimal CSP program, what roles do `csp.const`, `@csp.graph`, `@csp.node`, and `csp.run` play?
- Answer summary:
  csp.const is a built in node, which when wired in the graph gives a constant value as assigned. @csp.graph designates the function as graph wiring. @csp.node designates runtime node logic that executes when inputs tick. csp.run executes the graph with the provided parameters.

### 01 Installation and Environment
- Score: 2/2
- Revision: `learning/01-installation-and-environment/README.md`
- Prompt:
  What is the difference between using the installed CSP package and building CSP from source?
- Answer summary:
  The installed CSP package is for normal learning and application work. Building from source is mainly for contributing to CSP itself or changing CSP internals.

## Session 2026-05-08 10:11:34 UTC

### 03 Nodes
- Score: 2/2
- Revision: `learning/03-nodes/README.md`
- Prompt:
  Why is `ts[float]` not the same thing as `float`, and why does `csp.valid` matter?
- Answer summary:
  ts[float] is represented of timeseries of float values which can tick and have a sense of time of occurrence of events while 'float' is a single float value that does not change unless explicitly updated. A time series value that has not ticked ever will evaluate for csp.valid as false, so csp.valid is used to check if the ts value has ticked

### 01 Installation and Environment
- Score: 2/2
- Revision: `learning/01-installation-and-environment/README.md`
- Prompt:
  What is the difference between using the installed CSP package and building CSP from source?
- Answer summary:
  I know this and consider Installation and Environment mastered.

### 00 Orientation
- Score: 2/2
- Revision: `learning/00-orientation/README.md`
- Prompt:
  What problem is CSP designed to solve, and why is it useful for realtime systems?
- Answer summary:
  I know this and consider Orientation mastered.

### 02 First Steps
- Score: 2/2
- Revision: `learning/02-first-steps/README.md`
- Prompt:
  In a minimal CSP program, what roles do `csp.const`, `@csp.graph`, `@csp.node`, and `csp.run` play?
- Answer summary:
  I know this and consider First Steps mastered.
