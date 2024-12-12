"""from tkinter import *
from tkinter import font

root = Tk()
root.title('Font Families')
fonts=list(font.families())
fonts.sort()

def populate(frame):
    '''Put in the fonts'''
    listnumber = 1
    for i, item in enumerate(fonts):
        label = "listlabel" + str(listnumber)
        label = Label(frame,text=item,font=(item, 16))
        label.grid(row=i)
        label.bind("<Button-1>",lambda e,item=item:copy_to_clipboard(item))
        listnumber += 1

def copy_to_clipboard(item):
    root.clipboard_clear()
    root.clipboard_append("font=('" + item.lstrip('@') + "', 12)")

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas = Canvas(root, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

root.mainloop()"""

"""import tkinter as tk
from tkinter import ttk

tk_umlauts = ['odiaeresis', 'adiaeresis', 'udiaeresis', 'Odiaeresis', 'Adiaeresis', 'Udiaeresis', 'ssharp']


class AutocompleteEntry(ttk.Entry):
    """""" Subclass of :class:`ttk.Entry` that features autocompletion.

    To enable autocompletion use :meth:`set_completion_list` to define
    a list of possible strings to hit.
    To cycle through hits use down and up arrow keys.""""""
    def __init__(self, master=None, completevalues=None, **kwargs):
        """"""Create an AutocompleteEntry.

        :param master: master widget
        :type master: widget
        :param completevalues: autocompletion values
        :type completevalues: list
        :param kwargs: keyword arguments passed to the :class:`ttk.Entry` initializer""""""
        ttk.Entry.__init__(self, master, **kwargs)
        self._completion_list = completevalues
        self.set_completion_list(completevalues)
        self._hits = []
        self._hit_index = 0
        self.position = 0

    def set_completion_list(self, completion_list):
        """"""Set a new auto completion list

        :param completion_list: completion values
        :type completion_list: list""""""
        self._completion_list = sorted(completion_list, key=str.lower)  # Work with a sorted list
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)

    def autocomplete(self, delta=0):
"""""" Autocomplete the Entry.

        :param delta: 0, 1 or -1: how to cycle through possible hits
        :type delta: int""""""
        if delta:  # need to delete selection otherwise we would fix the current position
            self.delete(self.position, tk.END)
        else:  # set position to end so selection starts where textentry ended
            self.position = len(self.get())
        # collect hits
        _hits = []
        for element in self._completion_list:
            if element.lower().startswith(self.get().lower()):  # Match case-insensitively
                _hits.append(element)
        # if we have a new hit list, keep this in mind
        if _hits != self._hits:
            self._hit_index = 0
            self._hits = _hits
        # only allow cycling if we are in a known hit list
        if _hits == self._hits and self._hits:
            self._hit_index = (self._hit_index + delta) % len(self._hits)
        # now finally perform the auto completion
        if self._hits:
            self.delete(0, tk.END)
            self.insert(0, self._hits[self._hit_index])
            self.select_range(self.position, tk.END)

    def handle_keyrelease(self, event):
        """""" Event handler for the keyrelease event on this widget.

        :param event: Tkinter event""""""
        if event.keysym == "BackSpace":
            self.delete(self.index(tk.INSERT), tk.END)
            self.position = self.index(tk.END)
        if event.keysym == "Left":
            if self.position < self.index(tk.END):  # delete the selection
                self.delete(self.position, tk.END)
            else:
                self.position -= 1  # delete one character
                self.delete(self.position, tk.END)
        if event.keysym == "Right":
            self.position = self.index(tk.END)  # go to end (no selection)
        if event.keysym == "Down":
            self.autocomplete(1)  # cycle to next hit
        if event.keysym == "Up":
            self.autocomplete(-1)  # cycle to previous hit
        if event.keysym == "Return":
            self.handle_return(None)
            return
        if len(event.keysym) == 1 or event.keysym in tk_umlauts:
            self.autocomplete()

    def handle_return(self, event):
        """"""Function to bind to the Enter/Return key so if Enter is pressed the selection is cleared.

        :param event: Tkinter event""""""
        self.icursor(tk.END)
        self.selection_clear()

    def config(self, **kwargs):
        """"""Alias for configure""""""
        self.configure(**kwargs)

    def configure(self, **kwargs):
        """"""Configure widget specific keyword arguments in addition to :class:`ttk.Entry` keyword arguments.""""""
        if "completevalues" in kwargs:
            self.set_completion_list(kwargs.pop("completevalues"))
        return ttk.Entry.configure(self, **kwargs)

    def cget(self, key):
        """"""Return value for widget specific keyword arguments""""""
        if key == "completevalues":
            return self._completion_list
        return ttk.Entry.cget(self, key)

    def keys(self):
        """"""Return a list of all resource names of this widget.""""""
        keys = ttk.Entry.keys(self)
        keys.append("completevalues")
        return keys

    def __setitem__(self, key, value):
        self.configure(**{key: value})

    def __getitem__(self, item):
        return self.cget(item)"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Simulating a simple employee database using a dictionary
employee_data = {
    "2023200846": {
        "first_name": "Daniel",
        "last_name": "Agustin",
        "middle_name": "A",
        "civil_status": "Single",
        "qualified_dependent_status": "Student",
        "paydate": "2024-12-15",
        "employee_status": "single",
        "designation": "Manager",
        "department": "HR"
    },
    "2023200847": {
        "first_name": "Jane",
        "last_name": "Smith",
        "middle_name": "B",
        "civil_status": "Single",
        "qualified_dependent_status": "No",
        "paydate": "2024-12-10",
        "employee_status": "Contractual",
        "designation": "Developer",
        "department": "IT"
    },
    # Add more employee records as needed
}


class GuiDesign:
    def __init__(self, window):
        self.window = window

    def frames(self, x, y, width, height, color):
        frame = Frame(self.window, bg=color, width=width, height=height)
        frame.place(x=x, y=y)

    def image_design(self, image_path, x, y, width, height):
        try:
            img = Image.open(image_path)
            img = img.resize((width, height), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            label = Label(self.window, image=photo)
            label.image = photo
            label.place(x=x, y=y)
        except Exception as e:
            print(f"Error loading image: {e}")

    def title_design(self, x, y, title):
        title_label = Label(self.window, text=title, font=('Arial', 16), bg='white')
        title_label.place(x=x, y=y)

    def label_design(self, x, y, text):
        label = Label(self.window, text=text, font=('Arial', 12), bg='white')
        label.place(x=x, y=y)

    def textbox_design1(self, x, y, state="normal"):
        textbox = Entry(self.window, font=('Arial', 10), state=state)
        textbox.place(x=x, y=y)
        return textbox

    def button_design(self, x, y, text, bg, fg, hover_color, border_width):
        button = Button(self.window, text=text, bg=bg, fg=fg, font=('Arial', 10), width=20, height=2, relief=SOLID)
        button.place(x=x, y=y)
        return button


# Create the main window
window = tk.Tk()
window.title("Payroll System")
window.geometry('700x900')

lbl = Label(window, bg='white', width=1540, height=900)
lbl.place(x=1, y=1)

gui = GuiDesign(window)
image = 'C:\\Users\\danie\\Desktop\\repository\\PLD01E\\Laboratory 6\\profile.jpg'
gui.frames(15, 15, 670, 850, 'white')
# Profile picture
gui.image_design(image, 40, 70, 200, 200)
gui.title_design(39, 40, 'Employee Basic Info')

# First Name (non-editable)
gui.label_design(400, 80, 'First Name: ')
first_name_entry = gui.textbox_design1(530, 80, state="readonly")

# Last Name (non-editable)
gui.label_design(400, 120, 'Last Name: ')
last_name_entry = gui.textbox_design1(530, 120, state="readonly")

# Middle Name (non-editable)
gui.label_design(400, 160, 'Middle Name: ')
middle_name_entry = gui.textbox_design1(530, 160, state="readonly")

# Civil Status (non-editable)
gui.label_design(400, 200, 'Civil Status: ')
n = StringVar()
civil_status_combobox = ttk.Combobox(window, width=20, textvariable=n, state="readonly")
civil_status_combobox.place(x=530, y=200)

# Qualified Dependent Status (editable)
gui.label_design(400, 240, 'Qualified Dependent ')
gui.label_design(400, 265, 'Status: ')
status_entry = Entry(window, width=20, font=('Arial', 10))
status_entry.place(x=530, y=240)

# Paydate (editable)
gui.label_design(400, 300, 'Paydate: ')
paydate_entry = gui.textbox_design1(530, 300)

# Employee Status (non-editable)
gui.label_design(400, 340, 'Employee Status: ')
employee_status_combobox = ttk.Combobox(window, width=20, textvariable=n, state="readonly")
employee_status_combobox.place(x=530, y=340)

# Designation (non-editable)
gui.label_design(400, 380, 'Designation: ')
designation_entry = gui.textbox_design1(530, 380, state="readonly")

# Left Side
# Employee Number (editable)
gui.label_design(40, 300, 'Employee Number: ')
employee_number_entry = gui.textbox_design1(170, 300)


# Search Employee button
def search_employee():
    emp_number = employee_number_entry.get()
    if emp_number in employee_data:
        employee = employee_data[emp_number]

        # Update the GUI with the employee data
        first_name_entry.config(state="normal")  # Make it editable to update
        first_name_entry.delete(0, tk.END)
        first_name_entry.insert(0, employee["first_name"])
        first_name_entry.config(state="readonly")  # Make it non-editable after updating

        last_name_entry.config(state="normal")
        last_name_entry.delete(0, tk.END)
        last_name_entry.insert(0, employee["last_name"])
        last_name_entry.config(state="readonly")

        middle_name_entry.config(state="normal")
        middle_name_entry.delete(0, tk.END)
        middle_name_entry.insert(0, employee["middle_name"])
        middle_name_entry.config(state="readonly")

        civil_status_combobox.set(employee["civil_status"])

        status_entry.delete(0, tk.END)
        status_entry.insert(0, employee["qualified_dependent_status"])

        paydate_entry.delete(0, tk.END)
        paydate_entry.insert(0, employee["paydate"])

        employee_status_combobox.set(employee["employee_status"])

        designation_entry.config(state="normal")
        designation_entry.delete(0, tk.END)
        designation_entry.insert(0, employee["designation"])
        designation_entry.config(state="readonly")
    else:
        messagebox.showerror("Employee Not Found", "No employee found with that employee number.")


search_button = gui.button_design(170, 340, 'Search Employee', 'red', 'white', 'blue', 2)
search_button.config(command=search_employee)

# Department
gui.label_design(40, 400, 'Department: ')
department_entry = gui.textbox_design1(170, 400)

window.mainloop()
