N=int(input())
a=[]
for i in range(0,N):
    c=input().split()
    if c[0]=="print":
        print('\n',a)
    elif c[0]=="insert":
        a.insert(int(c[1]),int(c[2]))
    elif c[0]=="remove":
        a.remove(int(c[1]))
    elif c[0]=="append":
        a.append(int(c[1]))
    elif c[0]=="sort":
        a.sort()
    elif c[0]=="pop":
        a.pop()
    elif c[0]=="reverse":
        a.reverse() 