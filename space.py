number =5

row = 1
while row <= number:

    # space = row - 1
    # while space:
    #     print(" ", end="")
    #     space = space - 1
    col = 1
    star = number - row + 1
    while col <= star:
        print(col, "",end="")
        col = col + 1

    second = row - 1
    while second:
        print("*", "", end="")
        second = second - 1

    third = row - 1
    while third:
        print("*", "", end="")
        third = third - 1

    ts = 1
    third_star = number - row + 1
    while ts <= third_star:
        print(ts, "", end="")
        ts = ts + 1




    row = row + 1
    print("")

