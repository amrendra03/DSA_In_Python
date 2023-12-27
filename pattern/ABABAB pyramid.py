n=10
A=65
for i in range(n):
    #If i range is not even print A otherwise print B
    # here we not use the i+1 because 0 is even number
    for j in range(i):
        if i%2!=0:
          print(chr(A),end='')
        else:
            print(chr(A+1),end='')
    print()