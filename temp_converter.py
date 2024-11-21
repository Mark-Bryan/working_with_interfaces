from tkinter import*
from interface_functions import celsius_to_fahrenheit


mainWindow = Tk()
mainWindow.title('Temperature Converter')

instructions = Label(mainWindow, text="Enter a temperature in Celsuis to convert to Fahrenheit")
instructions.pack(padx=50, pady=50)

resultMessage = StringVar(value=f"Result will display here")
resultLabel = Label(mainWindow, textvariable= resultMessage)

inputFrame = Frame(mainWindow)
tempInput = Entry(inputFrame)

def convertTemp():

    temp = tempInput.get()
    fahrenheit = celsius_to_fahrenheit(int(temp))
    print(fahrenheit)
    resultMessage.set(f"{temp} Celsius is {fahrenheit} Fahrenheit")

converBtn = Button(inputFrame, text="Convert", command=convertTemp)

tempInput.pack(side=LEFT)
converBtn.pack(side=RIGHT)
inputFrame.pack(padx=20, pady=20)
resultLabel.pack(pady=20)

mainWindow.mainloop()