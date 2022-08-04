def fun(a,b) :
   try:
      c=(a+b)//(a-b)
   except ZeroDivisionError:
      print("can't divide ")
   else:
      print(c)
fun(3.0,4.0)
fun(4.0,4.0)