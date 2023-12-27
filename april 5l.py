'''s=int(input('Enter the marks\n'))
if s<50:
    print('\nstudent is fail')
print('\nstudent is pass')
#qestion 
a=8
b=9
if a>b or a==b:
    print('a greater then b and a equal to b')
else: 
    print('check again')

#question 2
male=int (input('Enter the number of male\n'))
female=int (input('Enter the number of female\n'))
if male>female:
    print('male number is greter the female in Engneering\n')
else:
print('female is more than male in Engneerging\n')
#check number is positive or negative or zero
a=float(input('Enter the number to check it is positive or negative ,Zero\n'))
if a>0:
    print('a is Positive')
elif a<0:
    print('a is negative\n')
elif a==0:
    print('a is equal to zero\n')

'''
course=str(input('Enter you course to get access in seminar\n'))
course1="Btech"
course2="btech"
course3="B tech"
if course==course1:
    print('You can  get in\n')
elif course==course2:
    print('You can enter\n')
elif course==course3:
    print('You can get\n')