# Write a Python program to calculate the sum of a list of numbers.

def sums(n, i, coun):
    if i == len(n):
        return coun
    else:
        coun = coun + n[i]

        return sums(n, i + 1,coun)


l = [2, 4, 1, 5, 8, 90]
counts = 0
print(sums(l, 0, counts))
