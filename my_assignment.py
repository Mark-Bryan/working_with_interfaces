from tkinter import *
from tkinter import messagebox
import os



required_fields = {
    "firstName": "First Name",
    "lastName": "Last Name",
    "emailAddress": "Email Address",
    "password": "Password",
}

window = Tk()
window.title('User Information')

user_info = {}

for field in required_fields.keys():
    user_info[field] = input(f"Enter your {required_fields[field]}: ")

user_file = open(f"{user_info['emailAddress']}.txt", "w")

for prop in user_info.keys():
    user_file.write(f"{prop}:{user_info[prop]}\n")

user_file.close()

def save_user_info():
    user_info = {}
    for field in required_fields.keys():
        user_info[field] = user_info[field].get() 

    if any(value == "" for value in user_info.values()):
        messagebox.showerror("Error", 'All fields are required.')
        return

def retrieve_user_info():
    user_Email = user_info["emailAddress"].get()
    fileName = (f"{user_Email}.txt")


    if os.path.exists(user_file):
        file = open(user_file, 'r')
        info = user_file.read()
        messagebox.showinfo("User Information", info)
    else:
        messagebox.showinfo('No information has been found for that email address')



saveButton = Button(window, text = "Save User Information", command = save_user_info)
saveButton.pack(padx=30, pady=25)


retrieveButton = Button(window, text = "Retrieve User Information", command = retrieve_user_info)
retrieveButton.pack(padx=30, pady=25)


window.mainloop()

# while True:
#     print("\nSelect what to do with your information: ")
#     print('1: Save user information')
#     print("2: Retrieve information from a user")
#     choice = input("Enter your choice(1 or 2): ")

#     if choice == '1':
#         save_user_info()
#     elif choice == '2':
#         retrieve_user_info()
#     break