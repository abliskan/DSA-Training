# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
  temp = int(input().strip())
  for _ in range(temp):
      x, m = int(input().strip()), set(map(int, input().split()))
      y, n = int(input().strip()), set(map(int, input().split()))
        
      print(True if m.issubset(n) else False) 
      # print(True if n.issuperset(m) else False)