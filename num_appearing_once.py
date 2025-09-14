arr = [1,1,2,2,3,3,5,6,6,7,7]
# first the obvious hashing solution
'''freq_map = {}
for i in arr:
    freq_map[i] = freq_map.get(i, 0) + 1
for num, count in freq_map.items():
    if count == 1:
        print(f"{num} appears once")
        break
else:
    print(f"None appear once")'''
# then not so obvious: using xor
xor = 0
for i in arr:
    xor^=i
print(f"{xor} appears once")
