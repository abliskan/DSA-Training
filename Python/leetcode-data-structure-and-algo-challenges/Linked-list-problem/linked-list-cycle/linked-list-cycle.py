# Solotion type 1: Two-ponter / Floyd’s Cycle-Finding Algorithm technique
import pytest
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer, fast_pointer = head, head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next 
            fast_pointer = fast_pointer.next.next
            if fast_pointer == slow_pointer:
                return True
        return False

@pytest.fixture
def solution():
    return Solution()

def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    
    # Create nodes
    nodes = [ListNode(val) for val in values]
    
    # Link nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create cycle if pos is valid
    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
    
    return nodes[0]

def test_no_cycle(solution):
    # Test case: 1->2->3->4->5->NULL
    head = create_linked_list_with_cycle([1, 2, 3, 4, 5], -1)
    assert solution.hasCycle(head) == False

def test_cycle_at_beginning(solution):
    # Test case: 1->2->3->4->5->1 (cycle back to beginning)
    head = create_linked_list_with_cycle([1, 2, 3, 4, 5], 0)
    assert solution.hasCycle(head) == True

def test_cycle_in_middle(solution):
    # Test case: 1->2->3->4->5->3 (cycle to position 2)
    head = create_linked_list_with_cycle([1, 2, 3, 4, 5], 2)
    assert solution.hasCycle(head) == True

def test_empty_list(solution):
    # Test case: NULL
    head = None
    assert solution.hasCycle(head) == False

def test_single_node_no_cycle(solution):
    # Test case: 1->NULL
    head = create_linked_list_with_cycle([1], -1)
    assert solution.hasCycle(head) == False

def test_single_node_with_cycle(solution):
    # Test case: 1->1 (self-cycle)
    head = create_linked_list_with_cycle([1], 0)
    assert solution.hasCycle(head) == True

def test_two_nodes_with_cycle(solution):
    # Test case: 1->2->1
    head = create_linked_list_with_cycle([1, 2], 0)
    assert solution.hasCycle(head) == True

def test_long_list_with_cycle_to_end(solution):
    # Test case: 1->2->3->4->5->6->7->8->9->10->5
    head = create_linked_list_with_cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
    assert solution.hasCycle(head) == True
    
# Solution type 2: Hash table
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        curr_node = head
        while curr_node is not None:
            if curr_node in nodes:
                return True
            nodes.add(curr_node)
            curr_node = curr_node.next
        return False