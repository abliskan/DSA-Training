# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
for _ in range(int(input())):
    cmd, *n = input().split()
    getattr(d, cmd)(*n)
print(*d)