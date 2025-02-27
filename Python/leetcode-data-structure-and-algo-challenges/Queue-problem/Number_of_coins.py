import pytest
from typing import List
import math

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [math.inf for _ in range(n+1)]
        dp[-1] = 0
        for i in range(n-1,-1,-1):
            for j in range(i+1, min(i+i+3, n+1)):
                dp[i] = min(dp[i], dp[j] + prices[i])
        return dp[0]

# Corrected test cases
def test_example_1():
    sol = Solution()
    prices = [3, 1, 2]
    expected = 4
    assert sol.minimumCoins(prices) == expected, f"Expected {expected}, got {sol.minimumCoins(prices)}"
    
def test_example_2():
    sol = Solution()
    prices = [1, 10, 1, 1]
    expected = 2
    assert sol.minimumCoins(prices) == expected, f"Expected {expected}, got {sol.minimumCoins(prices)}"