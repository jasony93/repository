from tkinter import *

root = Tk()

e = Entry(root)
e.grid(row=3, column=0)


def myClick():
    myLabel = Label(root, text=e.get(), width=50)
    myLabel.grid(row=4, column=0)


myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Jason!")
# myLabel = Label(root)
myButton = Button(root, text="Enter your name", command=myClick)


myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=2, column=0)


root.mainloop()
