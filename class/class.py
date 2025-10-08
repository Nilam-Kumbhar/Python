# class demo:
#     print("hi my name is nilam.")
# obj=demo()    

# specifier public,private,protected
class demo1:
    def __init__(self,x,y,z):
        self.__name=x
        self._div=y
        self.rollno=z
        print("name:",self.__name )
        print("Div:",self._div)
        print("roll no:",self.rollno)
obj=demo1("nilam","A",31)


