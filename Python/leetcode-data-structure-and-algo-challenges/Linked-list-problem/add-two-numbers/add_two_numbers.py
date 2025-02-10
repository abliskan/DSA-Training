from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
        return dummy.next

def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Helper function to create a linked list from an array"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head: Optional[ListNode]) -> List[int]:
    """Helper function to convert a linked list to an array"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_add_two_numbers_basic():
    solution = Solution()
    
    # Test case 1: Basic addition
    l1 = create_linked_list([2, 4, 3])  # 342
    l2 = create_linked_list([5, 6, 4])  # 465
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [7, 0, 8]  # 807

def test_add_two_numbers_different_lengths():
    solution = Solution()
    
    # Test case 2: Different length numbers
    l1 = create_linked_list([9, 9, 9, 9])  # 9999
    l2 = create_linked_list([9, 9])        # 99
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [8, 9, 0, 0, 1]  # 10098

def test_add_two_numbers_with_zero():
    solution = Solution()
    
    # Test case 3: Adding with zero
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [0]

def test_add_two_numbers_large_carry():
    solution = Solution()
    
    # Test case 4: Large numbers with multiple carries
    l1 = create_linked_list([9, 9, 9])     # 999
    l2 = create_linked_list([9, 9, 9, 9])  # 9999
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [8, 9, 9, 0, 1]  # 10998

def test_add_two_numbers_empty_list():
    solution = Solution()
    
    # Test case 5: One empty list
    l1 = create_linked_list([1, 2, 3])
    l2 = None
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [1, 2, 3]