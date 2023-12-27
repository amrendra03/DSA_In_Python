'''
def greet(name):
  print('helllo'+name)
  print("\ngood moring")
h=str(input())
greet(h)

def add(a,b):
    sum=a+b
    return sum
def sub(a,b):
    sub=a-b
    return sub
def mul(a,b):
    mul=a*b
    return mul
def div(a,b):
    div=a//b
    return div
a=int(input())
b=int(input())
d=add(a,b)
e=sub(a,b)
f=mul(a,b)
g=div(a,b)
print('sum',d)
print('\nsub',e)
print('\nmul',f)
print('\ndiv',g)
'''
#wap to calculater the area of circle,rectangle amd square
def ca(r):
    area=(3.14)*r*r
    return area
def ra(l,b):
    area=l*b
    return area
def sa(l1):
    area=l1*l1
    return area
r=float(input("Enter radius:"))
l=int(input('Enter the of rectangle lenght:'))
b=int(input('Enter the breadth of rectangle":'))
l1=int(input("Enter the a side value of square:"))

a=ca(r)
b=ra(l,b)
c=sa(l1)
print('circle\n',ca)
print("rectangle\n",b)
print('sa\n',c)
