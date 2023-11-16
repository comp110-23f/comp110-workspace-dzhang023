"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Returns head data."""
        return self.data
    
    def tail(self) -> Node | None:
        """Returns tailing list."""
        if self.next is None:
            return None
        else:
            return self.next
    
    def last(self) -> int | Node:
        """Returns last item's data."""
        while self.next is not None:
            return self.next.last()
        return self.data
    

node_c: Node = Node(2, None) # base case
node_b: Node = Node(1, node_c)
node_a: Node = Node(0, node_b) # head of list

print(node_b.last())