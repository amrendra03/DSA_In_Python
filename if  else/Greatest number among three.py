def largest_number(k,l,m):
    if(k>=l):
        if(k>m):
            print("Greater number is k",k)
        elif(k>l):
            print("Greater number is k",k)
        else:
            print("Greater number is m",m)
    elif(l>=k):
        if (l > m):
            print("Greater number is k", l)
        elif (l > l):
            print("Greater number is k", l)
        else:
            print("Greater number is m", m)
    else:
        print("Greater number is m",m)

a=int(input("Enter number a "))
b=int(input("Enter number b "))
c=int(input("Enter number c "))
largest_number(a,b,c)