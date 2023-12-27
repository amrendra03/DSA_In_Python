# a=["i am amrendra","hello my friends"]
# l=[]
# for k in range(len(a)):
#     b=0
#     for i in a[k]:
#         size=0
#         for j in i:
#             if i!=' ':
#                 size+=1
#         b+=size
#     l.append(b)
# print(l)

# counting the number of words in a sentence

a=["i am amrendra","hello my friends Ydav"]
l=[]
for i in a:
    t=list(i.split())
    print(t)
    l.append(len(t))
print(l)


