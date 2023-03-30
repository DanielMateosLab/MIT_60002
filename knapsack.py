# Each node is a quadruple of properties:
# - Current items in the backpack
# - Remaining items in the backpack
# - Current weight in BP
# - Remaining size in BP
# The last two properties are just an optimization, as they can always be computed out of the rest of the data.
# Trees like this are often called decision trees, and need not be binary.


import random
from typing import TypeAlias


class Item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        return f"<{self.name}, {self.value}, {self.weight}>"


MaxValResult: TypeAlias = tuple[int, tuple[Item, ...]]


def maxVal(toConsider: list[Item], avail: int) -> MaxValResult:
    if toConsider == [] or avail == 0:
        result: MaxValResult = (0, ())
    elif toConsider[0].getWeight() > avail:
        # Discard left branch, explore right only
        result = maxVal(toConsider[1:], avail)
    else:
        # Explore left branch
        nextItem = toConsider[0]
        withVal, withKnapsack = maxVal(toConsider[1:], avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutKnapsack = maxVal(toConsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withKnapsack + (nextItem,))
        else:
            result = (withoutVal, withoutKnapsack)
    return result


def smallTest():
    names = ["a", "b", "c", "d"]
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    items = []
    for i in range(len(vals)):
        items.append(Item(names[i], vals[i], weights[i]))
    val, taken = maxVal(items, 5)
    for item in taken:
        print(item)
    print("Total value of items taken =", val)


def buildManyItems(numItems: int, maxVal: int, maxWeight: int) -> list[Item]:
    items = []
    for i in range(numItems):
        items.append(
            Item(str(i), random.randint(1, maxVal), random.randint(1, maxWeight))
        )
    return items


def bigTest(numItems):
    random.seed(
        10
    )  # Not true randomness, helps to debug by ensuring same result between tests
    items = buildManyItems(numItems, 10, 10)
    (val, taken) = fastMaxVal(items, 40, {})
    for i in taken:
        print(i)
    print("Total value of taken = ", val)


def fastMaxVal(
    toConsider: list[Item], avail: int, memo: dict[tuple[int, int], MaxValResult]
) -> MaxValResult:
    memoKey = (len(toConsider), avail)
    if memoKey in memo:
        result = memo[memoKey]
    elif toConsider == [] or avail == 0:
        result: MaxValResult = (0, ())
    elif toConsider[0].getWeight() > avail:
        # Discard left branch, explore right only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        # Explore left branch
        nextItem = toConsider[0]
        withVal, withKnapsack = fastMaxVal(
            toConsider[1:], avail - nextItem.getWeight(), memo
        )
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutKnapsack = fastMaxVal(toConsider[1:], avail, memo)
        if withVal > withoutVal:
            result = (withVal, withKnapsack + (nextItem,))
        else:
            result = (withoutVal, withoutKnapsack)
    memo[memoKey] = result
    return result


bigTest(40)
