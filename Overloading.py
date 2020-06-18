class A:
    def printname(self,name=None):
        if(name is not None):
            print("name is",name)
        else:
            print("Hello")
obja =A()
#obja.printname()
obja.printname("Pavan")