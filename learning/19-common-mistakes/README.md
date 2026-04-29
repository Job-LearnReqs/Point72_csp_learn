# 19 Common Mistakes

## Read

- <https://github.com/Point72/csp/wiki/Common-Mistakes>
- <https://github.com/Point72/csp/wiki/Glossary>

## Concepts

- confusing graph build time with runtime
- mixing scalar values and time-series values
- missing `csp.valid` checks
- accidental side effects
- type annotation mistakes
- invalid graph cycles

## Practice Setup

Create `mistake_catalog.md` with:

- mistake
- why it happens
- error symptom
- corrected pattern

Then create `practice.py` with corrected versions only. Keep broken snippets in
markdown, not runnable Python.

## Checkpoint

You can debug a beginner CSP error by first asking whether the issue is type,
time, graph construction, or runtime behavior.
