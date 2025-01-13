from typing import List
import pytest

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            raise IndexError("Input list is empty")
            
        # Take first string as reference
        pref = strs[0]
        
        # Compare with all other strings
        for i in range(1, len(strs)):
            # Keep reducing prefix until it matches current string
            while strs[i][:len(pref)] != pref:
                pref = pref[:-1]
                if not pref:  # If prefix becomes empty
                    return ""
        return pref

class TestLongestCommonPrefix:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize("input_strs,expected", [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["throne", "throne"], "throne"),
        ([""], ""),
        (["a"], "a"),
        (["", "b"], ""),
        (["flower", "flower", "flower", "flower"], "flower"),
    ])
    def test_common_cases(self, input_strs, expected):
        assert self.solution.longestCommonPrefix(input_strs) == expected

    def test_empty_list(self):
        with pytest.raises(IndexError):
            self.solution.longestCommonPrefix([])

    def test_case_sensitivity(self):
        # Testing that the function is case-sensitive
        input_strs = ["Flower", "flower", "FLOWER"]
        assert self.solution.longestCommonPrefix(input_strs) == ""