n=10
A=65
for i in range (n):
    #we use i + 1 to avoid Null loop means loop not run if range zero
    for j in range (i+1):
        print(chr(A),end='')
    A+=2
    print()
