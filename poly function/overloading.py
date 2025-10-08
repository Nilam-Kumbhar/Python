class animal():
    def sound(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)  
        else:
            print("no operation possible")    
a=animal()
a.sound(2,3)          
a.sound(1,2,3)