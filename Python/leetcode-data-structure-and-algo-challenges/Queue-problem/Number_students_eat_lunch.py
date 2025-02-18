from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while len(students) > count:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                count = 0
            else:
                students.append(students[0])
                count+=1
            students.pop(0)
        return len(students)

import pytest

def test_basic_case():
    """Test basic case where some students can't eat"""
    solution = Solution()
    students = [1, 1, 0, 0]
    sandwiches = [0, 1, 0, 1]
    assert solution.countStudents(students, sandwiches) == 0

@pytest.mark.parametrize("students, sandwiches, expected", [
    ([1, 1, 0, 0], [0, 1, 0, 1], 0)
])
def test_count_students_parameterized(students, sandwiches, expected):
    """Parameterized test covering multiple scenarios"""
    solution = Solution()
    assert solution.countStudents(students, sandwiches) == expected