# Www.HackerRank.com → wWW.hACKERrANK.COM

a = str(input())
b = ''
for i in a:
    if (i.isupper()) == True:
        b += (i.lower())
    elif (i.islower()) == True:
        b += (i.upper())
    else:
        b += i
print(b)

'''
str= "Hello, World!"
a=[a for a in str]

for i in range(0,len(a)):
    az=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    AZ=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if a[i]>=az[0] and a[i]<=az[25]:
        az=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        AZ=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for j in range(len(az)):  
            if a[i]==az[j]:
                a[i].append(az[j])
    elif a[i]>AZ[0] and a[i]<=AZ[25]:
        az=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        AZ=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for j in range(len(AZ)):  
            if a[i]==AZ[j]:
                a[i].append(AZ[j])
    else:
       a[i]=a[i]


print(a[i])
'''
