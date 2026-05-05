from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import random
import re
import textwrap


ROOT = Path(__file__).resolve().parent
PROGRESS = ROOT / "PROGRESS.md"
REVISION_LOG = ROOT / "REVISION_LOG.md"
REVISION_PLAN = ROOT / "REVISION_PLAN.md"
EXERCISES = ROOT / "PRACTICAL_EXERCISES.md"


@dataclass(frozen=True)
class Question:
    concept_id: str
    concept: str
    prompt: str
    expected: str
    revision_path: str


QUESTIONS = [
    Question(
        "00",
        "Orientation",
        "What problem is CSP designed to solve, and why is it useful for realtime systems?",
        "Mention event streams, graph-based computation, simulation/realtime reuse, and adapters.",
        "learning/00-orientation/README.md",
    ),
    Question(
        "01",
        "Installation and Environment",
        "What is the difference between using the installed CSP package and building CSP from source?",
        "Installed package is for learning/application work; source build is for contributing or changing CSP internals.",
        "learning/01-installation-and-environment/README.md",
    ),
    Question(
        "02",
        "First Steps",
        "In a minimal CSP program, what roles do `csp.const`, `@csp.graph`, `@csp.node`, and `csp.run` play?",
        "Constants create streams, graph wires streams, nodes compute at runtime, run executes the graph over time.",
        "learning/02-first-steps/README.md",
    ),
    Question(
        "03",
        "Nodes",
        "Why is `ts[float]` not the same thing as `float`, and why does `csp.valid` matter?",
        "`ts[float]` is a time-series value; validity checks prevent using inputs before they have runtime values.",
        "learning/03-nodes/README.md",
    ),
    Question(
        "04",
        "Graphs",
        "What belongs in a graph function versus a node function?",
        "Graphs wire streams and compose nodes; nodes contain event-time calculation logic.",
        "learning/04-graphs/README.md",
    ),
    Question(
        "05",
        "Types, Structs, Data Modeling",
        "When would you model an event as a `csp.Struct` instead of separate primitive streams?",
        "Use structs when fields belong to one event/schema and should move through adapters together.",
        "learning/05-types-structs-and-data-modeling/README.md",
    ),
    Question(
        "06",
        "Execution Modes and Time",
        "What should stay unchanged when moving from historical simulation to realtime execution?",
        "Core schemas, graph wiring, and calculation nodes should stay unchanged; adapters and run mode change.",
        "learning/06-execution-modes-and-time/README.md",
    ),
    Question(
        "07",
        "Base Nodes",
        "Why should you check built-in base nodes before writing a custom node?",
        "Built-ins are clearer, tested, and often optimized for common stream operations.",
        "learning/07-base-nodes/README.md",
    ),
    Question(
        "08",
        "Math, Logic, Functional Methods",
        "When is a math/logic built-in better than a custom domain node?",
        "Use built-ins for generic transformations; use custom nodes when the domain name/formula improves intent.",
        "learning/08-math-logic-and-functional-methods/README.md",
    ),
    Question(
        "09",
        "Statistical Nodes",
        "Why do rolling statistics require explicit time/window semantics?",
        "Streaming stats need bounded historical context and deterministic behavior over event time.",
        "learning/09-statistical-nodes/README.md",
    ),
    Question(
        "10",
        "Baskets and Dynamic Graphs",
        "How is a basket of streams different from a single stream containing a Python list?",
        "A basket preserves independent streams per key/entity; a list is one value ticking as a whole.",
        "learning/10-baskets-and-dynamic-graphs/README.md",
    ),
    Question(
        "11",
        "Historical Buffers and Feedback",
        "What makes delayed feedback valid while immediate feedback can be invalid?",
        "Delayed feedback depends on a prior value/tick; immediate feedback creates an instantaneous cycle.",
        "learning/11-historical-buffers-and-feedback/README.md",
    ),
    Question(
        "12",
        "Adapters Overview and IO",
        "Where should external IO live in a CSP application?",
        "At adapter boundaries; core graph and calculation nodes should stay infrastructure-independent.",
        "learning/12-adapters-overview-and-io/README.md",
    ),
    Question(
        "13",
        "Historical Input Adapters",
        "Why are historical adapters important for testing streaming code?",
        "They provide timestamped, deterministic replay input for reproducible tests.",
        "learning/13-historical-input-adapters/README.md",
    ),
    Question(
        "14",
        "Realtime Input Adapters",
        "What extra concerns appear in realtime adapters compared with historical adapters?",
        "Connection lifecycle, live subscriptions, wall-clock behavior, threading/process boundaries, and shutdown.",
        "learning/14-realtime-input-adapters/README.md",
    ),
    Question(
        "15",
        "Output Adapters",
        "Why should publishing or database writes usually not live inside calculation nodes?",
        "They are side effects and should be isolated at output boundaries for testability and reliability.",
        "learning/15-output-adapters/README.md",
    ),
    Question(
        "16",
        "Built-In Adapters",
        "How do you decide between a built-in adapter and a custom adapter?",
        "Use built-ins when source/sink and schema fit; write custom adapters for unsupported systems or semantics.",
        "learning/16-built-in-adapters/README.md",
    ),
    Question(
        "17",
        "Random Generators",
        "When are synthetic random streams useful?",
        "For simulation, load testing, behavior checks, and prototyping when real historical data is unavailable.",
        "learning/17-random-generators/README.md",
    ),
    Question(
        "18",
        "Profiling and Debugging",
        "What are the main causes to separate when diagnosing a slow CSP graph?",
        "Event volume, node logic, adapter IO, output side effects, and graph structure.",
        "learning/18-profiling-and-debugging/README.md",
    ),
    Question(
        "19",
        "Common Mistakes",
        "What four categories should you check first when debugging a beginner CSP error?",
        "Type mistakes, time/validity mistakes, graph construction mistakes, and runtime behavior mistakes.",
        "learning/19-common-mistakes/README.md",
    ),
    Question(
        "20",
        "Example Catalog Study",
        "How should you read an unfamiliar upstream CSP example?",
        "Classify schemas, inputs, adapters, nodes, graphs, execution mode, and outputs.",
        "learning/20-example-catalog-study/README.md",
    ),
    Question(
        "21",
        "Capstone",
        "What parts should an end-to-end CSP application be able to explain separately?",
        "Schema, input source/adapter, graph wiring, node behavior, execution mode, output sink, and profiling risk.",
        "learning/21-capstone/README.md",
    ),
]


