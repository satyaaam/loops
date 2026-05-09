number = list(map(int, input("Enter numbers separated by space: ").split()))
smallest = number[0]
for num in number:
    if num < smallest:
        smallest = num
print("The smallest number is:", smallest)