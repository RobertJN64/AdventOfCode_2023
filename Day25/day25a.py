import copy

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

def break_connection(wire: Wire, nodes: dict[str, Node]):
    nodes[wire.a].connections.remove(wire.b)
    nodes[wire.b].connections.remove(wire.a)

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

    for aindex, wire_a in enumerate(wires):
        print(aindex * 100 / len(wires))
        for bindex, wire_b in enumerate(wires[aindex+1:]):
            for wire_c in wires[bindex+aindex+2:]:
                t_nodes = copy.deepcopy(nodes)
                break_connection(wire_a, t_nodes)
                break_connection(wire_b, t_nodes)
                break_connection(wire_c, t_nodes)
                cgs = calc_group_size(t_nodes)
                if len(cgs) == 2:
                    print(cgs, wire_a, wire_b, wire_c)
                    print(cgs[0] * cgs[1])
                    raise Exception("ANSWER")

                #
                # print(wire_a, wire_b, wire_c)

    # print(wires)
    # print(nodes)
    # print(calc_group_size(nodes))
