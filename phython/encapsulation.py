class Person:


    def __init_(self, name, age=0):
       self.name = name
       self.age = age
    def diaplay(self):
        print (self.name)
        print (self.age)

Person =Person( 'Dev', 30)

Person.display()

print(Person.name)
print(Person.age)