class A:
    a,b=10,20
    def m1(self,a,b):
        print(self.a+self.b)

class B(A):
    a,b=100,200
    def m2(self):
        print("M2",self.a+self.b)
        print( super().a + super().b)

bobj=B()
bobj.m1(2,3)
bobj.m2()