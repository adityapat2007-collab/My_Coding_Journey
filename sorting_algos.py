def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)): # time complexity: O(sum of first n-1 natural numbers) == O(n^2)
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def selectionSort(arr): # time complexity: O(n^2) for all scenarios (best, average, worst)
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertionSort(arr): # tc: O(n^2) for worst {when reverse sorted array} and average case, O(n) for best case {for completely sorted array, it checks conditions once per element}
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
    return arr




n = input('Enter elements separated by space: ')
arr = n.split(' ')
for i in range(len(arr)):
    arr[i] = int(arr[i])
print("Selection sorted: ", selectionSort(arr))
print("Bubble sorted: ", bubbleSort(arr))
print("Insertion sorted: ", insertionSort(arr))



