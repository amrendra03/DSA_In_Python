'''Declaring the Sum function'''
def sum(arr):
    s = 0;
    for i in range(len(arr)):
        s = s + arr[i]
    '''Return the S '''
    return s

'''We use list as a Array otherwise we can use also different Array by importing NUmpy library'''
arr = []
l = int(input("Enter the length of array \n"))
for i in range(l):
    j=int(input())
    arr.append(j)
    print("aarr ",arr[i],"i ",i)
    '''Calling FUnction and passing the arguments in function'''
ans = sum(arr)

print(ans)
