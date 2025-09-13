arr = list(map(int, input("Enter sorted array: ").split())) # 1 2 3 4 5 6 8
n = int(input("Enter number to be searched: ")) # 5
count = 0
low, high = 0, len(arr)-1 #low = 0, high = 6
while low <= high:
    mid = (low+high)//2 #3, 5, 4
    if arr[mid] < n: # 4<5, true;
        low = mid+1 # low = 4
    elif arr[mid] > n:#; 6>5
        high = mid-1# 4
    if arr[mid] == n:
        print("Element is present at index", mid)
        count = 69
        break
if count != 69:
    print("Element is not present in array")

