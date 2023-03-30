# Each node is a quadruple of properties:
# - Current items in the backpack
# - Remaining items in the backpack
# - Current weight in BP
# - Remaining size in BP
# The last two properties are just an optimization, as they can always be computed out of the rest of the data.
# Trees like this are often called decision trees, and need not be binary.


from typing import TypeAlias


class Item(object):
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

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
        items.append(Item(names[i], weights[i], vals[i]))
    val, taken = maxVal(items, 5)
    for item in taken:
        print(item)
    print("Total value of items taken =", val)


smallTest()
