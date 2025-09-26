arr = [1,2,3,1,1,1,1,3,3]
# optimal solution (for all types of problems): hash map and prefix sum concepts
# good solution for positives and zeroes, optimal: 2-pointer approach
# worst case time complexity: O(n**2) {unordered map, heavy collisions possible}

remainder = 0
prefix_sum = 0
max_len = 0
length=0
start_index = 0
hash_map = {0:-1}
k = int(input())

for i in range(len(arr)):
    prefix_sum += arr[i] #adding sum from beginning

    if prefix_sum == k:
        max_len = max(max_len,i+1) #i+1 if it subarray at i=0 itself

    remainder = prefix_sum - k # k + x-k = x
    if remainder in hash_map:
        start_index = hash_map[remainder] # where the remainder x-k was found
        length = i - start_index # length of subarray giving sum == k
        max_len = max(max_len,length)

    if prefix_sum not in hash_map:
        hash_map[prefix_sum] = i # adding sums as keys to access the index where rem was found, if not present in map

print(max_len)

#two pointer approach: optimal for positives and zeroes
'''prefix_sum = 0
max_len = 0
length = 0
i,j = 0,0
k = int(input())
for j in range(i,len(arr)):
    prefix_sum += arr[j]
    if prefix_sum > k:
        prefix_sum = prefix_sum - arr[i]
        i+=1
    if prefix_sum == k:
        length = j-i+1
        max_len = max(max_len,length)
print(max_len)'''

