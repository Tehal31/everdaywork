class A:
    a=10
    b=20
    def __init__(self):
        print('a')
    def ml(self):
        print('ml')
class b(A):
    a=4
    b=5
    def ml (self):
        print('B class')

ob=b()
ob.ml()                    