import copy

import line_profiler
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

@line_profiler.profile
def is_split_group(nodes: dict[str, Node], wire):
    start_node = wire.a
    found = {start_node}
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        for conn in nodes[node].connections:
            if conn == wire.b:
                return False, 0

            if conn not in found:
                found.add(conn)
                queue.append(conn)

    return len(found) != len(nodes), len(found)

def main():
    with open("Day25/day25.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    wires = []
    nodes: dict[str, Node] = {}
    for line in lines:
        start, ends = line.split(': ')
        ends = ends.split()
        for end in ends:
            wires.append(Wire(start, end))

            add_node(start, end, nodes)

    #@util.debug_IO
    def break_connection(wire: Wire):
        nodes[wire.a].connections.remove(wire.b)
        nodes[wire.b].connections.remove(wire.a)

    #@util.debug_IO
    def restore_connection(wire: Wire):
        nodes[wire.a].connections.append(wire.b)
        nodes[wire.b].connections.append(wire.a)

    print(nodes)

    for aindex, wire_a in enumerate(wires):
        break_connection(wire_a)

        for bindex, wire_b in enumerate(wires[aindex+1:]):
            break_connection(wire_b)
            print(aindex * 100 / len(wires), (aindex+bindex+1) * 100 / len(wires))

            for wire_c in wires[bindex+aindex+2:]:
                break_connection(wire_c)
                valid, size = is_split_group(nodes, wire_a)
                restore_connection(wire_c)

                if valid:
                    print(wire_a, wire_b, wire_c)
                    print(size * (len(nodes) - size))
                    #raise Exception("ANSWER")

            restore_connection(wire_b)
        restore_connection(wire_a)
