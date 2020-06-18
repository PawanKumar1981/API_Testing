class A:
    def add(self,a,b):
        print('supperclass',a+b)

class B(A):
    def mul(self,a,b):
        print('derived class',a*b)
class C(B):
    def multilevel(self):
        print("i am derived class")
aobj =A()
aobj.add(3,5)
bobj =B()
bobj.add(4,7)
bobj.mul(2,4)
cobj= C()
cobj.add(1,3)
cobj.mul(2,3)
cobj.multilevel()


