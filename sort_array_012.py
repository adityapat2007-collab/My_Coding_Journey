#brute force: count number of 0s,1s and 2s, then manually override sort
#optimal: Dutch National Flag Algorithm (three pointer approach)
# TC: O(N), because all the 3 checks swap 1 number; SC = O(1)
arr = [0,1,1,0,1,2,1,2,0,0,1]
low,mid,high = 0,1,len(arr)-1
while mid <= high:
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low,mid = low+1,mid+1
    elif arr[mid] == 1:
        mid+=1
    elif arr[mid] == 2:
        arr[high], arr[mid] = arr[mid], arr[high]
        high-=1
print(arr)

