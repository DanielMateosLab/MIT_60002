from typing import Dict, List


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


class Digraph(object):
    # A Digraph is a directed graph
    # nodes is a list of all the nodes in the digraph
    nodes: List[Node] = []
    # edges is a dictionary mapping each node to a list of its children
    edges: Dict[Node, List[Node]] = {}

    def addNode(self, node: Node):
        if node in self.nodes:
            raise ValueError("Node already in graph")
        self.nodes.append(node)
        self.edges[node] = []

    def addEdge(self, edge: Edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self) -> str:
        result = ""
        for src in self.nodes:
            for dest in self.edges[src]:
                result + f"{src} -> {dest}\n"
        return result[:-1]


class Graph(Digraph):
    def addEdge(self, edge: Edge):
        super().addEdge(edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        super().addEdge(rev)


# TODO: Test Digraph and Graph
