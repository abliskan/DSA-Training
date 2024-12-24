from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the list that add up to the target.
        Returns their indices.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        curr_idx = {}
        for i, num in enumerate(nums):
            if target - num in curr_idx:
                return [curr_idx[target - num], i]
            curr_idx[num] = i
        return []

import pytest

def test_two_sum_basic_scenario():
    """Test the basic scenario from the problem statement"""
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    assert result == [0, 1], f"Expected [0, 1], but got {result}"

def test_two_sum_multiple_solutions():
    """Test a list where multiple pairs could be a solution"""
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    assert result == [1, 2], f"Expected [1, 2], but got {result}"

def test_two_sum_same_elements():
    """Test a list with same elements used twice"""
    solution = Solution()
    nums = [3, 3]
    target = 6
    result = solution.twoSum(nums, target)
    assert result == [0, 1], f"Expected [0, 1], but got {result}"

def test_two_sum_no_solution():
    """Test a scenario where no solution exists"""
    solution = Solution()
    nums = [1, 2, 3, 4]
    target = 10
    result = solution.twoSum(nums, target)
    assert result == [], f"Expected [], but got {result}"

def test_two_sum_large_numbers():
    """Test with larger numbers"""
    solution = Solution()
    nums = [230, 863, 916, 585, 981, 404, 316, 785, 88, 12, 70, 435, 384, 778, 887, 755, 740, 337, 86, 92, 325, 422, 815, 650, 920, 125, 277, 336, 221, 847, 168, 23, 677, 61, 400, 136, 874, 363, 394, 199, 863, 997, 794, 587, 124, 321, 212, 957, 764, 173, 314, 422, 927, 783, 930, 282, 306, 506, 44, 926, 691, 568, 68, 730, 933, 737, 531, 180, 414, 751, 28, 546, 60, 371, 493, 370, 527, 387, 43, 541, 13, 457, 328, 227, 652, 365, 430, 803, 59, 858, 538, 427, 583, 368, 375, 173, 809, 896, 370, 789]
    target = 542
    result = solution.twoSum(nums, target)
    assert result is not None, "No solution found"
    assert nums[result[0]] + nums[result[1]] == target, "Solution does not sum to target"

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),  # Basic scenario
    ([3, 2, 4], 6, [1, 2]),        # Multiple solutions
    ([3, 3], 6, [0, 1]),           # Same elements
    ([1, 2, 3, 4], 10, [])         # No solution
])
def test_two_sum_parameterized(nums, target, expected):
    """Parameterized test covering multiple scenarios"""
    solution = Solution()
    result = solution.twoSum(nums, target)
    assert result == expected, f"For nums={nums}, target={target}, expected {expected}, but got {result}"

def test_two_sum_solution_indices_are_different():
    """Ensure the returned indices are different"""
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    assert len(result) == 2, "Should return two indices"
    assert result[0] != result[1], "Indices should be different"

def test_two_sum_solution_order():
    """
    Verify that the solution always returns indices in ascending order
    This is important because the problem typically requires sorted indices
    """
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    assert result == sorted(result), "Indices should be in ascending order"

# Run the code using command:$ pytest two_sum_with_test.py / coverage run -m pytest
# Run the code to generates the coverage report: coverage report -m

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    print(f"Output test-order: {result}")