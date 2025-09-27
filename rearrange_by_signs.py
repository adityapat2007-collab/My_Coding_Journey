# objective: to rearrange the elements of an array alternating between positive and negative without changing order
# given: there are exactly n/2 positives and negatives (n=len(arr)), and has no zeroes
arr = [3,1,-2,-5,2,-4] # expected o/p: [3,-2,1,-5,2,-4]

# brute force: store +ves and -ves in separate arrays, then join. TC = O(2N), SC = O(N)
# optimal: observation - positives on even index, negative on odd. So use pointers on the arr. TC = O(N), SC = O(N)

result = [0]*len(arr)
pos, neg = 0,1 # pos from even and neg from odd index
for i in range(len(arr)):
    if arr[i] < 0:
        result[neg] = arr[i]
        neg += 2 # next odd index
    else:
        result[pos] = arr[i]
        pos += 2
print(result)

'''for variety 2: if +ves and -ves are not exactly n/2, 
    fall back to brute force solution'''
