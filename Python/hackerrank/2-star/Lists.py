if __name__ == '__main__':
    N = int(input())
    lst = list()
    for n in range(N):
        x,*y = input().split()
        argument = tuple(map(int,y))
        if x == 'print':
            print(lst)
        else:
            eval('lst.'+x+str(argument))