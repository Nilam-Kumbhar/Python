class demo1:
    var1="hello"
    var2="welcome"
    def __del__(self):
        print("hi",self.var1)
        print("hi",self.var2)
obj=demo1()