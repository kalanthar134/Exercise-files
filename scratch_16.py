def greet(list1):
        more=0
        less=0
        for i in range(len(list1)):
                if len(list[i])>5:
                     more=more+1

                elif len(list[i])<5:


                        less+=1
        return more,less
x=int(input("Enter the search value"))
list=[]
for j in range(x):

        list.append(input("Enter the names"))

more,less=greet(list)
print(more)
print(less)


