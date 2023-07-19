n = int(input("Enter the value of n\n"))
a = 0
b = 1
print(a,b,end=" ")
for i in range(n):
    next_number = a+b
    print(next_number,end=" ")
    a = b
    b = next_number;