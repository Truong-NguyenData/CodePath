# Problem 2: Find Last Node in a Linked List Cycle
# Given the head of a singly linked list, write a function
# that returns the last node in the cycle. If there is no cycle in the linked list, return None.
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next
def find_last_node_in_cycle(head):
    current = head
    lst = []
    if current is None:
        return None
    while current.next not in lst:
        lst.append(current)
        current = current.next
    return current.value


# 1 -> 2 -> 3 -> 4->2
node_d = Node(1)
node_e = Node(2)
node_f = Node(3)
node_g = Node(4)
node_d.next = node_e
node_e.next = node_f
node_f.next = node_g
node_g.next = node_e

print(find_last_node_in_cycle(node_d))