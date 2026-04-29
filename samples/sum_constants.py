from datetime import datetime, timezone

import csp
from csp import ts


@csp.node
def add(left: ts[int], right: ts[int]) -> ts[int]:
    if csp.valid(left, right):
        return left + right


@csp.graph
def sum_graph() -> None:
    left = csp.const(3)
    right = csp.const(4)
    total = add(left, right)

    csp.print("left", left)
    csp.print("right", right)
    csp.print("total", total)


if __name__ == "__main__":
    csp.run(sum_graph, starttime=datetime.now(timezone.utc))
