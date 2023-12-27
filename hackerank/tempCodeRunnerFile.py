for i in range(nofstudents):
    for j in range(i,i+1):
        if cla[i[score]]>cla[i+1[score]]:
            temp=cla[i[score]]
            cla[i[score]]=cla[i+1[score]]
            cla[i+1[score]]=temp
print(cla)       