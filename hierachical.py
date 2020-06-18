class A:
    def methodofclass_A(self):
        print("i am mehtod calss A")
class B(A):
    def methodofclass_B(self):
        print("i am method of class B")
class C(A):
    def methodofclass_C(self):
        print("i am method of class C")
cobj=C()
cobj.methodofclass_A()
cobj.methodofclass_C()
bobj=B()
bobj.methodofclass_A()
bobj.methodofclass_B()
