# Max-Heap data structure in Python

def heapify_max(array, length, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < length and array[index] < array[left]:
        largest = left
    if right < length and arr[largest] < array[right]:
        largest = right
    if largest != index:
        arr[index], array[largest] = array[largest], array[index]
        heapify_max(arr, length, largest)


def insert_element(array, temp_element):
    size = len(array)
    if size == 0:
        array.append(temp_element)
    else:
        array.append(temp_element)
        for i in range((size // 2) - 1, -1, -1):
            heapify_max(array, size, i)


def delete_element(array, element):
    size = len(array)
    i = 0
    for i in range(0, size):
        if element == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]
    array.remove(element)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify_max(array, len(array), i)


if __name__ == '__main__':
    arr = []
    insert_element(arr, 3)
    insert_element(arr, 4)
    insert_element(arr, 9)
    insert_element(arr, 5)
    insert_element(arr, 2)

    print("Max-Heap array: " + str(arr))
    delete_element(arr, 4)
    print("After deleting an element: " + str(arr))
