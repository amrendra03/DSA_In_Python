list = [1, 2, 3, 4, 5, 6, 7]
# list=[-1,-100,3,99]

temp = []
size = len(list)
rot = 4
i = 0
while i < rot:
    temp.append(list[i])
    i = i + 1
i = 0
while rot < size:
    list[i] = list[rot]
    print(list[i])
    i = i + 1
    rot = rot + 1

list[:] = list[: i] + temp

print("Enter", list)
for i in range(len(list)):
    print(list[i])
# Small code for rotation of array
'''arr=[1,2,3,4,5]
d=4
arr=arr[d:]+arr[:d]
print(arr)'''
