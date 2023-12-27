'''
from tkinter.font import names


def printme(*names):
    print(len(names))
    print('type of passed argumentis',type(names))
    print('Printing the passed argument')
    for name in names:
        print(name)
printme("abc","pqr","xyz","lmn")
'''

#make a programme calculate the m,arks of student 
def marks(*mrk):
    s=sum(mrk)
    return s
n=int(input('number of marks\n'))
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=marks(a,b,c,d)
print(e)