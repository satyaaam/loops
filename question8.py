# Find sum of digits of a number

n = int(input("Enter a number: "))
sum = 0
for i in str(n):
    sum += int(i)
print("The sum of digits of", n, "is:", sum)