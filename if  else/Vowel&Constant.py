def vowel(s):
    if(s=='a'):
        print("Entered leter is vowel")
    elif(s=='e'):
        print("Entered leter  is vowel")
    elif(s=='i'):
        print("Entered leter is vowel")
    elif(s=='o'):
        print("Entered leter is vowel")
    elif(s=='u'):
        print("Entered leter is vowel")
    else:
        print("Entered leter is constant")
    print(s,end="")

a=input("Enter the leter to check it is vowel or constant ")
vowel(a)