def parse_progress() -> dict[str, tuple[str, int]]:
    if not PROGRESS.exists():
        return {}

    rows: dict[str, tuple[str, int]] = {}
    pattern = re.compile(r"^\|\s*(\d{2})\s*\|.*?\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|")
    for line in PROGRESS.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if not match:
            continue
        concept_id, status, confidence = match.groups()
        rows[concept_id] = (status.strip(), int(confidence))
    return rows


def next_concept(progress: dict[str, tuple[str, int]]) -> Question | None:
    active_statuses = {"Not Started", "Reading", "Practicing", "Review"}
    for question in QUESTIONS:
        status, _ = progress.get(question.concept_id, ("Not Started", 0))
        if status in active_statuses:
            return question
    return None


def choose_questions(progress: dict[str, tuple[str, int]], max_questions: int = 5) -> list[Question]:
    covered_statuses = {"Reading", "Practicing", "Review", "Done"}
    weak_ids = {
        concept_id
        for concept_id, (status, confidence) in progress.items()
        if status in covered_statuses and confidence <= 2
    }
    covered_ids = {
        concept_id
        for concept_id, (status, confidence) in progress.items()
        if status in covered_statuses or confidence > 0
    }

    weak = [q for q in QUESTIONS if q.concept_id in weak_ids]
    covered = [q for q in QUESTIONS if q.concept_id in covered_ids and q.concept_id not in weak_ids]

    random.shuffle(weak)
    random.shuffle(covered)
    selected = (weak + covered)[:max_questions]
    return selected


