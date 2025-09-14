arr = list(map(int, input("Enter nums spaced: ").split()))#[1,2,3,4,5,6,7]
lr = input("Rotate Left or Right?: ")
lr=lr.lower()
if lr != 'left' and lr != 'right':
    print("Invalid input")
    exit()
k = int(input("Enter places to rotate: "))#k=3 --> rotated array: [4,5,6,7,1,2,3]
if lr == "left":#--> rotated array: [4,5,6,7,1,2,3]
    arr[0:k] = arr[0:k][::-1]
    arr[k:] = arr[k:][::-1]
    arr.reverse()
    print(f'Rotated array: {arr}')
elif lr == "right":# --> rotated array: [5,6,7,1,2,3,4]
    arr.reverse()
    arr[0:k] = arr[0:k][::-1]
    arr[k:] = arr[k:][::-1]
    print("Rotated array: ", arr)


