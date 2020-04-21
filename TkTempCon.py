'''Kyle Deniel De Castro  Group03 AS3#1'''

from tkinter import *
 
def f2c():
    res=((float(fahrenheit.get())-32)*5)/9
    F2C.set(res)
def c2f():
    res=((float(celsius.get())*9)/5)+32
    C2F.set(res)

master = Tk()
master.configure(background ='black')
master.title("Temperature Converter")

F2C=DoubleVar(master, value=0.0);
C2F=DoubleVar(master, value=32.0);

 
Label(master, text="Fahrenheit", fg='white', font ='helvetica',bg = 'black').grid(row=0,column=0, sticky=W)
Label(master, text="Celsius", fg='white', font ='helvetica', bg ='black').grid(column=1, row=0, sticky=W)



 
fahrenheit = Entry(master, textvariable=C2F)
celsius = Entry(master, textvariable=F2C )
 
fahrenheit.grid(row=1, column=0, sticky =W)
celsius.grid(row=1, column=1)
 
b = Button(master, text=">>>>", command=f2c, bg='LightSkyBlue3', fg='white', font ='helvetica')
b.grid(row=3, column=0,columnspan=1, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
b = Button(master, text="<<<<", command=c2f, bg='LightSkyBlue3', fg='white', font ='helvetica')
b.grid(row=3, column=1,columnspan=1, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 

master.mainloop()