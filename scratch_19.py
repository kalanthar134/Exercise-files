def factoril(n):
    a=1

    for i in range(1,n+1):
        a=a*i


    return a


x=6
result=factoril(x)
print(result)
