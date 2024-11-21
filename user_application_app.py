from tkinter import *
from tkinter import messagebox
import os

def saveUserInfo():
    # get values from inputs
    userInfo = {}
    userInfo['firstName'] = fnEntry.get()
    userInfo['lastName'] = lnEntry.get()
    userInfo['dob'] = DOBEntry.get()
    userInfo['password'] = pwEntry.get()
    
    # write information to a file
    userFile = open(f"{userInfo['firstName']}_{userInfo['lastName']}.txt", "w")
    
    for line in userInfo:
        userFile.write(f"{line}:{userInfo[line]}\n")
        
    userFile.close()
    
    # provide feedback once complete
    messagebox.showinfo("Success!", "Information has been saved successfully")

def loadUserInfo():
    fName = fnEntry.get()
    lName = lnEntry.get()
    pword = pwEntry.get()
    
    if not os.path.exists(f"{fName}_{lName}.txt"):
        errorTitle = "No User Found"
        errorMessage = f"Could not find information for {fName} {lName}"
        messagebox.showerror(errorTitle, errorMessage)
    else:
        # Create a dictionary to hold user information
        userInfo = {}
        
        # Parse the file for user information
        with (open(f"{fName}_{lName}.txt", "r") as userFile):
            for line in userFile:
                keyValue = line.split(":")
                userInfo[keyValue[0]] = keyValue[1].strip()
                
        # Check if the password provided matches the password saved
        if not pword == userInfo["password"]:
            messagebox.showerror("Password Incorrect", "Your password didn't match. Please try again.")
        else:
            messageTitle = f"{fName} {lName} Account"
            messageContent = f"Account found for {fName} {lName}"
            messagebox.showinfo(messageTitle, messageContent)
        

mainWindow = Tk()
mainWindow.title("User Registration App")

# Add a label to the application with instructions for the user
# Complete the form and press submit to register a new user.

instructions = Label(mainWindow, text="Complete the form and press submit to register a new user.")
instructions.pack(padx=20, pady=10)

# Create the frame for the first name components
fnFrame = Frame(mainWindow)
# Create the components to be added to the frame
fnLabel = Label(fnFrame, text="First Name")
fnEntry = Entry(fnFrame)

# Add the components to the frame before adding the frame to the window
fnLabel.pack(side=LEFT)
fnEntry.pack(side=RIGHT)
# Components can't be changed after they have been rendered so the order is important!
fnFrame.pack(padx=20, pady=10)

# Do the same for the other components
lnFrame = Frame(mainWindow)
lnLabel = Label(lnFrame, text="Last Name")
lnEntry = Entry(lnFrame)

lnLabel.pack(side=LEFT)
lnEntry.pack(side=RIGHT)
lnFrame.pack(padx=20, pady=10)

DOBFrame = Frame(mainWindow)
DOBLabel = Label(DOBFrame, text="Date of Birth")
DOBEntry = Entry(DOBFrame)

DOBLabel.pack(side=LEFT)
DOBEntry.pack(side=RIGHT)
DOBFrame.pack(padx=20, pady=10)

pwFrame = Frame(mainWindow)
pwLabel = Label(pwFrame, text="Password")
pwEntry = Entry(pwFrame, show="*", )

pwLabel.pack(side=LEFT)
pwEntry.pack(side=RIGHT)
pwFrame.pack(padx=20, pady=10)

# Create a frame to group the action buttons
actionsFrame = Frame(mainWindow)

# Change the saveBtn container from the main window to the actions frame
saveBtn = Button(actionsFrame, text='Save User Information', command=saveUserInfo)
saveBtn.pack(side=RIGHT, padx=20, pady=10)

# Create a new Load button and add to the actions frame
loadBtn = Button(actionsFrame, text='Load User Information', command=loadUserInfo)
loadBtn.pack(side=LEFT, padx=20, pady=10)

actionsFrame.pack()

mainWindow.mainloop()