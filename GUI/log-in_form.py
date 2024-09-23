import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Log-in Form")
window.geometry("340x440")
window.configure(bg='#555555')

frame = tkinter.Frame(window, bg='#555555')

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Success", "Access Granted")
        print("Access Granted")
    else:
        print("Access Denied")
        messagebox.showerror("Error", "Access Denied")

# Creating Widgets
login_label = tkinter.Label(frame, text="Login", bg='#555555', font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg='#555555', font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password", bg='#555555', font=("Arial", 16))
username_entry = tkinter.Entry(frame)
password_entry = tkinter.Entry(frame, show='*')
login_button = tkinter.Button(frame, text="Log-in", bg='blue', fg='white', font=("Arial", 16), command=login)


# Displaying Widgets to Screen

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=35)
username_label.grid(row=1, column=0, pady=25)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0, pady=25)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2, pady=25)

frame.pack()

window.mainloop()
