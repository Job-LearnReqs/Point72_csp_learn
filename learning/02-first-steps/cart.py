import csp
from typing import List
from csp import ts
from datetime import timedelta, datetime
from functools import reduce
from copy import copy

class Item(csp.Struct):
    name: str
    cost: float
    qty: int

class Cart(csp.Struct):
    user_id: int
    items: List[Item]

class CartUpdate(csp.Struct):
    item: Item
    add: bool


@csp.node
def update_cart_discounted(event: ts[CartUpdate], discounted: ts[float], user_id: int ) -> csp.Outputs(user=ts[int], total=ts[float], num_items=ts[int], discounted=ts[float] ) :
    """ track with external discount """
    with csp.state():
        s_cart = Cart(user_id=user_id, items=[])
        discount = 1.0
    if csp.ticked(discounted):
        discount = discounted

    if csp.ticked(event):
        if event.add:
            s_cart.items.append(copy(event.item))
            print(f"\t Added {event.item.qty} of {event.item.name} to cart at cost {event.item.cost}")
        else:
            new_items = []
            remaining_qty, update_name  = event.item.qty, event.item.name
            for item in s_cart.items:
                if item.name == update_name:
                    print(f"\t\t\t status of the item:{item} v/s update: {event.item}")
                    if item.qty > remaining_qty:
                        item.qty -= remaining_qty
                        new_items.append(item)
                    else:
                        remaining_qty -= item.qty
                else:
                    new_items.append(item)
                    print(f"\t\t\t status of the item:{item} in {new_items}")
            s_cart.items = new_items
        print(f"\t --> all discounted == items:{s_cart.items}")

    current_total = reduce(lambda a, b: a + b.cost * b.qty * discount, s_cart.items, 0)
    current_num_items = reduce(lambda a, b: a + b.qty, s_cart.items, 0)
    csp.output(user = s_cart.user_id, total=current_total, num_items=current_num_items, discounted=discount)

@csp.node
def update_cart(event: ts[CartUpdate], user_id: int) -> csp.Outputs(total=ts[float], num_items=ts[int]):
    """
    Track of the cart total and number of items.
    """
    with csp.alarms():
        discount = csp.alarm(float)

    with csp.state():
        # create an empty shopping cart
        s_cart = Cart(user_id=user_id, items=[])

    with csp.start():
        csp.make_passive(discount)
        csp.schedule_alarm(discount, timedelta(), 0.9) # 10% off for the first minute
        csp.schedule_alarm(discount, timedelta(minutes=1), 1.0) # full price after!

    if csp.ticked(event):
        if event.add:
            # apply current discount
            event.item.cost *= discount
            s_cart.items.append(copy(event.item))
        else:
            # remove the given qty of the item
            new_items = []
            remaining_qty = event.item.qty
            for item in s_cart.items:
                if item.name == event.item.name:
                    if item.qty > remaining_qty:
                        item.qty -= remaining_qty
                        new_items.append(item)
                    else:
                        remaining_qty -= item.qty
                else:
                    new_items.append(item)
            s_cart.items = new_items
        print(f"\t --> all items:{s_cart.items}")

    current_total = reduce(lambda a, b: a + b.cost * b.qty, s_cart.items, 0)
    current_num_items = reduce(lambda a, b: a + b.qty, s_cart.items, 0)
    csp.output(total=current_total, num_items=current_num_items)

st = datetime(2020, 1, 1)

@csp.graph
def my_graph():
    # Example cart updates
    events = csp.curve(
        CartUpdate,
        [
            # Add 1 unit of X at $10 plus a 10% discount
            (st + timedelta(seconds=15), CartUpdate(item=Item(name="X", cost=10, qty=1), add=True)),
            # Add 2 units of Y at $15 each, plus a 10% discount
            (st + timedelta(seconds=30), CartUpdate(item=Item(name="Y", cost=15, qty=3), add=True)),
            # Remove 1 unit of Y
            (st + timedelta(seconds=45), CartUpdate(item=Item(name="Y", qty=1), add=False)),
            # Add 1 unit of Z at $20 but no discount, since our minute expired
            (st + timedelta(seconds=75), CartUpdate(item=Item(name="Z", cost=20, qty=1), add=True)),
        ],
    )
    # discounts = csp.curve(typ=float, data = [(st, 0.5), (st + timedelta(minutes=1), 1.0)])
    discounts = csp.curve(typ=float, data = [(st + timedelta(minutes=1), 0.5)])

    csp.print("Events", events)

    current_cart = update_cart(events, user_id=42)
    current_cart_discounted = update_cart_discounted(events, discounts, user_id=43)

    csp.print("Cart number of items", current_cart.num_items)
    csp.print("Cart total", current_cart.total)

    csp.print("\t discounted Cart ", current_cart_discounted)


def main():
    csp.run(my_graph, starttime=st)


if __name__ == "__main__":
    main()