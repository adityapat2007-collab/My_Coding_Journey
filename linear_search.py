arr = list(map(int, input().split()))
n = int(input("Number to search: "))
idx = -69
for i in range(len(arr)):
    if arr[i] == n:
        idx = i
        break
print(f"Index of {n} is {idx} ")

