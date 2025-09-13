# to print nth fibonacci number, 0th being 0.
# concept: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
def fibonacci(n):
    if n<=1:
        return n
    elif n<0:
        return "Invalid input"
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n = int(input("Enter position of fibonacci number: "))
print(f"{n}th fibonacci number is {fibonacci(n)}")

