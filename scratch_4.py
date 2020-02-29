for i in range(1,5):
    for j in range(i,5):
        print(j,end="")
    print()

x,y='ABCD','PQR'
for i in range(4):
    print(x[:i+1]+y[i:])