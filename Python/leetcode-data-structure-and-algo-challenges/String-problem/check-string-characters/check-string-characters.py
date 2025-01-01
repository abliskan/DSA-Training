from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        """
        Check if all characters in string have equal number of occurrences.
        Empty string returns True as it satisfies the condition vacuously.
    
        Args:
            s: Input string
        
        Returns:
            bool: True if all characters occur same number of times or string is empty
        """
        if not s:
            return True
    
        map = Counter(s)
        return len(set(map.values())) == 1

import pytest

def test_basic_equal_occurrences():
    """Test string where all characters appear same number of times"""
    solution = Solution()
    assert solution.areOccurrencesEqual("abacbc") == True  # each char appears twice

def test_unequal_occurrences():
    """Test string where characters appear different number of times"""
    solution = Solution()
    assert solution.areOccurrencesEqual("aaabb") == False  # 'a' appears 3 times, 'b' appears 2 times

def test_single_character():
    """Test string with single character repeated"""
    solution = Solution()
    assert solution.areOccurrencesEqual("aaaa") == True  # single char repeated

def test_empty_string():
    """Test empty string"""
    solution = Solution()
    assert solution.areOccurrencesEqual("") == True  # empty string case

def test_two_characters():
    """Test string with two different characters"""
    solution = Solution()
    assert solution.areOccurrencesEqual("ab") == True  # each appears once

def test_case_sensitivity():
    """Test case sensitivity"""
    solution = Solution()
    assert solution.areOccurrencesEqual("aAaA") == True  # 'a' and 'A' are different chars

def test_numbers_and_special_chars():
    """Test string with numbers and special characters"""
    solution = Solution()
    assert solution.areOccurrencesEqual("11@@") == True  # numbers and special chars

def test_long_string():
    """Test longer string with multiple character types"""
    solution = Solution()
    assert solution.areOccurrencesEqual("aabbccddee") == True  # each char appears twice

def test_single_occurrence():
    """Test string where each character appears exactly once"""
    solution = Solution()
    assert solution.areOccurrencesEqual("abcde") == True  # each char appears once

@pytest.mark.parametrize("input_str, expected", [
    ("abacbc", True),    # each char appears twice
    ("aaabb", False),    # unequal occurrences
    ("aaaa", True),      # single char repeated
    ("", True),          # empty string
    ("ab", True),        # two different chars once
    ("aAaA", True),      # case sensitive
    ("11@@", True),      # numbers and special chars
    ("aabbccddee", True) # multiple chars, equal occurrences
])
def test_are_occurrences_equal_parameterized(input_str, expected):
    """Parameterized test covering multiple scenarios"""
    solution = Solution()
    assert solution.areOccurrencesEqual(input_str) == expected
    
if __name__ == "__main__":
    solution = Solution()
    str_word = "abacbc"
    result = solution.areOccurrencesEqual(str_word)
    print(f"Output test-order: {result}")