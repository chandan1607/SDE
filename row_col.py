numbers = 4
row = 1
value = 1

while row <= numbers:

    space = numbers - row
    # count = row
    while space:
        print("")
        space = space - 1
    col = 1
    while col <= numbers:
        # char = chr(ord('A') + row - 1)
        print("*","",end="")
        # print(row+col-1,"",end="")
        # value = value + 1
        # count = count + 1
        col = col+1

    print("")
    row = row+1
