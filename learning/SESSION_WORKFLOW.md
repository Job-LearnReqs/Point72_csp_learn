# Interactive Learning Session Workflow

Use this workflow each time you launch Codex for CSP study.

## Start Of Session

Run:

```bash
python learning/start_session.py
```

The script:

- reads [`PROGRESS.md`](PROGRESS.md)
- selects concepts already marked `Reading`, `Practicing`, `Review`, or `Done`
- prioritizes low-confidence concepts
- asks a short revision question
- records your answer and self-score in [`REVISION_LOG.md`](REVISION_LOG.md)
- writes weak areas to [`REVISION_PLAN.md`](REVISION_PLAN.md)
- points you to the next practical exercise/evaluator command

## Scoring

- `0`: missed the concept
- `1`: partially remembered it
- `2`: solid answer

Any concept scored below `2` should be revised before starting a new concept.

## Session Loop

1. Run the revision warm-up.
2. Open [`REVISION_PLAN.md`](REVISION_PLAN.md).
3. If weak concepts exist, revise those folders first.
4. Update [`PROGRESS.md`](PROGRESS.md) confidence scores after revision.
5. Continue the next concept in [`COMPLETE_CSP_PLAN.md`](COMPLETE_CSP_PLAN.md).
6. Build the topic artifact from
   [`PRACTICAL_EXERCISES.md`](PRACTICAL_EXERCISES.md).
7. Run `python learning/evaluate_exercises.py <concept-id>` and compare with
   [`SOLUTIONS.md`](SOLUTIONS.md) after your own attempt.
8. End by updating [`PROGRESS.md`](PROGRESS.md) and adding notes to
   [`notes.md`](notes.md).

## Suggested Codex Prompt

Use this prompt at the start of a future session:

```text
Load the CSP learning context from memory. Start an interactive learning
session: run learning/start_session.py, use REVISION_PLAN.md to identify weak
concepts, help me revise those first, then continue the next item in
PROGRESS.md.
```

## Tracking Rule

Do not mark a concept `Done` unless:

- revision score is `2/2`
- confidence is at least `3`
- the evidence artifact exists
- `python learning/evaluate_exercises.py <concept-id>` passes
- the checkpoint answer is clear without reading the docs
