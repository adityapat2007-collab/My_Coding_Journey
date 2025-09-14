arr = [1,1,0,0,1,1,1,0,1]
count = 0
max_cnt = 0
for i in range(len(arr)):
    if arr[i]==1:
        count += 1
        max_cnt = max(max_cnt, count)
    else:
        count = 0
print(max_cnt)