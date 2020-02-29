class computer:



    def confiq(self):
        print("My computer's name is ",self.name)
        print("My computer's procerssor are ",self.kp)
        print("Year",self.year)

    def __init__(self,name,p,year):
        self.kp = p
        self.name=name
        self.year=year

        print("indent")

c1=computer("Lenovo",'i5','2018')
c2=computer("dell",'i3','2019')
c3=computer('Apple','i9','2021')
c1.confiq()
c2.confiq()
c3.confiq()