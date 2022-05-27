from tkinter import *

window = Tk()
window.title("Lab 6 (Semestral Grade Calculator)")
window.geometry("375x175")

lbl1 = Label(window,text="Grades")
lbl1.grid(row = 1,column = 2)

lbl2 = Label(window,text="Prelims:")
lbl2.grid(row=2,column=1)

prlmentry = Entry(window)
prlmentry.grid(row=3,column=1,padx=4)

lbl3 = Label(window,text="Midterms:")
lbl3.grid(row=4,column=1)

mdtentry = Entry(window)
mdtentry.grid(row=5, column=1,padx=4)

lbl4 = Label(window, text="Finals: ")
lbl4.grid(row=6,column=1)

fnlentry = Entry(window)
fnlentry.grid(row=7, column=1,padx=4)

def Average():
    sementry.delete(0,"end")
    number1=int(prlmentry.get())
    number2=int(mdtentry.get())
    number3=int(fnlentry.get())
    answer=(number1+number2+number3)/3
    sementry.insert(END,str(answer))

lbl5 = Label(window,text = "  Calculate  ")
lbl5.grid(row=4,column = 2)

btn1=Button(window,text="=",width=4, command=Average)
btn1.grid(row=5,column=2)

lbl6 = Label(window,text = "Semester:")
lbl6.grid(row=4,column = 3)

sementry = Entry(window)
sementry.grid(row=5, column = 3)

window.mainloop()
