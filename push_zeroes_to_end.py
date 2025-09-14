#Concept: 2 pointers
'''arr = list(map(int, input().split()))
arr.sort()
arr.reverse()
print(arr)'''

arr = list(map(int, input().split())) #[0,1,2,0,3,0,0,5]
j = -1
for i in range(len(arr)):
    if arr[i] == 0:
        j = i # j is always pointing zero
        break
for i in range(j+1, len(arr)): # checking elements after the zero
    if arr[i]!=0:
        arr[i], arr[j] = arr[j], arr[i] # swapping the zero and non zero number
        j+=1 #to keep j on zero always
print(arr)



