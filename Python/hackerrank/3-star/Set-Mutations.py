# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
temp = set(map(int,input().split()))
for _ in range(int(input())):
    y = input().split()
    getattr(temp,y[0])(set(map(int,input().split())))

print(sum(temp))