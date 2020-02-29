pos=-1
def search(list,n):
    i=0
    while i<len(list):
    #for i in list:
     #   if i<len(list):
            if list[i]==n:
                globals()['pos']=i
                return True
            i=i+1
    return False



list=[1,2,3,4,55,6,7,78,11,99,12]
n=12
if search(list,n):
    print("Found Here",pos)

else:
    print("not Found",)