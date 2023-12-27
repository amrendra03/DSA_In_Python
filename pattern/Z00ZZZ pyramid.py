n = 5
# range used -1 to start from highest value to lowest is 0
for i in range (n,0,-1):
    for j in range (i):
        if i%2==0:
         print("Z",end='')
        else:
            print("0",end='')
    print()
