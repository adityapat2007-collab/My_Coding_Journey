t = int(input())  # test cases
# to check if array has elements in non-decreasing order
while t > 0:
    N = int(input())  # the number of elements
    d = list(map(int, input().split()))# d is an array with N elements
    arr = d.copy()
    d.sort()
    if arr == d:
        print("Yes")
    else:
        print("No")

    t -= 1
