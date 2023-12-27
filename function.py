a=[]
b=int(input('Enter no of elements\n'))
print('Enter the numbers in list\n')
for c in range(b):
    c=int(input())
    a.append(c)
print(a)
d=int(input('Enter the number to devide the list numbers\n'))
e=list(filter(lambda x:(x%d==0),a))
print(e)


