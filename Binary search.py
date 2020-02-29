pos=0
def search(list1,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list1[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list1[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
list=[11,2,34,5,6,7,8,11]
list1=sorted(list)
n=11

if search(list1,n):
    print("Found at ",pos+1)
else:
    print("Not Found")