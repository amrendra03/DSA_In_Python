
a=int(input('Enter the first number for the find HCF\n'))
c={0}
b=int(input('Enter the second number \n'))
d={0}
for i in range(2,a+1):
    e=a%i
    if e==0:
        c.add(i)
print(c)
for j in range(2,b+1):
    f=b%j
    if f==0:
        d.add(j)
print(d)

g={0}
g=c.intersection(d)
print(max(g))



    

