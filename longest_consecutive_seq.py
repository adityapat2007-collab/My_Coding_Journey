# to print: length of longest consecutive sequence in an array
arr = [10,4,20,1,3,2] # to print: 4
# m1: sort and check
length,max_length = 1,1
arr.sort() # [1,2,3,4,9,10,20]
for i in range(len(arr)):
    if (arr[i]+1) in arr:
        length += 1
        max_length = max(max_length, length)
    else:
        length = 1
print(max_length)

# m2: a sequence starts from a number if one less than that number doesn't exist
# so throw all numbers in a hash set and check if n-1 exists in it
length, max_length = 1, 1
hashSet = set(arr)
for i in hashSet:
    if (i-1) not in hashSet:
        length = 1
        while (i+length) in hashSet:
            length += 1
        max_length = max(max_length, length)
print(max_length)