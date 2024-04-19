class bubble_sort:
    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def __str__(self):
        return " ".join([str(x)
                         for x in self.array])

    def recursive_bubble_sort(self, n=None):
        if n is None:
            n = self.length

        count = 0

        if n == 1:
            return

        for i in range(n - 1):
            if self.array[i] > self.array[i + 1]:
                self.array[i], self.array[i +
                                          1] = self.array[i + 1], self.array[i]
                count = count + 1

        if count == 0:
            return

        self.recursive_bubble_sort(n - 1)


def main():
    array = [64, 34, 25, 12, 22, 11, 90]
    print("Array before Sorting: ", array)
    sort = bubble_sort(array)
    sort.recursive_bubble_sort()
    print("Array after Sorting: ", sort)


if __name__ == "__main__":
    main()
