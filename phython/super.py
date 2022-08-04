class A:
    a=10
    b=20
    def __init__(self,a,b):
        print('a')
    def ml (self):
        print('ml')
class b(A):
    a=4
    b=5
    def __init__(self):
        super().__init__(12,12)
    def m2(self):

        super().ml()
        print(self.a,self.b)
        print(super().a,super().b)

ob=b()
ob.ml()
ob.m2()                    