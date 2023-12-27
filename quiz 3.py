# change this value for a different output
my_str = str(input())
print("Given string is = ",)
# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str =my_str[::-1]
 
# check if the string is equal to its reverse
if rev_str==my_str:
   print("It is palindrome")
else:
   print("It is not palindrome")