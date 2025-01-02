

n = int(input("Please enter any number:"))
print("The list of numbers from 1", "to",n)
for i in range(1, n+1):
    print(i,end=' ')



num = int(input("Please Enter any Number: "))


factorial = 1


for i in range(1, num + 1):
    factorial *= i


print(f"The factorial of {num} is {factorial}")
