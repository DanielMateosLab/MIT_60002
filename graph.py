class Node(object):
    def __init__(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class Edge(object):
    def __init__(self, src: Node, dest: Node) -> None:
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self) -> str:
        return f"{self.src} -> {self.dest}"


class WeightedEdge(Edge):
    def __init__(self, src: Node, dest: Node, weight=1.0) -> None:
        super().__init__(src, dest)
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self) -> str:
        return f"{self.src} ->({self.getWeight()}) {self.dest}"


# print(WeightedEdge(Node("Salamanca"), Node("Málaga"), 600))
