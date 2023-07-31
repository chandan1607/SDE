def complement(n):
    m = n
    mask = 0
    while m != 0:
        mask = (mask << 1) | 1
        m = m >>1

    ans = (~n) & mask
    return ans

n = int(input("Enter your number"))
print(complement(n))
