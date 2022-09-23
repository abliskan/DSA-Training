def average(array):
    # your code goes here
    x = list(set(array))
    return sum(x)/len(x)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)