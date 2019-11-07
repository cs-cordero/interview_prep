from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


class DisjointSet:
    def __init__(self, data: List[Vertex]) -> None:
        self.index_mapping = {vertex: index for index, vertex in enumerate(data)}
        self.reverse_mapping = data[:]
        self.parent_ids = list(range(len(data)))
        self.ranks = [0] * len(data)

    def union(self, a: Vertex, b: Vertex) -> bool:
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a == parent_b:
            return False

        parent_a_index = self.index_mapping[parent_a]
        parent_b_index = self.index_mapping[parent_b]
        parent_a_rank = self.ranks[parent_a_index]
        parent_b_rank = self.ranks[parent_b_index]

        if parent_a_rank > parent_b_rank:
            self.parent_ids[parent_b_index] = parent_a_index
        elif parent_a_rank < parent_b_rank:
            self.parent_ids[parent_a_index] = parent_b_index
        else:
            self.parent_ids[parent_b_index] = parent_a_index
            self.ranks[parent_a_index] += 1
        return True

    def find(self, node: Vertex) -> Vertex:
        node_index = self.index_mapping[node]
        parent_index = self.parent_ids[node_index]
        if parent_index != node_index:
            self.parent_ids[node_index] = self.index_mapping[
                self.find(self.reverse_mapping[parent_index])
            ]
        return self.reverse_mapping[self.parent_ids[node_index]]


@dataclass(unsafe_hash=True)
class Vertex:
    name: str

    def __repr__(self) -> str:
        return f"Vertex({self.name})"


nodes = [Vertex(chr(97 + i)) for i in range(12)]
a, b, c, d, e, f, g, h, i, j, k, l = nodes

disjoint_set = DisjointSet(nodes)
disjoint_set.union(c, k)
disjoint_set.union(f, e)
disjoint_set.union(a, j)
disjoint_set.union(a, b)
disjoint_set.union(c, d)
disjoint_set.union(d, i)
disjoint_set.union(l, f)
disjoint_set.union(c, a)
disjoint_set.union(a, b)
disjoint_set.union(h, g)
disjoint_set.union(h, f)
disjoint_set.union(h, b)
for node in nodes:
    if disjoint_set.find(node) != h:
        raise Exception(f"{node}'s parent is not {h}. It is {disjoint_set.find(node)}")
