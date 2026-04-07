num = int(input("Enter any number: "))
# int typecasting yani type conversion ke liye lagaya he kyu ke input as a string consider horaha tha 

def recursive_factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * recursive_factorial(num - 1)

print(f"Factorial of {num} is: ",recursive_factorial(num))
# string literals mene js me seekhi thi aur python me research ki to isme bhi syntax milgaya 🤣