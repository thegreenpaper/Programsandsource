#!/bin/python3
from tkinter import *

root = Tk()
root.title("calc")
e = Entry(root, width=25, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
#e.insert(0, "Enter your name:")
posible = False
gnumbers = []

## Buttons
def bprus(number):
    athe = e.get()
    e.delete(0, END)
    e.insert(0, str(athe) + str(number))

def bclear():
    e.delete(0, END)
    gnumbers.clear()
    global posible
    posible = True

#def bplus():
#    numbers = int(e.get())
#    gnumbers.append(numbers)
#    e.delete(0, END)

def bq():
    ans = eval(e.get())
    e.delete(0, END)
    e.insert(0, ans)

## IDK how to fix this so i made varables
#brus1 = bprus(1)
#brus2 = bprus(2)
#brus3 = bprus(3)
#brus4 = bprus(4)
#brus5 = bprus(5)
#brus6 = bprus(6)
#brus7 = bprus(7)
#brus8 = bprus(8)
#brus9 = bprus(9)
#brus0 = bprus(0)
## Nevermind

## Buttons

b1 = Button(root, text="1", padx=30, pady=10, command=lambda: bprus(1))
b2 = Button(root, text="2", padx=30, pady=10, command=lambda: bprus(2))
b3 = Button(root, text="3", padx=30, pady=10, command=lambda: bprus(3))
b4 = Button(root, text="4", padx=30, pady=10, command=lambda: bprus(4))
b5 = Button(root, text="5", padx=30, pady=10, command=lambda: bprus(5))
b6 = Button(root, text="6", padx=30, pady=10, command=lambda: bprus(6))
b7 = Button(root, text="7", padx=30, pady=10, command=lambda: bprus(7))
b8 = Button(root, text="8", padx=30, pady=10, command=lambda: bprus(8))
b9 = Button(root, text="9", padx=30, pady=10, command=lambda: bprus(9))
b0 = Button(root, text="0", padx=30, pady=10, command=lambda: bprus(0))
bplus = Button(root, text="+", padx=29, pady=10, command=lambda: bprus("+"))
bminus = Button(root, text="-", padx=32, pady=10, command=lambda: bprus("-"))
bdevide = Button(root, text="/", padx=10, pady=54, command=lambda: bprus("/"))
bmultiply = Button(root, text="*", padx=9, pady=54, command=lambda: bprus("*"))
bdot = Button(root, text=".", padx=32, pady=10, command=lambda: bprus("."))
bobracket = Button(root, text="(", padx=31, pady=10, command=lambda: bprus("("))
bcbracket = Button(root, text=")", padx=31, pady=10, command=lambda: bprus(")"))


becool = Button(root, text="=", padx=29, pady=31, command=bq)
back = Button(root, text="|AC|", padx=20, pady=10, command=bclear)

## Show buttons
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)
bdot.grid(row=4, column=1)

bplus.grid(row=4, column=2)
becool.grid(row=5, column=2, rowspan=2)
back.grid(row=5, column=0)

bobracket.grid(row=6, column=0)
bminus.grid(row=5, column=1)
bcbracket.grid(row=6, column=1)

bdevide.grid(row=1, column=3, rowspan=3)
bmultiply.grid(row=4, column=3, rowspan=3)

root.mainloop()
