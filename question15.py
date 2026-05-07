# Print numbers divisible by 3 and 5

# for a number

number = int(input("Enter a number: "))
if number % 3 == 0:
    print(f"{number} is divisible by 3")
else:
    print(f"{number} is not divisible by 3")
if number % 5 == 0:
    print(f"{number} is divisible by 5")
else:
    print(f"{number} is not divisible by 5")


# for range of numbers


n = int(input("Enter the limit: "))

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)