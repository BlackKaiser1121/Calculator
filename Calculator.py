import tkinter
from tkinter import *
win = Tk()

def Addition():
    num1, num2 = int(txtbx1Num.get()), int(txtbx2Num.get())
    result = num1 + num2
    output.config(text=str(result))
def Subtraction():
    num1, num2 = int(txtbx1Num.get()), int(txtbx2Num.get())
    result = num1 - num2
    output.config(text=str(result))
def Multiplication():
    num1, num2 = int(txtbx1Num.get()), int(txtbx2Num.get())
    result = num1 * num2
    output.config(text=str(result))
def Division():
    num1, num2 = int(txtbx1Num.get()), int(txtbx2Num.get())
    result = num1 / num2
    output.config(text=str(result))
def FloorDiv():
    num1, num2 = int(txtbx1Num.get()), int(txtbx2Num.get())
    result = num1 // num2
    output.config(text=str(result))
def Expo():
    num1, num2 = int(txtbx1Num.get()), int(txtbx2Num.get())
    result = num1 ** num2
    output.config(text=str(result))
def Modulo():
    num1, num2 = int(txtbx1Num.get()), int(txtbx2Num.get())
    result = num1 % num2
    output.config(text=str(result))
win.title("Baquirin's Calculator"), win.geometry("650x300+570+250"), win.configure(background='#D3D3D3')
lbl1Title = Label(win, text="Baquirin's Calculator", font=("Arial", 20, 'bold'), bg="#D3D3D3")
lbl1Title.place(x=190, y=10)
lbl1Num, lbl2Num, outputTxt, output = Label(win, text="First Number", font=("Arial", 20, "bold"), bg="#D3D3D3"), Label(win, text="Second Number", font=("Arial", 20, "bold"), bg="#D3D3D3"), Label(win, text="Output", font=("Arial", 20, "bold"), bg="#D3D3D3"), Label(win, text="", font=("Arial", 20), bg="#D3D3D3")
lbl1Num.place(x=10, y=50), lbl2Num.place(x=10, y=100), outputTxt.place(x=480, y=50), output.place(x=480, y=100)
txtbx1Num, txtbx2Num = Entry(win, width=15, font=("Arial", 15)), Entry(win, width=15, font=("Arial", 15))
txtbx1Num.place(x=270, y=53), txtbx2Num.place(x=270, y=105)
addBut, subBut, mulBut, divBut, FdivBut, exBut, modBut = Button(win, text=("+"), command= Addition, bg="#171717", fg="#D3D3D3", font=("bold", 10)), Button(win, text="-", command=Subtraction, bg="#171717", fg="#D3D3D3", font=("bold", 10)), Button(win, text="*", command=Multiplication, bg="#171717", fg="#D3D3D3", font=("bold", 10)), Button(win, text="/", command=Division, bg="#171717", fg="#D3D3D3", font=("bold", 10)), Button(win, text="//", command=FloorDiv, bg="#171717", fg="#D3D3D3", font=("bold", 10)), Button(win, text="**", command=Expo, bg="#171717", fg="#D3D3D3", font=("bold", 10)), Button(win, text="%", command=Modulo, bg="#171717", fg="#D3D3D3", font=("bold", 10))
addBut.config(height=5,width=8), subBut.config(height=5,width=8), mulBut.config(height=5,width=8), divBut.config(height=5,width=8), FdivBut.config(height=5,width=8), exBut.config(height=5,width=8), modBut.config(height=5,width=8)
addBut.place(x=25, y=180), subBut.place(x=115, y=180), mulBut.place(x=200, y=180), divBut.place(x=290, y=180), FdivBut.place(x=375, y=180), exBut.place(x=460, y=180), modBut.place(x=550, y=180)
win.mainloop()
