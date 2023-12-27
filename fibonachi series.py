n=int (input("ENter the number for fabonacci series"))
x=1
y=0
z=0
temp=[1]
while(n>1):
    z=x+y
    temp.append(z)
    print(z)
    y=x
    x=z
    n-=1
print(temp)
    

