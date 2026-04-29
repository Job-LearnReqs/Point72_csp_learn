from datetime import datetime, timezone

import csp
from csp import ts


@csp.node
def spread(bid: ts[float], ask: ts[float]) -> ts[float]:
    if csp.valid(bid, ask):
        return ask - bid


@csp.node
def midprice(bid: ts[float], ask: ts[float]) -> ts[float]:
    if csp.valid(bid, ask):
        return (bid + ask) / 2.0


@csp.node
def pct_spread(spread_value: ts[float], mid: ts[float]) -> ts[float]:
    if csp.valid(spread_value, mid) and mid != 0:
        return spread_value / mid


@csp.graph
def spread_graph() -> None:
    bid = csp.const(100.25)
    ask = csp.const(100.40)

    spread_value = spread(bid, ask)
    mid = midprice(bid, ask)
    spread_pct = pct_spread(spread_value, mid)

    csp.print("bid", bid)
    csp.print("ask", ask)
    csp.print("spread", spread_value)
    csp.print("mid", mid)
    csp.print("spread_pct", spread_pct)


if __name__ == "__main__":
    csp.run(spread_graph, starttime=datetime.now(timezone.utc))
