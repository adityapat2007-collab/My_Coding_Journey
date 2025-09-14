'''arr1 = [1,1,2,3,4]
arr2 = [2,2,3,4,5,5,6]
arr_set = set() #using sets because they don't allow duplicates ,brute force solution
for i in arr1: # time complexity: n1logn
    arr_set.add(i)
for i in arr2: # time complexity: n2logn
    arr_set.add(i)
union_arr = []
for i in arr_set: # time complexity: n1+n2
    union_arr.append(i)
print(union_arr)'''

# optimal solution: two pointers for each array
def find_union(arr1, arr2):
    i = 0  # Pointer for arr1
    j = 0  # Pointer for arr2
    union_array = []

    # Loop as long as both pointers are within their arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            # If the union_array is empty OR the last element is not a duplicate...
            if not union_array or union_array[-1] != arr1[i]:
                union_array.append(arr1[i])
            i += 1  # Move the first pointer
        elif arr2[j] < arr1[i]:
            if not union_array or union_array[-1] != arr2[j]:
                union_array.append(arr2[j])
            j += 1  # Move the second pointer
        else:  # This means arr1[i] == arr2[j]
            if not union_array or union_array[-1] != arr1[i]:
                union_array.append(arr1[i])
            i += 1  # Move both pointers
            j += 1

    # Add any remaining elements from arr1
    while i < len(arr1):
        if not union_array or union_array[-1] != arr1[i]:
            union_array.append(arr1[i])
        i += 1

    # Add any remaining elements from arr2
    while j < len(arr2):
        if not union_array or union_array[-1] != arr2[j]:
            union_array.append(arr2[j])
        j += 1

    return union_array

arr1 = [1, 1, 3, 4]
arr2 = [1, 2, 2, 3, 4, 5, 5, 6]

print(find_union(arr1, arr2))


