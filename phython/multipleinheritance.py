
class A():
    def f1(self):
        print('A')
class B():
    def f2(self):
        print('B')
class c(A,B):
    def f3(self):
        print('C')


ob=c()
ob.f1()
ob.f2()
ob.f3()
