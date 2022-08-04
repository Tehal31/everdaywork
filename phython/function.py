def sum( ):
   print(10+10)
sum()

def disp(a,b,c):
    d=a+b+c
    print(d)
disp(23,56,79)

def multiple(*k):
   print(k[0])

multiple(45,46,47)  

def names(**d):
    print(d['a2'])
  
names(a1='tehal',a2='sukhman',a3='nimish')    

def nw(a,b):
    c=a+b
    return(c)
res=nw(23,89)
print(res)    