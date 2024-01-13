from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:                                                                 #클래스는 설계도
    def __init__(self, key:Any, value:Any, next:Node) -> None:              #인스턴스는 클래스로 정의된 하나의 객체
        self.key=key                                                        #인스턴스는 클래스가 정의한 속성과 메서드를 받는다.
        self.value=value
        self.next=next

class ChainedHash:
    def __init__(self, capacity: int) ->None:
        self.capacity=capacity
        self.table=[None]*self.capacity

    def hash_value(self, key:Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16)% self.capacity)

def search(self, key: Any)-> Any:
    hash=self.hash_value(key)
    p=self.table[hash]

    while p is not None:
        if p.key==key:
            return p.value
        p=p.next
    
    return None

def add(self, key:Any, value:Any)->bool:
    hash=self.hash_value(key)
    p=self.table[hash]

    while p is not None:
        if p.key==key:
            return False
        p=p.next

    temp=Node(key, value, self.table[hash])
    self.table[hash]=temp
    return True