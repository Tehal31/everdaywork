class pm:  
    def speak(self):  
        print("pm Speaking")  
  
class minister(pm):  
    def listen(self):  
        print("minister listening")  

class mla(minister):  
    def work(self):  
        print("mla is doing work")  
d = mla()  
d.listen()  
d.speak()  
d.work()  