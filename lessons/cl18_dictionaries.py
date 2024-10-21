"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# add key-value entries using subscription
ice_cream["mint"] = 3

# re-assign values by their key using assign
ice_cream["vanilla"] += 10

# remove items by key using pop method
ice_cream.pop("strawberry")

# test if a key is in the dictionary:
has_pbj: bool = "pbj" in ice_cream

# loop through items using for-in loops
total_orders: int = 0
for flavor in ice_cream:
    # the variable (e.g. flavor) iterates over
    # each key one-by-one in the dictionary
    print(flavor)
    total_orders += ice_cream[flavor]
print(total_orders)


print(ice_cream["pecan"])
