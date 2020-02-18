# A recursive algo must:
# 1. Have a base case
# 2. Change its state and move toward the base case
# 3. Call itself, recursively

# Print every number, starting at 'number', until you reach 0

def recurse(number):
    if number <= 0:
        return
    
    print(number)
    number -= 1
    recurse(number)

# Fibonacci Sequence [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Returns the nth Fiobnacci number

def fibonacci(n):
    if n < 0:
        print("Negative numbers are a no-no :/")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #return (n - 1) + (n - 2)
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(8))