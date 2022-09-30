# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
Student = namedtuple('Student', ",".join(input().split()))
print(sum([int(Student(*input().split()).MARKS) for _ in range(n)])/n)