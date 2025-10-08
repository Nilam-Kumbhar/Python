class A:
    def show_a(self):
        print("hii")
class B(A):
    def show_b(self):
        print("hello")  
class C():
    def show_c(self):
        print("i am")
class D(B,C,A):
    def show_d(self):
        print("nilam")
d=D()
d.show_a()
d.show_b()
d.show_c()
d.show_d()

