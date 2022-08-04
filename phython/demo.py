from tkinter import *
import tkinter as tk
ab=Tk()

 
name = Label(ab,text = "Name").grid(row = 0, column = 0)  
e1 = Entry(ab).grid(row = 0, column = 1)  
roll_no= Label(ab,text = "roll_no").grid(row = 1, column = 0)  
e2 = Entry(ab).grid(row = 1, column = 1)

password = Label(ab,text = "Password").grid(row = 2, column = 0)  
e3 = Entry(ab).grid(row = 2, column = 1)  
  
gender = Label(ab,text = "gender").grid(row = 3, column = 0)  
var = IntVar()
Radiobutton(ab, text="Male",variable=var, value=1).place(x=50,y=65)
Radiobutton(ab, text="Female", variable=var, value=2).place(x=50,y=85)

b1 =Button(ab,text="login",fg="red")
b1.place(x=50,y=110)


ab.mainloop()