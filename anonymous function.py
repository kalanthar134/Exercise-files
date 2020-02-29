#def name(a):
#    return a*a
#result=name(5)
#print(result)
#We can simply declare the anonymous function by lamda
#f=lambda a:a*a
#result=f(6)
#print(result)

#z=lambda a,b:a+b
#result=z(9,11)
#print(result)


from functools import reduce
def add1(a,b):
    return a+b
nums=[2,3,4,5,6,7,89,8]
evens=list(filter(lambda n:n%2==0,nums))
double=list(map(lambda n:n*2,evens))
add=reduce(add1,double)
print(evens)
print(double)
print(add)




