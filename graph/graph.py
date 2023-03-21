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
    # A Digraph is a directed graph. The above representation technique is an adjacency list.
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


def printPath(path: List[Node]):
    result = ""
    for node in path:
        result += str(node)
        isLastNode = node == path[-1]
        if not isLastNode:
            result += " -> "
    return result


def DFS(
    graph: Digraph,
    start: Node,
    end: Node,
    path: List[Node],
    shortest: List[Node] | None,
    toPrint=False,
):
    path = path + [start]

    if toPrint:
        print(f"Current DFS path: {printPath(path)}")

    if start == end:
        return path

    for node in graph.childrenOf(start):
        if node not in path:  # Avoid cycles
            # Is it worth exploring next nodes?
            if shortest == None or len(path) < len(shortest):
                # newPath will default to shortest if a better option is not found
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                # if newPath != None: # This check is in the original code before re-assigning shortest, but it's not needed
                shortest = newPath

    return shortest


# TODO: Write a DFS implementation that returns None if no better path is found, rather than current shortest
# The current implementation is a bit confusing


def BFS(graph: Digraph, start: Node, end: Node, toPrint=False):
    initPath: List[Node] = [start]
    pathQueue: List[List[Node]] = [initPath]
    while len(pathQueue) != 0:
        tempPath = pathQueue.pop(0)
        if toPrint:
            print(f"Current BFS path: {printPath(tempPath)}")
        lastNode = tempPath[-1]
        if lastNode == end:
            return tempPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tempPath:
                pathQueue.append(tempPath + [nextNode])
    return None


def testSP():
    # Create the picture graph
    nodes: List[Node] = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for node in nodes:
        g.addNode(node)
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[4], nodes[0]))

    dfs_sp = DFS(g, nodes[0], nodes[5], [], None, True)
    if dfs_sp:
        print(f"DFS solution: {printPath(dfs_sp)}")

    bfs_sp = BFS(g, nodes[0], nodes[5], True)
    if bfs_sp:
        print(f"BFS solution: {printPath(bfs_sp)}")


testSP()
