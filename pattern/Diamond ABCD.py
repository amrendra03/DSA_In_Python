n = 5
A = 65
for i in range(n-1):
    for j in range(i, n-1):
        print(" ", end='')
    for j in range(i):
        print(chr(A+i), end='')
    for j in range(i+1):
        print(chr(A+i), end='')
    print()
A = 69
for i in range(n):
    for j in range(i):
        print(" ", end='')
    for j in range(i, n-1):
        print(chr(A+i), end='')
    for j in range(i, n):
        print(chr(A+i), end='')
    print()
    