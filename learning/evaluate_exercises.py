from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass, field
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Exercise:
    concept_id: str
    concept: str
    artifact: str
    checks: tuple[str, ...]
    run_python: bool = False
    min_chars: int = 120
    required_terms: tuple[str, ...] = ()
    required_any_terms: tuple[tuple[str, ...], ...] = ()
    required_functions: tuple[str, ...] = ()
    required_classes: tuple[str, ...] = ()
    required_decorators: tuple[str, ...] = ()
    required_calls: tuple[str, ...] = ()
    forbidden_terms: tuple[str, ...] = ()

    @property
    def artifact_path(self) -> Path:
        return ROOT / self.artifact


EXERCISES: tuple[Exercise, ...] = (
    Exercise(
        "00",
        "Orientation",
        "00-orientation/summary.md",
        ("Write a summary that explains where CSP fits and why graph reuse matters.",),
        required_terms=("event", "graph", "adapter", "simulation", "realtime"),
    ),
    Exercise(
        "01",
        "Installation and Environment",
        "01-installation-and-environment/environment_check.py",
        ("Create a script that imports csp, prints environment details, and can run locally.",),
        run_python=True,
        required_terms=("csp", "python"),
    ),
    Exercise(
        "02",
        "First Steps",
        "02-first-steps/practice.py",
        ("Build two constants, arithmetic nodes, a graph, printed outputs, and a csp.run entrypoint.",),
        run_python=True,
        required_functions=("add", "subtract", "multiply"),
        required_decorators=("csp.node", "csp.graph"),
        required_calls=("csp.const", "csp.print", "csp.run"),
    ),
    Exercise(
        "03",
        "Nodes",
        "03-nodes/practice.py",
        ("Demonstrate stateless, validity-gated, stateful, and scalar-parameter node patterns.",),
        run_python=True,
        required_decorators=("csp.node", "csp.graph"),
        required_calls=("csp.valid", "csp.run"),
        required_any_terms=(("with csp.state", "csp.state"), ("scalar", "threshold", "factor", "window")),
    ),
    Exercise(
        "04",
        "Graphs",
        "04-graphs/practice.py",
        ("Compose at least two small graphs or graph helpers and keep node logic separate from wiring.",),
        run_python=True,
        required_decorators=("csp.node", "csp.graph"),
        required_calls=("csp.run",),
        required_any_terms=(("compose", "pipeline", "subgraph", "helper"),),
    ),
    Exercise(
        "05",
        "Types, Structs, Data Modeling",
        "05-types-structs-and-data-modeling/practice.py",
        ("Define domain structs, create events, and derive at least one stream from structured data.",),
        run_python=True,
        required_classes=("Quote", "Trade"),
        required_decorators=("csp.node", "csp.graph"),
        required_calls=("csp.run",),
        required_terms=("csp.Struct",),
    ),
    Exercise(
        "06",
        "Execution Modes and Time",
        "06-execution-modes-and-time/practice.py",
        ("Run the same graph with explicit historical start and end times.",),
        run_python=True,
        required_calls=("csp.run",),
        required_terms=("starttime", "endtime"),
        required_any_terms=(("datetime", "timedelta"),),
    ),
    Exercise(
        "07",
        "Base Nodes",
        "07-base-nodes/practice.py",
        ("Demonstrate at least five built-in/base nodes or base-node patterns.",),
        run_python=True,
        required_calls=("csp.run",),
        required_any_terms=(("csp.merge", "csp.filter", "csp.sample", "csp.delay", "csp.count", "csp.flatten"),),
    ),
    Exercise(
        "08",
        "Math, Logic, Functional Methods",
        "08-math-logic-and-functional-methods/practice.py",
        ("Compare built-in math/logic transformations with a named custom domain node.",),
        run_python=True,
        required_decorators=("csp.node", "csp.graph"),
        required_calls=("csp.run",),
        required_any_terms=(("abs", "min", "max", "csp.curve", "csp.apply"), ("spread", "ratio", "threshold")),
    ),
    Exercise(
        "09",
        "Statistical Nodes",
        "09-statistical-nodes/practice.py",
        ("Compute rolling or streaming metrics with explicit window/time semantics.",),
        run_python=True,
        required_calls=("csp.run",),
        required_any_terms=(("mean", "average", "std", "var", "min", "max"), ("window", "timedelta")),
    ),
    Exercise(
        "10",
        "Baskets and Dynamic Graphs",
        "10-baskets-and-dynamic-graphs/design.md",
        ("Design a multi-symbol stream shape and explain why independent streams matter.",),
        required_terms=("basket", "symbol", "stream", "key"),
    ),
    Exercise(
        "11",
        "Historical Buffers and Feedback",
        "11-historical-buffers-and-feedback/practice.py",
        ("Show a delayed dependency or historical lookup that avoids an instantaneous cycle.",),
        run_python=True,
        required_calls=("csp.run",),
        required_any_terms=(("delay", "delayed", "feedback"), ("buffer", "history", "window")),
    ),
    Exercise(
        "12",
        "Adapters Overview and IO",
        "12-adapters-overview-and-io/adapter_plan.md",
        ("Define the IO boundary, adapter responsibilities, and the graph contract.",),
        required_terms=("adapter", "input", "output", "schema", "graph"),
    ),
    Exercise(
        "13",
        "Historical Input Adapters",
        "13-historical-input-adapters/events.csv",
        ("Create deterministic timestamped replay data with at least four rows.",),
        min_chars=60,
        required_terms=("timestamp",),
    ),
    Exercise(
        "14",
        "Realtime Input Adapters",
        "14-realtime-input-adapters/design.md",
        ("Design lifecycle, subscription, threading, shutdown, and error-handling behavior.",),
        required_terms=("connect", "subscribe", "shutdown", "error"),
        required_any_terms=(("thread", "process", "queue", "callback"),),
    ),
    Exercise(
        "15",
        "Output Adapters",
        "15-output-adapters/output_contract.md",
        ("Define output schema, sink semantics, side-effect boundary, and failure handling.",),
        required_terms=("output", "schema", "sink", "failure"),
        required_any_terms=(("publish", "database", "file", "log"),),
    ),
    Exercise(
        "16",
        "Built-In Adapters",
        "16-built-in-adapters/adapter_matrix.md",
        ("Compare candidate built-in adapters against source, sink, schema, and operational fit.",),
        required_terms=("adapter", "source", "sink", "schema"),
        required_any_terms=(("Kafka", "Parquet", "DBReader", "CSV"),),
    ),
    Exercise(
        "17",
        "Random Generators",
        "17-random-generators/practice.py",
        ("Generate a synthetic stream and explain how it supports tests or simulation.",),
        run_python=True,
        required_calls=("csp.run",),
        required_any_terms=(("random", "rand", "normal", "uniform"),),
    ),
    Exercise(
        "18",
        "Profiling and Debugging",
        "18-profiling-and-debugging/profile_notes.md",
        ("Profile or reason about a small graph and separate graph, node, adapter, and output costs.",),
        required_terms=("profile", "node", "adapter", "output"),
        required_any_terms=(("event volume", "latency", "slow", "bottleneck"),),
    ),
    Exercise(
        "19",
        "Common Mistakes",
        "19-common-mistakes/mistake_catalog.md",
        ("Build a catalog of beginner failure modes with symptoms, causes, and fixes.",),
        required_terms=("type", "valid", "graph", "runtime"),
        required_any_terms=(("symptom", "cause", "fix"),),
    ),
    Exercise(
        "20",
        "Example Catalog Study",
        "20-example-catalog-study/example_review_template.md",
        ("Review one upstream example by classifying schemas, nodes, graphs, adapters, and outputs.",),
        required_terms=("schema", "node", "graph", "adapter", "output"),
    ),
    Exercise(
        "21",
        "Capstone",
        "21-capstone/README.md",
        ("Define the capstone scope and explain each end-to-end boundary.",),
        required_terms=("schema", "input", "graph", "node", "output", "run"),
    ),
)


