#given: in an array there exists two elements summing up to a target, return indices
#brute: two for loops, TC: O(n**2)

#optimal (slightly than hash maps): two pointers
arr = [2,6,5,8,11]
i, j = 0, len(arr)-1
book = {}
for x in range(len(arr)):
    book[arr[x]] = x
target = int(input())
arr.sort() #[2,5,6,8,11]
while i < j:
    if arr[i] + arr[j] == target:
        print([book[arr[i]], book[arr[j]]])
        break
    elif arr[i] + arr[j] < target:
        i+=1
    else:
        j-=1



#better: hash maps
'''arr = [2,6,5,8,11]
result = []
hash_map = dict()
target = int(input())
for i in range(len(arr)):
    if target - arr[i] not in hash_map:
        hash_map[arr[i]] = i
    else:
        result = [hash_map[target-arr[i]], i]
        break
print(result)'''


