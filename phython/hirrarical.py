class A():
    def f1(self):
        print('A')
class B(A):
    def f2(self):
        print('B')
class c(A):
    def f3(self):
        print('C')


ob=c()
ob.f1()

ob.f3()
ob=B()
ob.f1()
ob.f2()