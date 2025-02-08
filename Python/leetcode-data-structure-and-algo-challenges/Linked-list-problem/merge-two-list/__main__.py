import pytest
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode(0)
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else: 
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        temp.next = list1 or list2
        return dummy.next

@pytest.fixture
def solution():
    return Solution()

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper function to convert a linked list to a regular list for comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_basic_merge(solution):
    # Test case: Basic merge of two sorted lists
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]

def test_empty_lists(solution):
    # Test case: Both lists empty
    assert solution.mergeTwoLists(None, None) is None

def test_one_empty_list(solution):
    # Test cases: One list empty
    list1 = create_linked_list([1, 2, 3])
    assert linked_list_to_list(solution.mergeTwoLists(list1, None)) == [1, 2, 3]
    assert linked_list_to_list(solution.mergeTwoLists(None, list1)) == [1, 2, 3]

def test_lists_with_duplicates(solution):
    # Test case: Lists with duplicate values
    list1 = create_linked_list([1, 2, 2, 4])
    list2 = create_linked_list([2, 3, 4, 4])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 2, 2, 3, 4, 4, 4]

def test_different_length_lists(solution):
    # Test case: Lists of different lengths
    list1 = create_linked_list([1, 2, 3, 4, 5])
    list2 = create_linked_list([6])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]

def test_completely_overlapping_lists(solution):
    # Test case: Lists with same values
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([1, 2, 3])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 1, 2, 2, 3, 3]

def test_single_element_lists(solution):
    # Test case: Single element in each list
    list1 = create_linked_list([1])
    list2 = create_linked_list([2])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 2]

def test_negative_numbers(solution):
    # Test case: Lists with negative numbers
    list1 = create_linked_list([-3, -1, 1])
    list2 = create_linked_list([-2, 0, 2])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [-3, -2, -1, 0, 1, 2]

def test_large_value_difference(solution):
    # Test case: Lists with large value differences
    list1 = create_linked_list([1, 1000, 10000])
    list2 = create_linked_list([2, 2000, 20000])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 1000, 2000, 10000, 20000]

def test_alternating_values(solution):
    # Test case: Values that alternate between lists
    list1 = create_linked_list([1, 3, 5, 7])
    list2 = create_linked_list([2, 4, 6, 8])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6, 7, 8]