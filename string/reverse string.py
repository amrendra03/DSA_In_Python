b=input("Please input your string\n")
print ("Your input string is: ",b)
print ("The reverse of the input string is: ",end='')
for i in range(len(b)):
    j=i*-1
    if(j<0):
        print(b[j],end='')

print(b[0])
'''
s='hello my'
list=[i for i in s]
list.reverse()
str=''.join(list)
print(str)

'''
