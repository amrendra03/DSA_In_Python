n=int(input())
if n%2!=0:
    print("weird")
elif n==28 or n%2==0:
    if n in range (2,5):
        print("Not weird")
    elif n in range (6,21):
        print("weird")
    elif n>20:
        print("Not weird")

        