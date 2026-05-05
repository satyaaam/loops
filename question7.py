#  Count digits in a number


num = int(input("Enter a number: "))

count = 0

if num == 0:
    count = 1
else:
    num = abs(num)
    for i in range(len(str(num))):
        count += 1

print("Number of digits:", count)