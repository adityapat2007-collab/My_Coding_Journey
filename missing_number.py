arr = [1,2,3,4,5,7] #len = 6

'''obvious first optimal solution: difference in sum
n = arr[len(arr)-1]
sum = 0
for i in arr:
    sum+=i
sum2 = int(n*(n+1)/2)
print(f"Missing num = {sum2-sum}")'''

#not obvious, best optimal solution: XOR operation
# a^a = 0  (a^b = a.b' + b.a')
#sligthly better as if for sum, n~10^5 will give overflow error, whereas xor doesn't

n = len(arr) # n=6
xor1 , xor2 = 0, 0
for i in range(n): # i runs from 0->5
    xor1^=arr[i] #1^2^3^4^5^7
    xor2^=i+1 # 1^2^3^4^5^6
xor2^=arr[n-1] # for xor-ing the last element
print(f"Missing num = {xor2^xor1}")

