class A:
    a,b=10,20
    def m1(self,x,y):
        print(x+y)
        print(self.a+self.b)
class B(A):
    i,j=100,200
    def m2(self):
        print(self.i+self.j)

bobj=B()
bobj.m1(2,3)
bobj.m2()