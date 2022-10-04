x = set(map(int, input().split()))
sets = [
    set(map(int, input().split()))
    for n in range(int(input()))
]
print(all([x > y for y in sets]))