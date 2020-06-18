from abc import ABC,abstractmethod
class A(ABC):
    def __init__(self,value):
        self.value=value
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
       pass
class B(A):
    def m1(self):
        print("i am implemented now m1")
        print(self.value)

    def m2(self):
        print("i am implemented now m2")
obj=B(100)
obj.m1()
obj.m2()