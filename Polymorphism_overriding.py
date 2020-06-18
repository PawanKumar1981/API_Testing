#overriding the variables
class parent:
    name="Pavan"
class child(parent):
    pass
c= child()
print(c.name)

#overriding the methods
class Bank:
    def rateofintrest(self):
        return 3
    def m1(self):
        print("Hello")
class ICICI(Bank):
    def rateofintrest(self):
        return 20
Ic=ICICI()
print(Ic.rateofintrest())

