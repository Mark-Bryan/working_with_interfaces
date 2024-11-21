from tkinter import *

myWindow = Tk()
myWindow.title("My First Desktop Program")

Label = Label(myWindow, text = "Hello, World!")
Label.pack(padx=200, pady=25)

def changeBg():
    myWindow.configure(bg = 'magenta')

simpleBtn = Button(myWindow, text = "Do Something", command=changeBg)
simpleBtn.pack(padx=50, pady=25)
myWindow.mainloop()