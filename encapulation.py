#declare and accessing private variables and methods
class Myclass:
    __a=10
    def __praviateMethod(self,a):
        self.__a=a
        print("I am praviate")
    def acessvariable(self,a):

        self.__praviateMethod(a)
        print(self.__a)
mc=Myclass()
mc.acessvariable(25)
