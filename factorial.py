num = int(input("Enter any number: "))

def recursive_factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * recursive_factorial(num - 1)

print(f"Factorial of {num} is: ",recursive_factorial(num))