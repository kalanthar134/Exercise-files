
from array import *
x=array('i',[])
w=int(input("Enter the number of values "))

for i in range(w):
    z=int(input("Enter the values"))
    x.append(z)
print(x)

l=int(input("Enter the value search for"))

j=0
for e in x:
    if e==l:
        print(j)
        break
    j=j+1

