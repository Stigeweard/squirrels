# Simple calculator so I don't have to strain my fingers using the actual
# physical calculator that is always on the desk next to me

from tkinter import *

#8.25% sales tax calculator

def sales_tax(p):
    ans = float(p)+(float(p)*0.0825)
    return str("%.2f" % ans)
#########################################
#30% mark up calculator

def mark_up30(p):
    ans = float(p)+(float(p)*.3)
    return str("%.2f" % ans)
#########################################
#10% mark up calculator

def mark_up10(p):
    ans = float(p)+(float(p)*.1)
    return str("%.2f" % ans)
#########################################

def three_percent(p):
    ans = float(p)*.03
    return str("%.2f" % ans)

def evaluate1(event):
    res.configure(text = "With Tax: " + str(eval(sales_tax(e1.get()))))
    #e1.delete(0,END) # I kind of like the number left there...
def evaluate2(event):
    res.configure(text = "30% Markup: " + str(eval(mark_up30(e2.get()))))
    #e2.delete(0,END)
def evaluate3(event):
    res.configure(text = "10% Markup: " + str(eval(mark_up10(e3.get()))))
    #e3.delete(0,END)
def evaluate4(event):
    res.configure(text = "3%: " + str(eval(three_percent(e4.get()))))
   
master = Tk()

Label(master, text="Price(tax):").grid(row=0)
Label(master, text="Price(30%):").grid(row=1)
Label(master, text="Price(10%):").grid(row=2)
Label(master, text="3% SS:").grid(row=3)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.bind("<Return>", evaluate1)
e1.grid(row=0, column=1)
e2.bind("<Return>", evaluate2)
e2.grid(row=1, column=1)
e3.bind("<Return>", evaluate3)
e3.grid(row=2, column=1)
e4.bind("<Return>", evaluate4)
e4.grid(row=3, column=1)

res = Label(master)
res.grid(row=4, column=1)

master.mainloop()



