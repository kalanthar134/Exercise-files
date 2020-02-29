from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):

    def process(self):
        print("It is running")
class Desktop(Computer):

    def process(self):
        print("It is Desktop")
class programmer:
    def work(self,c1):
        print("Clearing bugs")
        c1.process()

#c2=Computer()
c1=Desktop()
pro=programmer()
c3=Laptop()
#c3.process()
pro.work(c1)


