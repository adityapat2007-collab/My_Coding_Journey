# concept: start from 2, remove all the multiples of 2, then go to 3 and do the same thing till sqrt(n)
# why till sqrt(n) only? cuz that's the highest possible factor of n
# removing composites is easier than printing primes
# time complexity: O(nlog(logn)) - almost close to linear time, space complexity: O(n) for boolean array

import math
n = int(input("Till where do you want to find primes? "))
isPrime = [True for i in range(n+1)]
isPrime[0],isPrime[1] = False,False # 0 and 1 are not considered as prime
for i in range(2,math.floor(math.sqrt(n))+1):
    if isPrime[i]:
        for j in range(i**2,n+1,i):
            isPrime[j] = False
primes = []
for i in range(2,n+1):
    if isPrime[i]:
        primes.append(i)
print(primes)
