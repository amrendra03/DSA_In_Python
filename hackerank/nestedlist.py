'''from unicodedata import name


no=int(input())
nestl=[]
for i in range(no):
    name=str(input())
    score=float(input())
    nestl.append([name,score])

nestl.sort()

print(sorted(nestl))
'''
from os import remove


def Sort(nlist):
    l = len(nlist)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (nlist[j][1] > nlist[j + 1][1]):
                tempo = nlist[j]
                nlist[j]= nlist[j + 1]
                nlist[j + 1]= tempo
    return nlist
  
'''Input by user'''
nlist =[]
no=int(input())
for i in range(no):
    name=str(input())
    score=float(input())
    nlist.append([name,score])

Sort(nlist)

'''Print second gretest score'''
l=len(nlist)
if nlist[-1][-1]==nlist[-2][-2]:

 for j in range(0,l):
     for k in range(0,l-i-1):
      if nlist[k][1] != nlist[k + 1][1]:
         nlist.pop([k][1])
 print(nlist)
else:
     print(nlist[-1])
       

