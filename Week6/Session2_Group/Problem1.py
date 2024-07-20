# Problem 1: Detect Circular Linked List
# A circular linked list is a linked list where the tail node points
# at the head node. Given the head of a linked list, write a function
# is_circular() that returns True if the linked list is circular and False otherwise.
#
# Evaluate the time and space complexity of your solution. Define
# your variables and provide a rationale for why you believe your solution
# has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_circular(head):
    current = head
    if current is None:
        return None
    while current:
        if (current.next == head):
            return True
        current = current.next
    return False

node_a = Node(1)
node_b = Node(2)
node_c = Node(3)

node_a.next = node_b
node_b.next = node_c
node_c.next = node_a

print(is_circular(node_a))


