def add(a,*b):
    #c=a+b--We cannot give the this type because b is tuble
    #print(c) so we use tuple
    v=a
    for i in b:
        v=v+i
    print(v)

add(2,3,4,5,5,66,8,7)