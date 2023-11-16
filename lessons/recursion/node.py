from __future__ import annotations

class Node:

    data: int
    next: Node | None

    def __init__(self, data: int, next: Node | None):
        self.data = data
        self.next = next

    def pretty_list(self) -> str:
        if self.next == None:
            # base case, where recursion ends
            return str(self.data)
        else:    
            return str(self.data) + " -> " + self.next.pretty_list()