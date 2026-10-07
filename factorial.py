num = int(input("Enter a positive number: "))
if num < 0:
    print("Factorial does notexist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * 1
    print(f"The factorial of {num} is {factorial}")  