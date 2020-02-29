


def count(list1):
    even=0
    odd=0
    for i in list1:
        if i%2!=0:
            odd=odd+1

        else:
            even=even+1
    return odd,even
even,odd=count([1,2,2,34,6,5,7,8,9,9])
print(even)
print(odd)


