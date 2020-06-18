class A:
    def __init__(self):
        print("i am class A constractor")
    def m1(self):
        print("i am method m1 of class A")
class B(A):
      def __init__(self):
          print("i am class B constractor")
         # super().__init__() # one approch
          A.__init__(self)

objb= B()

