# M1: using recursion & backtracking:
# TC: O(2^N), SC: O(N) for the extra subset and recursion stack
def recursion(i,arr,result,subset):
    if i == len(arr): # adding the last subset, which is arr
        result.append(list(subset))
        return
    subset.append(arr[i])  # include the current value
    recursion(i+1,arr,result,subset)
    # now the backtracking step and finding all the other subarray
    subset.pop()
    recursion(i+1,arr,result,subset)
def subsets(arr):
    subset = []
    result = []
    recursion(0,arr,result,subset)
    return result
if __name__ == '__main__':
    Arr = [1,2,3]
    Result = subsets(Arr)
    print("Using recursion: ")
    for Subset in Result:
        print("[",end = '')
        print(', '.join(str(num) for num in Subset), end = '')
        print("]")

# M2: bit-masking / bit manipulation
# TC: O(2^N), SC: O(n) (this is just easier to write compared to recursion)

def bit(arr):
    n = len(arr)
    result = []
    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(arr[j])
        result.append(subset)
    return result
if __name__ == "__main__":
    Arr = [1,2,3]
    Result = bit(Arr)
    print("Using bit manipulation: ")
    for Subset in Result:
        print("[",end = '')
        print(", ".join(str(num) for num in Subset),end='')
        print("]")