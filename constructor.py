# defalt constructor
# class demo1:
#     var1="hello"
#     var2="welcome"
#     def __init__(self):
#         print("hi",self.var1)
#         print("hi",self.var2)
# obj=demo1()
    
# Parameterized Constructor
class demo1:
    var1="hello"
    var2="welcome"
    def __init__(self,x,y,z):
        print("hi",self.var1)
        print("hi",self.var2)
        self.sum=x+y
        self.mul=x*z
        self.eq=x+y-z
obj=demo1(2,3,4)
print("sum:",obj.sum)
print("mul:",obj.mul)
print("equation(x+y-z):",obj.eq)