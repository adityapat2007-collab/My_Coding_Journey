# to find: majority element (occurs more than n/2 times, n=len(arr))
#brute force: nested for loops
#better: hash array
#optimal: Moore's voting algorithm

arr = [7,7,5,7,5,1,1,5,7,2,3,5,5,7,7,5,5,5,5]
#first we assume starting element to be the majority
maj = arr[0]
count = 1
for i in range(1, len(arr)):
    if arr[i] == maj:
        count+=1
    else:
        count-=1
    if count == 0:
        maj = arr[i]
        count=1
# now, the element stored in 'maj' may or may not be the majority element, so verify:
count2 = 1
for i in range(1, len(arr)):
    if arr[i] == maj:
        count2+=1
if count2 > len(arr)/2:
    print(maj)
else:
    print("No majority element")
