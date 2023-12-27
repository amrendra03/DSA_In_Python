def factorial(n,i):
    if n==1:
        return i
    else:
        i=i*n
        return factorial(n-1,i)

n=5
i=1
print(factorial(n,i))
