# Print square of numbers from 2 to n




n = int(input("Enter a number: "))
i = 2
while i <= n:
    print(f"The square of {i} is {i * i}")
    i +=1




n = int(input("Enter a number: "))

for i in range(1,n + 1):
    print(f"The square of {i} is {i * i}")