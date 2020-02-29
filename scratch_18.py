def fib(n):
    x=0
    y=1
    if n<0:
        print("Enter the valid number")
    #elif n==1:
     #   print(x)
      #  print(y)
    else:
        print(x)
        print(y)
        for i in range(2,n):
            c=x+y
            x=y
            y=c
            if c>100:

                break
            print(c,end=" ")
        print()


fib(100)