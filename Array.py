from array import *
vals= array('i',[2,3,4,5,1,2,3,4])
print(sorted(vals))
for i in range(len(vals)):
    print(i)

new=array(vals.typecode,(a for a in vals))
for b in new:
     print(b)

##Factorial

n=int(input("Enter the value"))
f=1

for i in range(1,n+1):
        f=f*i
print(f)

n = input("Enter a number: ")
factorial = 1
if int(n) >= 1:
   for i in range (1,int(n)+1):
    factorial = factorial * i
print("Factorail of ",n , " is : ",factorial)
n = int(input('Enter the number '))
count = 1

for i in range(1, n+1):

    count = count * i

print(count)


