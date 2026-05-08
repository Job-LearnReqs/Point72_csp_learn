from datetime import datetime, timedelta

import csp
from csp import ts


START = datetime(2020, 1, 1)


@csp.node
def double_price(price: ts[float]) -> ts[float]:
    """Stateless node: each output depends only on the current input value."""
    if csp.ticked(price):
        return price * 2.0


@csp.node
def spread_when_valid(bid: ts[float], ask: ts[float]) -> ts[float]:
    """Validity-gated node: do not read both inputs until both have values."""
    if csp.ticked(bid, ask) and csp.valid(bid, ask):
        return ask - bid


@csp.node
def tick_counter(x: ts[float]) -> ts[int]:
    """Stateful node: the count survives across runtime invocations."""
    with csp.state():
        s_count = 0

    if csp.ticked(x):
        s_count += 1
        return s_count


@csp.node
def scale_by_factor(x: ts[float], factor: float) -> ts[float]:
    """Scalar parameter node: factor is fixed graph wiring, x is event data."""
    if csp.ticked(x):
        return x * factor


@csp.graph
def nodes_practice_graph() -> None:
    bid = csp.curve(
        typ=float,
        data=[
            (START, 100.0),
            (START + timedelta(seconds=2), 101.5),
            (START + timedelta(seconds=4), 102.0),
        ],
    )
    ask = csp.curve(
        typ=float,
        data=[
            (START + timedelta(seconds=1), 100.25),
            (START + timedelta(seconds=3), 101.75),
        ],
    )

    doubled_bid = double_price(bid)
    valid_spread = spread_when_valid(bid, ask)
    bid_tick_count = tick_counter(bid)
    scaled_bid = scale_by_factor(bid, factor=1.1)

    csp.print("bid", bid)
    csp.print("ask", ask)
    csp.print("doubled_bid", doubled_bid)
    csp.print("valid_spread", valid_spread)
    csp.print("bid_tick_count", bid_tick_count)
    csp.print("scaled_bid", scaled_bid)


if __name__ == "__main__":
    csp.run(
        nodes_practice_graph,
        starttime=START,
        endtime=START + timedelta(seconds=5),
    )
