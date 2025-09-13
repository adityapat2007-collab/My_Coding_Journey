#sum of n numbers using recursion (no using loops)
#concept: S(n) = n + S(n-1), eg: S(1) = S(0) + 1

# functional method::
'''def sum_numbers(n):
    sum = 0
    if n>0:
        sum = n + sum_numbers(n-1)
        # n=2, sum = 3... sum = 2+sum_numbers(1)
        # n=1, sum = 1+ sum_numbers(0) = 1
    elif n==0:
        sum = 0
    else:
        print("Enter a positive number")
    return sum
n = int(input("Enter a number: "))
print(f"Sum of natural numbers till {n} is {sum_numbers(n)}")'''

def sum_numbers(n,sum):
    if n<1:
        print(f"Sum of natural numbers is {sum}")
        return
    else:
        return sum_numbers(n-1,sum+n)
n = int(input("Enter a number: "))
sum_numbers(n,0)





