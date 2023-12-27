'''a=1.5
# Printing the type of the variable a and then converting it to an integer.
print(type(a))
print(int(a))
import fractions
# Printing the fractional representation of the float.
print(fractions.Fraction(a))
import random
print(random.randrange(10,99))
x=['a','b','c','d']
print(random.choice(x))
random.shuffle(x)
print(x)
print(random.random())

# check number is negative or positive
num = float(input('enter the  number:'))
if num>0:
    print('Positive number')
elif num==0:
    print('zero')
else:
    print('number is negative')

#using nested if ,else ,elif

a=int(input('Enter the  number to check positive or negative\n'))
if a>=0:
    if a==0:
        print('number is zero')
    else:
        print('Number is positive')
else:
    print('nUmber is negative')
    
#check a number is odd or even
a=float(input('Enter the number to check it is odd or even\n'))
if a%2==0:
    print('Number is even %3.2f'%a)
else:
    print('Given number is odd %3.2f'%a)
    
    # check it is leap year or not 
a=int(input('Enter the year to check is leap year or not\n'))
if (a%4)==0:
    print('Given year is leap year %4i'%a)
else:
    print('Given year is not leap year %i'%a)

# Find the largest nuber among the given three number
list=[]
a=int(input('Enter the length of elements to get greatest nuber between three numbers\n'))
if a==3:
    
    for i in range(a):
        c=int(input("Enter the number %3i"%a))
        list.append(c)   
    print(list)
else:
    print('bsdk lawde bola tha 3 number \n')

# The below code is comparing the three numbers and printing the greatest number.
x=float (input('Enter the 1 number for comprision\n'))
y=float (input('Enter the 2 nuber for comprision\n'))
z=float (input('Enter the 3 nuber for comprision\n'))
if x>y:
    if x>z:
        print('X  first is gretest number %7.3f\n'%x)
elif y>x:
    if y>z:
        print('Y second is gretest %7.3f\n'%y)
        
else:
    print('Z third is gretest nuber %7.3f\n'%z)
    
#power of 2 on give number using lambda function
a = int(input('Enter the value of power\n'))
b=2
c=list (map(lambda x: b**x,range(a)))
print(c)

#
c=[]
a=int(input('Entetr the number of elements\n'))
for b in range(a):
   
    b= int (input('Enter the number  '+ str(b+1)))
    c.append(b)
print(c)
c.sort()
print(c)
print('%3i is greatest number\n'%c[-1])
'''

'''
If the number is 1, return 1. Otherwise, 
return the number multiplied by the factorial of the number
minus 1
    
    :param x: The number to find the factorial of
    :return: The factorial of 3 is 6
'''
def factorial(x):
    '''This is a recursive function to find the factorial of an integer'''
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
num=int(input('Enter the nuber to get the factorial value\n'))
fact=factorial(num)
print("The factorial of",num,"is",fact)