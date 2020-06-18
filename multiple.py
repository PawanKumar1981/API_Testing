class A:
    def m1(self):
        print("class A method")
class B:
    def m2(self):
        print("class B method")
    def m3(self):
        print("class B method M3")
class C(A,B):
    pass
cobj = C()
cobj.m1()
cobj.m2()
cobj.m3()
