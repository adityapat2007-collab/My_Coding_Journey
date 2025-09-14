#concept: similar to union of two sorted sets, using two pointers (optimised solution)
arr1 = [1,2,3]
arr2 = [1,2,3,4,5]
int_arr=[]
i,j=0,0 # i for arr1, j for arr2
while i<len(arr1) and j<len(arr2):
    if arr1[i]==arr2[j]: # selecting intersecting elements
        if not int_arr or int_arr[-1]!=arr1[i]:
            int_arr.append(arr1[i])
        i,j=i+1,j+1
    elif arr2[j]<arr1[i]:
            j+=1
    elif arr1[i]<arr2[j]:
            i+=1
# no need to check remaining elements as this is intersection :)
print(int_arr)

