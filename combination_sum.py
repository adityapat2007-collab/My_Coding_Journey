# to find and print elements summing to a target sum
# concept: recursion and backtracking -> pick, no pick
# C1: inputs don't have duplicates and one element can be used unlimited times -
arr = [2,3,5,7]
arr2 = [2,2,3,5,7,7]
target_arr = []
target_arr2 = []
def combination_sum(ds, target, ind): # ds is an array
    # base case:
    if ind == len(arr):
        if target == 0:
            target_arr.append(ds[:]) # append element array to resulting array
        return
    if arr[ind] <= target:
        ds.append(arr[ind])
        # pick element
        combination_sum(ds, target - arr[ind], ind) # here we use ind and not ind+1 as we can use one element multiple times
        ds.pop() # backtracking
    combination_sum(ds, target , ind+1) # not picking element
combination_sum([], 7, 0)
print(target_arr)

# C2: if inputs have duplicates and one element can be used only once -
arr2.sort() # because line 35 assumes array to be sorted
def combination_sum2(ds, target, ind):
    if ind == len(arr2):
        if target == 0:
            target_arr2.append(ds[:])
        return
    if arr2[ind] <= target:
        ds.append(arr2[ind])
        combination_sum2(ds, target - arr2[ind], ind+1) # here ind+1 because can't use one element multiple times
        ds.pop()
    # this part to skip duplicates to avoid repeated elements in dp
    next_idx = ind + 1
    while next_idx < len(arr2) and arr2[next_idx] == arr2[ind]:
        next_idx += 1
    combination_sum2(ds, target , next_idx)
combination_sum2([], 7, 0)
print(target_arr2)
