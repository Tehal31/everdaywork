class A:
    def __init__(self):
        print('a')
    def ml (self):
        print('ml')
class b(A):
    a=4
    b=5
    def m2(self):
        print(a,b)

ob=b()
ob.m1()
ob.m2()                    