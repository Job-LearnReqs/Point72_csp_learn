from datetime import datetime, timezone

import csp
from csp import ts


@csp.node
def add(left: ts[int], right: ts[int]) -> ts[int]:
    if csp.valid(left, right):
        return left + right


@csp.node
def subtract(left: ts[int], right: ts[int]) -> ts[int]:
    if csp.valid(left, right):
        return left - right


@csp.node
def multiply(left: ts[int], right: ts[int]) -> ts[int]:
    if csp.valid(left, right):
        return left * right


@csp.graph
def arithmetic_graph() -> None:
    left = csp.const(8)
    right = csp.const(3)

    total = add(left, right)
    difference = subtract(left, right)
    product = multiply(left, right)

    csp.print("left", left)
    csp.print("right", right)
    csp.print("total", total)
    csp.print("difference", difference)
    csp.print("product", product)


if __name__ == "__main__":
    csp.run(arithmetic_graph, starttime=datetime.now(timezone.utc))
