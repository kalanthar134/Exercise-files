from array import*
n=array('i',[])
w=int(input("Enter the index"))
for i in range(w):
       value=int(input("Enter the values"))
       n.append(value)
print(n)

dele=int(input("Enter the index you want delete"))
arr=array('i',[])

for e in n:
    if dele==e:
        continue
    else:
        arr.append(e)
print(arr)