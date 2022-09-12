if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list_x = []
    list_y = []
    list_z = []
    for i in range(x+1):
        for j in range (y+1):
            for k in range (z+1):
                if i+j+k != n:
                   list_x.append(i)
                   list_y.append(j)
                   list_z.append(k)
    print(list(list(t) for t in zip(list_x, list_y, list_z)))