nlist=[]
klist=[]
"Number of students"
no=int(input())
"input name and score"
for i in range(no):
    name=str(input())
    score=float(input())
    klist.append(score)
    nlist.append([score,name])
"sorting Float number score"
klist=sorted(klist,key=lambda x: float(x))
"Removing duplicates score number and copy in res list"
res = []
for i in klist:
    if i not in res:
        res.append(i)
print(res)
"Take second lowest scoer"
b=float(res[1])
"Searching elements in main list by the value of b"
mlist=[]
l=len(nlist)
for i in nlist:
  if b in nlist[i]:
     print(nlist[i])

        




'''nlist.sort()
print(nlist)
l=len(nlist)
b=nlist[1][0]
print(b)
'''




'''for j in range(1,l):
    if nlist[j][0]==b:
        print(nlist[j][1])
     '''   
