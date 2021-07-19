from tkinter import *
import tkinter
from functools import partial


def addition(num1,num2):
    a=int(num1.get())
    b=int(num2.get())
    result=a+b
    res.set(str(result))
    
def sub(num1,num2):
    a=int(num1.get())
    b=int(num2.get())
    result=a-b
    res.set(str(result))
    
def multi(num1,num2):
    a=int(num1.get())
    b=int(num2.get())
    result=a*b
    res.set(str(result))
    
def div(num1,num2):
    a=int(num1.get())
    b=int(num2.get())
    result=a/b
    res.set(str(result))



box=Tk()
box.minsize(400,400)
box.maxsize(600,600)
box.title('Form')

num1=tkinter.StringVar()
num2=tkinter.StringVar()
res=tkinter.StringVar()



label=Label(box,text="Enter the 1st No.")
label.place(x=10,y=30)
e=Entry(box,text="",textvariable=num1)
e.place(x=105,y=30)

label1=Label(box,text="Enter the 2nd no.")
label1.place(x=10,y=55)
e=Entry(box,text="",textvariable=num2)
e.place(x=105,y=55)

add =partial(addition,num1,num2) 
minus =partial(sub,num1,num2)
multiplication =partial(multi,num1,num2)
division =partial(div,num1,num2)


btn1=Button(box,text='+',width=5,height=3, command=add)  #create button
btn1.place(x=40,y=150)

btn2=Button(box,text='-',width=5,height=3, command=minus)  
btn2.place(x=90,y=150)

btn3=Button(box,text='/',width=5,height=3, command=division)  
btn3.place(x=140,y=150)

btn4=Button(box,text='*',width=5,height=3,command=multiplication)  
btn4.place(x=190,y=150)

output=Label(box,text="Enter the 2nd no.")
output.place(x=10,y=220)
e=Entry(box,text="",textvariable=res)
e.place(x=115,y=220)


box.mainloop()
