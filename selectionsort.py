def sort(num):
    for i in range(len(num)):
        minpos=i
        for j in range(i,len(num)):
          if num[j]<num[minpos]:
              minpos=j
        temp=num[i]
        num[i]=num[minpos]
        num[minpos]=temp
        print(num)

num=[5,2,1,3,4,5,6,7]
sort(num)
print("Final Iteration :",num)