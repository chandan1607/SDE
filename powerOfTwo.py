

def powerOfTwo(n):
    ans = int(1)
    for i in range(0,30):
        print(ans)
        if ans == n:
            print(ans)
            return True
        ans = ans * 2
    return False

print(powerOfTwo(16))