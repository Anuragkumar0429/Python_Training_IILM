"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        # Pointer to traverse the list
        curr = head
        
        while curr:
            # Case: Node has a child list
            if curr.child:
                # Store the next node to reconnect later
                next_node = curr.next
                
                # 1. Recursively flatten the child list
                child_head = self.flatten(curr.child)
                
                # 2. Connect current node to the child head
                curr.next = child_head
                child_head.prev = curr
                
                # 3. Find the tail of the flattened child list
                child_tail = child_head
                while child_tail.next:
                    child_tail = child_tail.next
                
                # 4. Connect the child tail to the original next_node
                if next_node:
                    child_tail.next = next_node
                    next_node.prev = child_tail
                
                # 5. Crucial: Set the child pointer to null
                curr.child = None
            
            # Move to the next node (which might be the head of the child list we just linked)
            curr = curr.next
            
        return head