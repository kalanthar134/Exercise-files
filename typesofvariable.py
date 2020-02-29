#####Instance method

# noinspection PyStatementEffect
class Class():
    school='Usa'  #class variable

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):# Instance Method
        return (self.m1+self.m2+self.m3)/3

    def get(self):#Accessor
        return self.m2
    def set(self):
        #Modular


        return self.m1
    @classmethod
    def school1(cls):
        return cls.school
    @staticmethod
    def info():
        print("I'm born with wings")
s1=Class(22,33,44)
s2=Class(22,44,55)
print(s1.avg())
print(s1.school,s2.avg())
print(s1.get())
print(s1.set())
print(Class.school1())
print(Class.info())