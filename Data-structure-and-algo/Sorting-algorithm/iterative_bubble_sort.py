def iterative_bubble_sort(arr, n):
    for i in range(n):
        swapped = 0
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = 1

        if swapped == 0:
            break
    return arr


array = [67, 44, 82, 17, 20, 15, 89, 92]
array_index = len(array)
print("Array before Sorting: ")
print(array)
iterative_bubble_sort(array, array_index)
print("Array after Sorting: ")
print(array)
