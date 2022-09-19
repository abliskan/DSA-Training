if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
    [print(names) for names in sorted([name for name,
     tests in l if tests == 
     sorted(list(set([tests for name, tests in l])))[1]])]
     