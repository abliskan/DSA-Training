class Solution:
    def romanToInt(self, s: str) -> int:
        # Input validation
        if not s:  # Handle empty string
            raise ValueError("Input string cannot be empty")
            
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        # Validate all characters are valid Roman numerals
        if not all(c in roman for c in s):
            raise ValueError("Invalid Roman numeral characters")
            
        # For single character case
        if len(s) == 1:
            return roman[s]
            
        res = 0
        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                res -= roman[a]
            else:
                res += roman[a]
        return res + roman[s[-1]]

import pytest

class TestRomanToInt:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize("roman_numeral,expected", [
        ("I", 1),
        ("III", 3),
        ("IV", 4),
        ("V", 5),
        ("IX", 9),
        ("X", 10),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("XCIX", 99),
        ("CDXLIV", 444),
        ("MM", 2000),
        ("LXXX", 80),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900)
    ])
    def test_roman_to_int(self, roman_numeral, expected):
        assert self.solution.romanToInt(roman_numeral) == expected

    def test_single_character(self):
        assert self.solution.romanToInt("M") == 1000
        assert self.solution.romanToInt("D") == 500
        assert self.solution.romanToInt("C") == 100

    def test_subtractive_pairs(self):
        assert self.solution.romanToInt("IV") == 4
        assert self.solution.romanToInt("IX") == 9
        assert self.solution.romanToInt("XL") == 40
        assert self.solution.romanToInt("XC") == 90
        assert self.solution.romanToInt("CD") == 400
        assert self.solution.romanToInt("CM") == 900

    def test_repetitive_numerals(self):
        assert self.solution.romanToInt("III") == 3
        assert self.solution.romanToInt("XXX") == 30
        assert self.solution.romanToInt("CCC") == 300
        assert self.solution.romanToInt("MMM") == 3000

    def test_invalid_input(self):
        with pytest.raises(ValueError, match="Input string cannot be empty"):
            self.solution.romanToInt("")
            
        with pytest.raises(ValueError, match="Invalid Roman numeral characters"):
            self.solution.romanToInt("ABC")
            
        with pytest.raises(ValueError, match="Invalid Roman numeral characters"):
            self.solution.romanToInt("lviii")  # Testing case sensitivity