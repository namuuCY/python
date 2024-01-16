from __future__ import annotations
from typing import Any, Type

Null =  -1

class Node:

    def __init__(self, data = Null, next = Null, dnext = Null):

        self.data = data
        self.next = next
        self.d