from tkinter import *

window = Tk()
window.title("Final Exam")
window.geometry("240x150")


lbl1 = Label(window,text="Input Value A : ")
lbl1.grid(row = 1,column = 0)

aentry = Entry(window)
aentry.grid(row=1,column=1)


lbl2 = Label(window,text="Input Value B : ")
lbl2.grid(row=2,column=0)

bentry = Entry(window)
bentry.grid(row=2, column=1)


lbl4 = Label(window, text="Input Value C : ")
lbl4.grid(row=4,column=0)

centry = Entry(window)
centry.grid(row=4, column=1)


def Average():
    lowentry.delete(0,"end")
    number1=int(aentry.get())
    number2=int(bentry.get())
    number3=int(centry.get())
    answer = min(number1, number2, number3)
    lowentry.insert(END,str(answer))


btn1=Button(window,text="Find",width=10,command=Average)
btn1.grid(row=5,column=1)


lbl5 = Label(window,text = "Lowest Value : ")
lbl5.grid(row=6,column = 0)

lowentry = Entry(window)
lowentry.grid(row=6, column = 1)


window.mainloop()