def append_revision_log(entries: list[tuple[Question, int, str]]) -> None:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [f"\n## Session {timestamp}\n"]
    for question, score, answer in entries:
        lines.append(f"### {question.concept_id} {question.concept}")
        lines.append(f"- Score: {score}/2")
        lines.append(f"- Revision: `{question.revision_path}`")
        lines.append("- Prompt:")
        lines.append(f"  {question.prompt}")
        lines.append("- Answer summary:")
        lines.append("  " + answer.strip().replace("\n", "\n  "))
        lines.append("")

    if not REVISION_LOG.exists():
        REVISION_LOG.write_text("# CSP Revision Log\n", encoding="utf-8")
    with REVISION_LOG.open("a", encoding="utf-8") as file:
        file.write("\n".join(lines))


def write_revision_plan(entries: list[tuple[Question, int, str]]) -> None:
    weak = [(q, score) for q, score, _ in entries if score < 2]
    if not weak:
        body = textwrap.dedent(
            """\
            # CSP Revision Plan

            No weak concepts were detected in the latest session.

            Next session:

            - Continue with the next `Not Started` or `Reading` concept in `PROGRESS.md`.
            - Keep one older concept in the warm-up quiz.
            """
        )
    else:
        lines = [
            "# CSP Revision Plan",
            "",
            "Weak concepts from the latest session:",
            "",
        ]
        for question, score in weak:
            lines.extend(
                [
                    f"- `{question.concept_id}` {question.concept}: scored {score}/2",
                    f"  - Review: `{question.revision_path}`",
                    f"  - Re-practice: answer the checkpoint in that folder before new study",
                ]
            )
        lines.extend(
            [
                "",
                "Suggested next session order:",
                "",
                "1. Spend 10 minutes revising the weak concepts above.",
                "2. Re-run or create the evidence artifact for each weak concept.",
                "3. Continue with the next concept in `PROGRESS.md` only after weak scores are 2/2.",
            ]
        )
        body = "\n".join(lines) + "\n"

    REVISION_PLAN.write_text(body, encoding="utf-8")


def main() -> None:
    progress = parse_progress()
    questions = choose_questions(progress)

    if not questions:
        print("No covered concepts found in PROGRESS.md yet.")
        print("Start with learning/00-orientation, then mark it Reading or Practicing.")
        return

    print("CSP revision warm-up")
    print("Answer briefly. After seeing the expected points, self-score:")
    print("0 = missed, 1 = partial, 2 = solid\n")

    entries: list[tuple[Question, int, str]] = []
    for index, question in enumerate(questions, start=1):
        print(f"[{index}/{len(questions)}] {question.concept_id} {question.concept}")
        print(question.prompt)
        answer = input("\nYour answer: ").strip()
        print("\nExpected points:")
        print(textwrap.fill(question.expected, width=88))
        while True:
            raw_score = input("Score yourself 0, 1, or 2: ").strip()
            if raw_score in {"0", "1", "2"}:
                score = int(raw_score)
                break
            print("Enter 0, 1, or 2.")
        entries.append((question, score, answer))
        print("")

    append_revision_log(entries)
    write_revision_plan(entries)

    weak_count = sum(1 for _, score, _ in entries if score < 2)
    print(f"Recorded session in {REVISION_LOG.relative_to(ROOT.parent)}")
    print(f"Updated revision plan in {REVISION_PLAN.relative_to(ROOT.parent)}")
    if weak_count:
        print(f"{weak_count} weak concept(s) need revision before new study.")
    else:
        print("No weak concepts detected. Continue to the next concept in PROGRESS.md.")

    upcoming = next_concept(progress)
    if upcoming:
        print("")
        print(f"Next practical exercise: {upcoming.concept_id} {upcoming.concept}")
        print(f"Read: {EXERCISES.relative_to(ROOT.parent)}")
        print(f"Evaluate with: python learning/evaluate_exercises.py {upcoming.concept_id}")


if __name__ == "__main__":
    main()
