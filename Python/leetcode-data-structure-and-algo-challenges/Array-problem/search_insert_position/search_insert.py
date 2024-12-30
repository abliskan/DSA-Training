from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Find leftmost position where target exists or should be inserted.
        """
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        return left

import pytest

def test_target_exists():
    solution = Solution()
    nums = [1, 3, 5, 6]
    assert solution.searchInsert(nums, 5) == 2

def test_target_should_be_inserted_middle():
    solution = Solution()
    nums = [1, 3, 5, 6]
    assert solution.searchInsert(nums, 2) == 1

def test_target_should_be_inserted_end():
    solution = Solution()
    nums = [1, 3, 5, 6]
    assert solution.searchInsert(nums, 7) == 4

def test_target_should_be_inserted_start():
    solution = Solution()
    nums = [1, 3, 5, 6]
    assert solution.searchInsert(nums, 0) == 0

def test_empty_array():
    solution = Solution()
    nums = []
    assert solution.searchInsert(nums, 5) == 0

def test_single_element_less():
    solution = Solution()
    nums = [5]
    assert solution.searchInsert(nums, 3) == 0

def test_single_element_more():
    solution = Solution()
    nums = [5]
    assert solution.searchInsert(nums, 7) == 1

def test_single_element_equal():
    solution = Solution()
    nums = [5]
    assert solution.searchInsert(nums, 5) == 0

def test_duplicate_elements():
    solution = Solution()
    nums = [1, 3, 3, 3, 5]
    assert solution.searchInsert(nums, 3) == 1

def test_negative_numbers():
    solution = Solution()
    nums = [-3, -1, 0, 2]
    assert solution.searchInsert(nums, -2) == 1

@pytest.mark.parametrize("nums, target, expected", [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([], 5, 0),
    ([1], 2, 1),
    ([1], 0, 0),
    ([1, 1, 1], 1, 0),
    ([-3, -1, 0, 2], -2, 1)
])
def test_search_insert_parameterized(nums, target, expected):
    solution = Solution()
    assert solution.searchInsert(nums, target) == expected
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 5, 8, 11]
    target = 5
    result = solution.searchInsert(nums, target)
    print(f"Output test-order: {result}")