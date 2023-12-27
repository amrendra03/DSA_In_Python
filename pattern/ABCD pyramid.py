n=5
A=64
for i in range(n):
    for j in range(i):
        print(chr(A+i),end=' ')
    print()