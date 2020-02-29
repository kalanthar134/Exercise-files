nums=[12,9,33,56,89,89]
for num in nums:
    if(num%3==0):
        print(num)
        break
else:
    print("Fuckoff")

j=9
for i in range(2,j):
    if j%i==0:
        print("Not Prime number")
        break
else:
    print("prime number")