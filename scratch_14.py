from array import*
ar =array('i',[71,18,5,27,9])

print(ar[len(ar)-1]," is the maximum value")

#Palindrome
name=input("Enter the value")
name=name.casefold()
reverse=reversed(name)
for i in range(len(name)):
    if list(name)==list(reverse):
        print("Palindrome")
        break
else:
       print("Not a palindrome")


