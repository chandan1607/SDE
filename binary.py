number = int(input("Enter the number\n")) # reading the input
# number = [1,2,3]
ans = 0                             # In the initial stage initialze it to "0"
i = 0                               # for the loop increment
while number != 0:                  # until n will not become 0 do inside the loop
    digit = number & 1              # comparing the last bit of the number in binary
    print(digit)
    ans = digit * pow(10, i) + ans # it will give you the reverse of the number
    # ans = ans * 10 + digit
    number = number>>1
    i = i+1

print(ans)
566993