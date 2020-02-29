num1=[12,1,14,51,6,8,8]
print(num1[0])
num1[1]=333
print((num1))
names=['kalanthar','hussain','Mohamed']
print(names)
values=[0,0.1,'kalanthar']
print(type(values[2]))
mil=[num1,names,values]
print(mil)

num1.append(100)
print(num1)
num1.insert(2,33)
print(num1)
num1.append(3)
print(num1.pop(2))
del num1[2:5]
print(num1)
num1.sort()
print(num1)