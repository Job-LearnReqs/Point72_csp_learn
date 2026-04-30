# Project Instructions

## CSP Learning Workflow

When the user says any of the following:

- "continue learning CSP" with any capitalization
- "continue my CSP learning workflow"
- "continue CSP learning"
- "start my CSP learning session"
- "resume my CSP learning"

Do this immediately:

1. Read `learning/PROGRESS.md`.
2. Read `learning/SESSION_WORKFLOW.md`.
3. Run:

   ```bash
   python learning/start_session.py
   ```

4. If `learning/REVISION_PLAN.md` is generated and contains weak concepts,
   help the user revise those concepts before continuing to new material.
5. If no weak concepts are detected, continue with the next concept in
   `learning/PROGRESS.md`.
6. After the session, update `learning/PROGRESS.md` when the user reports
   completed reading, practice, confidence changes, or checkpoint answers.

Important context:

- The user's goal is to learn all major concepts in `github.com/Point72/csp`.
- The concept-wise curriculum lives in `learning/COMPLETE_CSP_PLAN.md`.
- Progress tracking lives in `learning/PROGRESS.md`.
- Interactive session instructions live in `learning/SESSION_WORKFLOW.md`.
- The revision quiz runner is `learning/start_session.py`.
