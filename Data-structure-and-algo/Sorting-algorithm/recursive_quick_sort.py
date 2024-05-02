def recursive_quick_sort(Arr, left, right):
    if left < right:
        partition_arr = partition(Arr, left, right)
        recursive_quick_sort(Arr, left, partition_arr-1) # left sort
        recursive_quick_sort(Arr, partition_arr+1, right) # right sort


def partition(Arr, left, right):
    # Choose the highest element as the pivot
    pivot = Arr[right]
    # pointer for greater element
    i = left - 1
    for j in range(left, right):
        if Arr[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i += 1
            # Swapping element at i with element at j
            Arr[i], Arr[j] = Arr[j], Arr[i]

    # Swap the pivot element with the greater element specified by i
    Arr[i + 1], Arr[right] = Arr[right], Arr[i + 1]
    # Return the position from where partition is done
    return i + 1


array = [4, 1, 3, 2, 8, 7, 5]
print("Unsorted Array")
print(array)

n = len(array)

recursive_quick_sort(array, 0, n-1)

print('\nSorted Array in Ascending Order:')
print(array)