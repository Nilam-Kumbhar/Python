class A:
    x=10
class B:
    y=20
class C(A,B):
    def sum(self):
        print(A.x+B.y)     
c=C()        
c.sum()