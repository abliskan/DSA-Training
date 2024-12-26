from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from sorted array in-place and return the number of unique elements.
        
        Args:
            nums: A sorted array of integers
            
        Returns:
            The number of unique elements in nums
        """
        if not nums:
            return 0
            
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

import pytest

def test_basic_duplicates():
    """Test basic case with duplicates"""
    solution = Solution()
    nums = [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5]
    k = solution.removeDuplicates(nums)
    
    # Check the length of unique elements
    assert k == 6
    
    # Check if first k elements are correct and sorted
    expected = [0, 1, 2, 3, 4, 5]
    assert nums[:k] == expected

def test_no_duplicates():
    """Test array with no duplicates"""
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    k = solution.removeDuplicates(nums)
    
    assert k == 5
    assert nums[:k] == [1, 2, 3, 4, 5]

def test_all_duplicates():
    """Test array with all identical elements"""
    solution = Solution()
    nums = [1, 1, 1, 1, 1]
    k = solution.removeDuplicates(nums)
    
    assert k == 1
    assert nums[:k] == [1]

def test_empty_array():
    """Test empty array"""
    solution = Solution()
    nums = []
    k = solution.removeDuplicates(nums)
    
    assert k == 0
    assert nums == []

def test_single_element():
    """Test array with single element"""
    solution = Solution()
    nums = [1]
    k = solution.removeDuplicates(nums)
    
    assert k == 1
    assert nums[:k] == [1]

def test_two_elements_duplicate():
    """Test array with two duplicate elements"""
    solution = Solution()
    nums = [1, 1]
    k = solution.removeDuplicates(nums)
    
    assert k == 1
    assert nums[:k] == [1]

def test_two_elements_different():
    """Test array with two different elements"""
    solution = Solution()
    nums = [1, 2]
    k = solution.removeDuplicates(nums)
    
    assert k == 2
    assert nums[:k] == [1, 2]

def test_negative_numbers():
    """Test array with negative numbers"""
    solution = Solution()
    nums = [-3, -3, -2, -1, -1, 0, 0, 0, 2, 2]
    k = solution.removeDuplicates(nums)
    
    assert k == 5
    assert nums[:k] == [-3, -2, -1, 0, 2]

@pytest.mark.parametrize("input_nums, expected_k, expected_nums", [
    ([0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5], 6, [0, 1, 2, 3, 4, 5]),
    ([1, 1, 1], 1, [1]),
    ([1, 2, 3], 3, [1, 2, 3]),
    ([], 0, []),
    ([1], 1, [1])
])
def test_remove_duplicates_parameterized(input_nums, expected_k, expected_nums):
    """Parameterized test covering multiple scenarios"""
    solution = Solution()
    k = solution.removeDuplicates(input_nums)
    
    assert k == expected_k
    assert input_nums[:k] == expected_nums
    
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [-3, -3, -2, -1, -1, 0, 0, 0, 2, 2]
#     result = solution.removeDuplicates(nums)
#     print(f"Output test-negative-numbers: {result}")