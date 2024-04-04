def iterative_binary_search(arr, first_index, last_index, target):
    middle_index = (first_index + last_index) // 2
    middle_element = arr[middle_index]
    arr_index = len(arr)
    print(f"Current middle element {middle_element} occurs in position {middle_index}")

    is_found = True
    while is_found:
        if first_index == last_index:
            if target != middle_index:
                is_found = False
                return f"Element you search {target} does not appear in the list"

        if target == arr[middle_index]:
            return f"Element you search {target} is present at index {middle_index}"

        elif target < arr[middle_index]:
            new_index = middle_index - 1
            last_index = new_index
            middle_index = (first_index + last_index) // 2
            if target == arr[middle_index]:
                return f"Element you search {target} is present at index {middle_index}"

        elif target > arr[middle_index]:
            new_index = middle_index + 1
            first_index = new_index
            last_index = arr_index - 1
            middle_index = (first_index + last_index) // 2
            if target == arr[middle_index]:
                return f"Element you search {target} is present at index {middle_index}"


array = [2, 5, 8, 10, 16, 22, 25]
# array = [8, 10, 16, 22, 25, 32]
target = 30
search_target = iterative_binary_search(array, 0, len(array) - 1, target)
print(search_target)