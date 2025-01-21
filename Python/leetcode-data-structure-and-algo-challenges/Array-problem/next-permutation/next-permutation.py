import pytest
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

@pytest.fixture
def solution():
    return Solution()

def test_basic_case(solution):
    nums = [1, 2, 3]
    solution.nextPermutation(nums)
    assert nums == [1, 3, 2]

def test_reverse_case(solution):
    nums = [3, 2, 1]
    solution.nextPermutation(nums)
    assert nums == [1, 2, 3]

def test_same_numbers(solution):
    nums = [1, 1, 5]
    solution.nextPermutation(nums)
    assert nums == [1, 5, 1]

def test_single_element(solution):
    nums = [1]
    solution.nextPermutation(nums)
    assert nums == [1]

def test_two_elements(solution):
    nums = [1, 2]
    solution.nextPermutation(nums)
    assert nums == [2, 1]

def test_duplicate_numbers(solution):
    nums = [1, 1, 2, 2, 3]
    solution.nextPermutation(nums)
    assert nums == [1, 1, 2, 3, 2]

def test_larger_sequence(solution):
    nums = [1, 2, 3, 4, 5]
    solution.nextPermutation(nums)
    assert nums == [1, 2, 3, 5, 4]

def test_descending_sequence(solution):
    nums = [5, 4, 3, 2, 1]
    solution.nextPermutation(nums)
    assert nums == [1, 2, 3, 4, 5]

def test_partial_ascending(solution):
    nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
    solution.nextPermutation(nums)
    assert nums == [1, 5, 8, 5, 1, 3, 4, 6, 7]