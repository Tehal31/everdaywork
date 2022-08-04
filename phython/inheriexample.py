class Human:  
    def speak(self):  
        print("Human Speaking")  
#child class Man inherits the base class Human  
class Man(Human):  
    def voice(self):  
        print("Man saying hello")  
d = Man()  
d.voice()  
d.speak()  