from array import *
arr=array('i',[])
n=int(input("Enter the store value"))
for i in range(n):
    x=int(input("Enter the values"))
    arr.append(x)
print(arr)



arr1=array('i',[])
i=0
delete=int(input("Enter the index"))
for i in arr:
    if delete==i:

        continue
    else:
        arr1.append(i)
print(arr1)