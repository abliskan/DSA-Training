def recursive_linear_search(arr, x, index=0):
    # Element not found
    if index >= len(arr):
        return f"Element you search {x} does not appear in the list"
    # Element found
    if arr[index] == x:
        return f"Element you search {x} is present at index {index}"
    return recursive_linear_search(arr, x, index + 1)


array = [1, 5, 7, 20, 5, 9, 10, 11]
target1 = 15
target2 = 20
print(recursive_linear_search(array, target2))