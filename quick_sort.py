def partition(arr,low,high):
  pivot = arr[high]#last element as the pivot
  i = low - 1

  for j in range(low,high):
    if arr[j]<=pivot:
      i+=1
      arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1


def quickSort(arr,low = 0,high = None):
  if high is None:
    high = len(arr) - 1
  if low < high:
    pivot_idx = partition(arr,low,high)
    quickSort(arr,low,pivot_idx-1)
    quickSort(arr,pivot_idx+1,high)


my_arr = [1,11,9,12,7,3]
quickSort(my_arr)
print(my_arr)
