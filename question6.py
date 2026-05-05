# . Print multiplication table of a number

n = int(input("Enter a number: "))
for i in range(1, 10 + 1):
    print(n, "x", i, "=", n * i)
    i += 1