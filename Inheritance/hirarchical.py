class A:
    a=10
class B(A):
    def show(self):
        print(A.a)  
class B1(A):
    def show(self):
        print(A.a)
b=B()
b1=B1()
b.show()
b1.show()