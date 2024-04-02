def permutation_recursive(string, pocket = ""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permutation_recursive(together, letter + pocket)

print(permutation_recursive("ABCD", ""))