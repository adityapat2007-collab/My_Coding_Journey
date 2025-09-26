arr = [-2,-3,4,-1,-2,1,5,-3]
#to find: maximum possible sum of a subarray (including empty subarrays) and print subarray
#optimal: Kadane's algorithm; TC = O(N), SC = O(1)
print(arr)
a_start, a_end = -1, -1
maxi = -1000000
start = -1
s = 0
for i in range(len(arr)):
    if s == 0: # all subarrays start when s=0
        start = i
    s += arr[i]
    if s>maxi:
        maxi = s
        a_start = start
        a_end = i
    # a_end will go from s=0 to one element before next s=0
    if s<0: # if sum<0, it'll obviously decrease the sum later, so remove
        s = 0
if maxi<0:
    maxi = 0 #if maximum sum of subarray is less than zero, consider empty subarray
print(maxi)
sub = []
for i in range(a_start, a_end+1):
    sub.append(arr[i])
print(sub)

