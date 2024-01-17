from __future__ import annotations
from typing import Any, Type

class Node:

    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):

        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):

        self.root = None


    def search(self, key: Any) -> Any:

        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key: Any, value: Any) -> bool:

        def add_node(node: Node, key: Any, value: Any) -> None:

            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
