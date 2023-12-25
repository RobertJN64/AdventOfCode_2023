import util

class Wire:
    def __init__(self, start, end):
        self.a = start
        self.b = end

    def __repr__(self):
        return f"Wire from {self.a} to {self.b}"

class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)

    def __repr__(self):
        return f"Node {self.name} with {self.connections=}"

def add_node(a: str, b: str, nodes: dict[str, Node]):
    if a not in nodes:
        nodes[a] = Node(a)
    nodes[a].add_connection(b)

    if b not in nodes:
        nodes[b] = Node(b)
    nodes[b].add_connection(a)

def calc_group_size(nodes: dict[str, Node]):
    found = []
    for node in nodes:
        for sublist in found:
            if node in sublist:
                break

        else:
            t_f = [node]
            queue = nodes[node].connections
            while queue:
                node = queue.pop(0)
                if node not in t_f:
                    t_f.append(node)
                    queue.extend(nodes[node].connections)
            found.append(t_f)

    return [len(slist) for slist in found]

def main():
    with open("Day25/day25.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    wires = []
    nodes = {}
    for line in lines:
        start, ends = line.split(': ')
        ends = ends.split()
        for end in ends:
            wires.append(Wire(start, end))

            add_node(start, end, nodes)

    print(nodes)
    print(calc_group_size(nodes))
