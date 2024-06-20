def recursive_binary_search(arr, first_index, last_index, target):
    if last_index >= first_index:
        middle_index = first_index + last_index - 1 // 2
        if target > arr[middle_index]:
            recursive_binary_search(arr, middle_index + 1, last_index, target)
        elif target < arr[middle_index]:
            return recursive_binary_search(arr, first_index, last_index - 1, target)
        else:
            return middle_index
    else:
        return -1


array = [2, 5, 8, 10, 16, 22, 25]
# array = [8, 10, 16, 22, 25, 32]
target = 10
search_target = recursive_binary_search(array, 0, len(array) - 1, target)
print(f"Element you search {target} is present at index {search_target}")
