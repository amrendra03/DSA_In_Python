a =100
b = 100
if (a<b):
    c=a
    for i in range(c+1,-1,-1):
        if(i>1):
          if(a%i==0 and b%i==0):
                print('HCF is',i)
                break
else:
    c = b
    for i in range(c+1,-1,-1):
        if(i>1):
          if (a % i == 0 and b % i == 0):
               print('HCF is',i)
               break