def dotted_names(tree: ast.AST) -> set[str]:
    names: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            names.add(name_for_node(node.func))
        elif isinstance(node, ast.FunctionDef):
            names.add(node.name)
        elif isinstance(node, ast.ClassDef):
            names.add(node.name)
    return {name for name in names if name}


def name_for_node(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = name_for_node(node.value)
        if parent:
            return f"{parent}.{node.attr}"
        return node.attr
    return ""


def decorator_names(node: ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef) -> set[str]:
    return {name_for_node(decorator) for decorator in node.decorator_list}


def load_python(path: Path) -> tuple[ast.Module | None, str | None]:
    try:
        return ast.parse(path.read_text(encoding="utf-8")), None
    except SyntaxError as error:
        return None, f"Python syntax error: {error}"


def run_python(path: Path) -> tuple[bool, str]:
    try:
        completed = subprocess.run(
            [sys.executable, str(path)],
            cwd=ROOT.parent,
            text=True,
            capture_output=True,
            timeout=20,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return False, "Timed out after 20 seconds"

    if completed.returncode == 0:
        return True, "Executed successfully"

    detail = (completed.stderr or completed.stdout).strip().splitlines()
    if detail:
        return False, detail[-1]
    return False, f"Exited with code {completed.returncode}"


def evaluate(exercise: Exercise, execute: bool) -> tuple[bool, list[str]]:
    path = exercise.artifact_path
    results: list[tuple[bool, str]] = []

    results.append((path.exists(), f"artifact exists: {path.relative_to(ROOT.parent)}"))
    if not path.exists():
        return False, [format_result(ok, message) for ok, message in results]

    text = path.read_text(encoding="utf-8")
    lowered = text.lower()
    results.append((len(text.strip()) >= exercise.min_chars, f"artifact has at least {exercise.min_chars} characters"))

    for term in exercise.required_terms:
        results.append((term.lower() in lowered, f"contains `{term}`"))

    for choices in exercise.required_any_terms:
        label = " or ".join(f"`{choice}`" for choice in choices)
        results.append((any(choice.lower() in lowered for choice in choices), f"contains one of {label}"))

    for term in exercise.forbidden_terms:
        results.append((term.lower() not in lowered, f"does not contain `{term}`"))

    tree: ast.Module | None = None
    if path.suffix == ".py":
        tree, error = load_python(path)
        results.append((error is None, "Python parses successfully" if error is None else error))

    if tree is not None:
        functions = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
        classes = {node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)}
        calls = dotted_names(tree)
        decorators = set()
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                decorators.update(decorator_names(node))

        for function in exercise.required_functions:
            results.append((function in functions, f"defines function `{function}`"))
        for class_name in exercise.required_classes:
            results.append((class_name in classes, f"defines class `{class_name}`"))
        for decorator in exercise.required_decorators:
            results.append((decorator in decorators, f"uses decorator `{decorator}`"))
        for call in exercise.required_calls:
            results.append((call in calls, f"calls `{call}`"))

    if execute and exercise.run_python and path.suffix == ".py":
        ok, message = run_python(path)
        results.append((ok, f"runtime check: {message}"))

    passed = all(ok for ok, _ in results)
    return passed, [format_result(ok, message) for ok, message in results]


def format_result(ok: bool, message: str) -> str:
    mark = "PASS" if ok else "FAIL"
    return f"[{mark}] {message}"


def parse_progress_ids() -> set[str]:
    progress = ROOT / "PROGRESS.md"
    if not progress.exists():
        return set()
    pattern = re.compile(r"^\|\s*(\d{2})\s*\|.*?\|\s*(Reading|Practicing|Review|Done)\s*\|")
    return {
        match.group(1)
        for line in progress.read_text(encoding="utf-8").splitlines()
        if (match := pattern.match(line))
    }


def select_exercises(raw: list[str], only_started: bool) -> list[Exercise]:
    by_id = {exercise.concept_id: exercise for exercise in EXERCISES}
    if only_started:
        ids = parse_progress_ids()
        return [exercise for exercise in EXERCISES if exercise.concept_id in ids]
    if not raw:
        return list(EXERCISES)

    selected: list[Exercise] = []
    for value in raw:
        concept_id = value.zfill(2)
        if concept_id not in by_id:
            raise SystemExit(f"Unknown concept id: {value}")
        selected.append(by_id[concept_id])
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate CSP learning exercise artifacts.")
    parser.add_argument("concepts", nargs="*", help="Concept ids to evaluate, for example: 02 03")
    parser.add_argument("--started", action="store_true", help="Evaluate only concepts started in PROGRESS.md")
    parser.add_argument("--no-run", action="store_true", help="Skip executing Python practice files")
    args = parser.parse_args()

    selected = select_exercises(args.concepts, args.started)
    execute = not args.no_run
    failures = 0

    for exercise in selected:
        passed, messages = evaluate(exercise, execute)
        status = "PASS" if passed else "FAIL"
        print(f"\n{exercise.concept_id} {exercise.concept}: {status}")
        print(f"Artifact: learning/{exercise.artifact}")
        for check in exercise.checks:
            print(f"Exercise: {check}")
        for message in messages:
            print(f"  {message}")
        if not passed:
            failures += 1

    print(f"\nEvaluated {len(selected)} exercise(s); {failures} failing.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
