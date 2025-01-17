from typing import List
import pytest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

class TestContainerWithMostWater:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize("heights,expected", [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),  # Standard example
        ([1, 1], 1),                         # Minimum valid input
        ([4, 3, 2, 1, 4], 16),              # Equal height at ends
        ([1, 2, 4, 3], 4),                  # Increasing then decreasing
        ([7, 1, 2, 3, 9], 28),              # Highest at ends
        ([2, 3, 4, 5, 18, 17, 6], 17),      # Peak in middle
    ])
    def test_common_cases(self, heights, expected):
        assert self.solution.maxArea(heights) == expected

    def test_empty_or_single(self):
        # Empty list should return 0
        assert self.solution.maxArea([]) == 0
        # Single element can't form container
        assert self.solution.maxArea([5]) == 0

    def test_same_heights(self):
        # All same heights
        assert self.solution.maxArea([4, 4, 4, 4]) == 12
        # Multiple pairs of same height
        assert self.solution.maxArea([1, 1, 1, 1, 1]) == 4

    def test_increasing_decreasing(self):
        # Strictly increasing
        assert self.solution.maxArea([1, 2, 3, 4, 5]) == 6
        # Strictly decreasing
        assert self.solution.maxArea([5, 4, 3, 2, 1]) == 6
        # Mountain shape
        assert self.solution.maxArea([1, 3, 5, 3, 1]) == 6

    def test_large_numbers(self):
        # Test with large heights
        assert self.solution.maxArea([10000, 1, 1, 1, 10000]) == 40000
        # Test with max constraint values (height[i] <= 10^4)
        assert self.solution.maxArea([10000, 10000]) == 10000

    def test_zero_heights(self):
        # Test with zeros
        assert self.solution.maxArea([0, 0, 0, 0]) == 0
        assert self.solution.maxArea([1, 0, 1]) == 2
        assert self.solution.maxArea([0, 1, 0]) == 0

    @pytest.mark.parametrize("n,expected", [
        (2, 1),    # Minimum size
    ])
    def test_different_sizes(self, n, expected):
        # Create array of size n with pattern [1,2,3,2,1,...]
        heights = [(i % 3) + 1 for i in range(n)]
        result = self.solution.maxArea(heights)
        assert result >= expected  # We know the minimum area possible