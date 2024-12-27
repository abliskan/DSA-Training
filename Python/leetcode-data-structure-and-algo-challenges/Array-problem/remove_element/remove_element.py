from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all instances of val from nums in-place and return new length.
        
        Args:
            nums: List of integers
            val: Value to remove
            
        Returns:
            Number of elements not equal to val
        """
        k = 0  # Position to place next non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

import pytest

def test_basic_removal():
    """Test basic case with multiple elements to remove"""
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    k = solution.removeElement(nums, val)
    
    assert k == 2  # Should have 2 elements after removal
    assert sorted(nums[:k]) == [2, 2]  # Remaining elements should be 2s

def test_no_elements_to_remove():
    """Test when no elements match the value to remove"""
    solution = Solution()
    nums = [1, 2, 3, 4]
    val = 5
    k = solution.removeElement(nums, val)
    
    assert k == 4
    assert sorted(nums[:k]) == [1, 2, 3, 4]

def test_all_elements_removed():
    """Test when all elements should be removed"""
    solution = Solution()
    nums = [1, 1, 1, 1]
    val = 1
    k = solution.removeElement(nums, val)
    
    assert k == 0
    assert nums[:k] == []

def test_empty_array():
    """Test with empty array"""
    solution = Solution()
    nums = []
    val = 1
    k = solution.removeElement(nums, val)
    
    assert k == 0
    assert nums == []

def test_single_element_removed():
    """Test with single element that matches val"""
    solution = Solution()
    nums = [1]
    val = 1
    k = solution.removeElement(nums, val)
    
    assert k == 0
    assert nums[:k] == []

def test_single_element_kept():
    """Test with single element that doesn't match val"""
    solution = Solution()
    nums = [2]
    val = 1
    k = solution.removeElement(nums, val)
    
    assert k == 1
    assert nums[:k] == [2]

def test_negative_numbers():
    """Test with negative numbers"""
    solution = Solution()
    nums = [-1, -2, -1, -3]
    val = -1
    k = solution.removeElement(nums, val)
    
    assert k == 2
    assert sorted(nums[:k]) == [-3, -2]

def test_zero_value():
    """Test removing zero value"""
    solution = Solution()
    nums = [0, 1, 0, 2, 0, 3]
    val = 0
    k = solution.removeElement(nums, val)
    
    assert k == 3
    assert sorted(nums[:k]) == [1, 2, 3]

@pytest.mark.parametrize("nums, val, expected_k, expected_nums", [
    ([3, 2, 2, 3], 3, 2, [2, 2]),
    ([1, 1, 1], 1, 0, []),
    ([1, 2, 3, 4], 5, 4, [1, 2, 3, 4]),
    ([], 1, 0, []),
    ([1], 1, 0, []),
    ([1], 2, 1, [1])
])
def test_remove_element_parameterized(nums, val, expected_k, expected_nums):
    """Parameterized test covering multiple scenarios"""
    solution = Solution()
    k = solution.removeElement(nums, val)
    
    assert k == expected_k
    assert sorted(nums[:k]) == sorted(expected_nums)
    
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [0, 1, 0, 2, 0, 3]
#     val = 0
#     result = solution.removeElement(nums, val)
#     print(f"Output test-negative-numbers: {result}")