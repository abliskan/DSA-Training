def merge_sort(arr, left, mid, right):
    left_range = mid - left + 1
    right_range = right - mid

    # create temp arrays
    temp_left = [0] * left_range
    temp_right = [0] * right_range

    # Copy data to temp arrays temp_left[] and temp_right[]
    for x_left in range(0, left_range):
        temp_left[x_left] = arr[left + x_left]

    for y_right in range(0, right_range):
        temp_right[y_right] = arr[mid + 1 + y_right]

    i = 0
    j = 0
    k = left  # initial index for merged

    # Merge the temp back into arr
    while i < left_range and j < right_range:
        if temp_left[i] <= temp_right[j]:
            arr[k] = temp_left[i]
            i += 1
        else:
            arr[k] = temp_right[j]
            j += 1
        k += 1

    # Copy the remaining elements of temp_left[]
    while i < left_range:
        arr[k] = temp_left[i]
        i += 1
        k += 1

    # Copy the remaining elements of temp_right[]
    while j < right_range:
        arr[k] = temp_right[j]
        j += 1
        k += 1


def recursive_sort(arr, left, right):
    if left < right:
        # Same as (l+r)//2, but for avoids overflow use this instead
        mid = left + (right - left) // 2

        # recursive sort first subarray and second subarray
        recursive_sort(arr, left, mid)
        recursive_sort(arr, mid + 1, right)
        # recursive merge first subarray and second subarray
        merge_sort(arr, left, mid, right)


# Driver code to test above
array = [67, 44, 82, 17, 20, 15, 89, 92]
n = len(array)
print("Given array is: ", array)
recursive_sort(array, 0, n - 1)
print("\nSorted array is: ", array)
