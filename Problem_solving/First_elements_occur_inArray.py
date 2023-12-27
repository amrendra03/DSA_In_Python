def firstElementKTime( a, n, k):
    # code here
    dic = {}
    for i in a:
        print('p',i)
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
        if dic[i]==k:
            return i
    return -1

arr = [4, 7, 4, 7, 7,7,4]
n = 7
k = 2
print(firstElementKTime(arr, n, k))
