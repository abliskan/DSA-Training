# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = input().split()
words = defaultdict(list)
for i in range(int(n)):
    a = input().strip()
    words[a].append(i+1)

for _ in range(int(m)):
    b = input().strip()
    print(*words[b]) if words[b] else print(-1)