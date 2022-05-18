from tkinter import *


window = Tk()
window.title("Calculator")
window.geometry("410x400")
window.configure(bg="pink")


ent = Entry(window, bd=6, borderwidth=20, bg="pink", font="Arial 20 bold", justify=RIGHT,width=24)
ent.grid(row=0,column=0, sticky='W')


def nine():
        ent.insert("end","9")
def eight():
        ent.insert("end","8")
def seven():
        ent.insert("end","7")
def six():
        ent.insert("end","6")
def five():
        ent.insert("end","5")
def four():
        ent.insert("end","4")
def three():
        ent.insert("end","3")
def two():
        ent.insert("end","2")
def one():
        ent.insert("end","1")
def zero():
        ent.insert("end","0")
def point():
        ent.insert("end",".")
def plus():
        ent.insert("end","+")
def minus():
        ent.insert("end","-")
def multiply():
        ent.insert("end","*")
def divide():
        ent.insert("end","/")
def equals():
        if ent.get() == "":
                ent.insert("end","error")
        elif ent.get()[0] == "0":
                ent.delete(0,"end")
                ent.insert("end","error")
        else:
                res = ent.get()
                res = eval(res)
                ent.insert("end"," = ")
                ent.insert("end",res)
def clear():
        ent.delete(0,"end")

btnerase = Button(window, text="C", font="Century 20 bold", command=clear,width=15)
btnerase.grid(row=2, column=0, sticky='W',padx=16, pady=5)

btnadd = Button(window, text="+", font="Century 20 bold", command=plus, width=5)
btnadd.grid(row=2, column=0, sticky='W',padx=300, pady=5)

btnsub = Button(window, text="-", font="Century 20 bold",command=minus,width=5)
btnsub.grid(row=3, column=0, sticky='W',padx=300)

btnmulti = Button(window, text="*", font="Century 20 bold",command=multiply,width=5)
btnmulti.grid(row=4,column=0, sticky='W',padx=300,pady=5)

btndiv = Button(window, text="/", font="Century 20 bold", command=divide, width=5)
btndiv.grid(row=5,column=0, sticky='W',padx=300)

btneql = Button(window, text="=", font="Century 20 bold", command=equals, width=5)
btneql.grid(row=6,column=0, sticky='W',padx=300, pady=5)

btnpnt = Button(window, text=".", font="Century 20 bold", command=point, width=5)
btnpnt.grid(row=6,column=0, sticky='W',padx=199, pady=5)

btn0 = Button(window, text="0", font="Century 20 bold", command=zero, width=10)
btn0.grid(row=6,column=0, sticky='W',padx=9, pady=5)

btn1 = Button(window, text="1", font="Century 20 bold", command=one, width=5)
btn1.grid(row=5,column=0, sticky='W',padx=9)

btn2 = Button(window, text="2", font="Century 20 bold", command=two, width=5)
btn2.grid(row=5,column=0, sticky='W',padx=110)

btn3 = Button(window, text="3", font="Century 20 bold", command=three, width=5)
btn3.grid(row=5,column=0, sticky='W',padx=210)

btn4 = Button(window, text="4", font="Century 20 bold", command=four,width=5)
btn4.grid(row=4,column=0, sticky='W',padx=9,pady=5)

btn5 = Button(window, text="5", font="Century 20 bold", command=five,width=5)
btn5.grid(row=4,column=0, sticky='W',padx=110,pady=5)

btn6 = Button(window, text="6", font="Century 20 bold", command=six, width=5)
btn6.grid(row=4,column=0, sticky='W',padx=210,pady=5)

btn7 = Button(window, text="7", font="Century 20 bold",command=seven, width=5)
btn7.grid(row=3, column=0, sticky='W', padx=9)

btn8 = Button(window, text="8", font="Century 20 bold", command=eight,width=5)
btn8.grid(row=3, column=0, sticky="W", padx=110)

btn9 = Button(window, text="9", font="Century 20 bold", command=nine, width=5)
btn9.grid(row=3,column=0, sticky='W',padx=210)


window.mainloop()