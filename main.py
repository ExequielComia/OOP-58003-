from tkinter import *

window = Tk()
window.title("The Program that Finds the Largest Number")
window.geometry("400x150+20+10")

def findLargest():

    L = []
    L.append(eval(conOfent1.get()))
    L.append(eval(conOfent2.get()))
    L.append(eval(conOfent3.get()))
    conOfLargest.set(max(L))

lbl1 = Label(window,text = "Enter the first value :")
lbl1.grid(row=1, column = 0,sticky=W)
conOfent1 = StringVar()
ent1 = Entry(window,bd=3,textvariable=conOfent1)
ent1.grid(row=1, column = 1)

lbl2 = Label(window,text = "Enter the second value :")
lbl2.grid(row=2, column=0)
conOfent2=StringVar()
ent2 = Entry(window,bd=3,textvariable=conOfent2)
ent2.grid(row=2,column=1)

lbl3 = Label(window,text="Enter the third value :")
lbl3.grid(row=3,column =0, sticky=W)
conOfent3 = StringVar()
ent3 = Entry(window,bd=3,textvariable=conOfent3)
ent3.grid(row=3, column=1)

btn1 = Button(window,text = "Find the largest value",command=findLargest)
btn1.grid(row=4, column = 1)

lbl4 = Label(window,text="The largest value :")
lbl4.grid(row=5,column=0,sticky=W)
conOfLargest = StringVar()
ent4 = Entry(window,bd=3,state="readonly",textvariable=conOfLargest)
ent4.grid(row=5,column=1)


mainloop()
