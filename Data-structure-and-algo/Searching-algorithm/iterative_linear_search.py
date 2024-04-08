"""
input1: {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
search1: 110
output1: 6 or element x is present at index 6

input2: {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
search2: -1
output2: -1 or element x is not present in array
"""


def iterative_linear_search(arr, x):
    for i in range(len(arr)):
        current_index = i
        print(f"Looping currently in index {current_index}")
        if arr[i] == x:
            target_index = i
            return f"Element you search {x} is present at index {target_index}"

    return f"Element you search {x} does not appear in the list"


array = [2, 5, 8, 10, 16, 22, 25]
# array = [8, 10, 16, 22, 25, 32]
target1 = 10 # part of element in array
target2 = 40 # outside element in array
search_target = iterative_linear_search(array, target2)
print(search_target)