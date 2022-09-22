if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(map(int,integer_list))
    print(hash(t))