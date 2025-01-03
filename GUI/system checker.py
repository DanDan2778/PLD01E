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

"""import tkinter as tk
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

window.mainloop()"""

"""import tkinter as tk


class App:
    def __init__(self, root):
        self.window = root
        self.inputs = []  # List to keep track of the dynamically created input fields
        self.input_count = 0  # To keep track of how many inputs we have added
        self.create_button()

    def create_button(self):
        # Create a button that adds a new input field when clicked
        add_button = tk.Button(self.window, text="Add Input", command=self.add_input)
        # Initially place the button below the inputs
        add_button.place(x=50, y=30 + self.input_count * 40)
        self.add_button = add_button  # Keep a reference to the button

    def add_input(self):
        # Define x, y positions for the new input field
        x = 50
        y = 30 + self.input_count * 40  # Adjust y to position inputs below each other

        # Create a new Entry widget (input field)
        new_input = tk.Entry(self.window)
        new_input.place(x=x, y=y)
        self.inputs.append(new_input)  # Store the input field in the list

        self.input_count += 1  # Increment input count to adjust the next y-position

        # Reposition the button below the newly added input
        self.add_button.place(x=50, y=30 + self.input_count * 40)  # Adjust y to be below the inputs


# Create the Tkinter root window
root = tk.Tk()
app = App(root)

root.mainloop()
"""
"""import tkinter as tk

class App:
    def __init__(self, root):
        self.window = root
        self.inputs = []  # List to keep track of the dynamically created input fields
        self.input_count = 0  # To keep track of how many inputs we have added
        self.button_x = 15  # Fixed x position of the button
        self.button_y = 342  # Initial y position for the button
        self.input_y = 382  # Starting y position for the input fields below the button
        self.create_button()  # Create the initial button

        # List of labels for the textboxes
        self.input_labels = [
            "Subject Code", "Course Description", "Section",
            "Time", "Day", "Room", "Units"
        ]

    def create_button(self):
        # Create the button at the defined fixed y position (342)
        add_button = tk.Button(self.window, text="Add More Subjects", command=self.add_input)
        add_button.place(x=self.button_x, y=self.button_y)
        self.add_button = add_button  # Keep a reference to the button

    def add_input(self):
        # Limit the number of subjects to 10
        if self.input_count >= 10:
            # Disable the button when 10 subjects have been added
            self.add_button.config(state=tk.DISABLED)
            return  # Exit the function if limit is reached

        # Create labeled input fields at the fixed y position, then move down
        for i, label in enumerate(self.input_labels):
            # Define x and y positions for each pair of input fields
            y_pos = self.input_y + i * 40  # Adjust y position for each label and input pair
            x_pos = 15 if i % 2 == 0 else 300  # Alternate x position for each pair (two per row)

            # Create the label for each input field
            label_widget = tk.Label(self.window, text=label)
            label_widget.place(x=x_pos, y=y_pos)

            # Create the Entry widget for each input field with placeholder text
            entry_widget = tk.Entry(self.window)
            entry_widget.insert(0, label)  # Set the placeholder text
            entry_widget.place(x=x_pos + 100, y=y_pos)  # Place input next to the label

            # Bind the focus events to clear/add placeholder text
            entry_widget.bind("<FocusIn>", self.clear_placeholder)
            entry_widget.bind("<FocusOut>", self.add_placeholder)

            # Append entry widget to the inputs list
            self.inputs.append(entry_widget)

        # Update input_count to adjust for the next set of inputs
        self.input_count += len(self.input_labels)

        # Update the starting y position for the next set of input fields
        self.input_y = self.input_y + len(self.input_labels) * 40  # Increment y position

    def clear_placeholder(self, event):
        """#Clear the placeholder text when the user clicks inside the entry field.
"""
        entry = event.widget
        if entry.get() == entry.get().strip():  # If the text is the placeholder
            entry.delete(0, tk.END)

    def add_placeholder(self, event):
        """#Add the placeholder text back if the user leaves the entry field empty.
"""
        entry = event.widget
        if not entry.get():  # If the field is empty, set the placeholder
            placeholder = "Subject Code" if entry == self.inputs[0] else "Course Description"  # Adjust this for each field
            entry.insert(0, placeholder)


# Create the Tkinter root window
root = tk.Tk()
app = App(root)

root.mainloop()"""

"""# LINE
import tkinter as tk


def vertical_line(window, x_loc, y_loc, x, y, length, color):
    # Create a canvas to draw the line
    canvas = tk.Canvas(window, width=10, height=length, bg="white", bd=0)
    canvas.place(x=x_loc, y=y_loc)

    # Draw a vertical line using the canvas widget
    canvas.create_line(5, y, 5, length, fill=color, width=2)


# Create the main window
root = tk.Tk()
root.title("Vertical Line Example")

# Call the vertical_line function to draw the line
vertical_line(root, 10, 50,10, 10, 500, "black")

# Start the Tkinter main loop
root.mainloop()
"""
"""import tkinter as tk

def create_scrollable_ui():
    # Create the main window
    root = tk.Tk()
    root.title("Scrollable UI Example")

    # Create a Canvas widget
    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the canvas to work with the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a scrollable frame within the canvas
    scrollable_frame = tk.Frame(canvas)

    # Add the scrollable frame to the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor=tk.NW)

    # Populate the frame with widgets (buttons as an example)
    for i in range(50):  # Add 50 buttons as an example of content
        button = tk.Button(scrollable_frame, text=f"Button {i+1}")
        button.pack(pady=5)

    # Update the scroll region of the canvas
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Start the Tkinter event loop
    root.mainloop()

# Call the function to create the UI
create_scrollable_ui()"""


# Calendar Textbox

"""import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar

def show_calendar(event):
    def select_date():
        selected_date = cal.get_date()
        entry.delete(0, tk.END)  # Clear the entry box
        entry.insert(0, selected_date)  # Insert the selected date
        cal_window.destroy()

    # Create a new top-level window for the calendar
    cal_window = tk.Toplevel(root)
    cal_window.title("Select a Date")

    # Create and display a calendar widget
    cal = Calendar(cal_window, selectmode='day', date_pattern='yyyy-mm-dd')
    cal.pack(padx=10, pady=10)

    # Button to select the date
    btn_select = tk.Button(cal_window, text="Select Date", command=select_date)
    btn_select.pack(pady=10)

def show_message():
    messagebox.showinfo("Date Selected", f"You selected: {entry.get()}")

# Main window
root = tk.Tk()
root.title("Tkinter Calendar Example")

# Create an Entry widget (Textbox) for showing selected date
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Bind the Entry widget to the function that shows the calendar when clicked
entry.bind("<Button-1>", show_calendar)  # Trigger the calendar on click

# Button to show the selected date
btn_show = tk.Button(root, text="Show Selected Date", command=show_message)
btn_show.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
"""

# Button Popup Window

"""import tkinter as tk


def open_new_window():
    # Create a new top-level window
    new_window = tk.Toplevel()
    new_window.title("New Window")

    # Set the dimensions of the new window
    new_window.geometry("300x200")

    # Add a label in the new window
    label = tk.Label(new_window, text="This is the new window!")
    label.pack(pady=50)


# Create the main window
root = tk.Tk()
root.title("Main Window")

# Set the dimensions of the main window
root.geometry("400x300")

# Create a button in the main window that opens the new window
button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
"""


"""# DESTROY NEW WINDOW
import tkinter as tk


def open_new_window():
    # Create a new top-level window
    new_window = tk.Toplevel()
    new_window.title("New Window")
    new_window.geometry("300x200")

    # Add a label in the new window
    label = tk.Label(new_window, text="This is the new window!")
    label.pack(pady=20)

    # Function to close the window
    def close_window():
        new_window.destroy()  # This closes the new window

    # Add a button in the new window that closes it
    close_button = tk.Button(new_window, text="Close Window", command=close_window)
    close_button.pack(pady=20)


# Create the main window
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

# Create a button in the main window that opens the new window
open_button = tk.Button(root, text="Open New Window", command=open_new_window)
open_button.pack(pady=50)

# Start the Tkinter event loop
root.mainloop()
"""

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

class DatePickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Date Picker Example")

        # Create the Entry widget (text box) where the selected date will be displayed
        self.date_entry = ttk.Entry(root, width=20)
        self.date_entry.grid(row=0, column=0, padx=10, pady=10)

        # Create a Button to open the calendar
        self.calendar_button = ttk.Button(root, text="Select Date", command=self.show_calendar)
        self.calendar_button.grid(row=0, column=1, padx=10, pady=10)

        # Placeholder for calendar popup
        self.calendar_popup = None

    def show_calendar(self):
        # Create the calendar popup if it doesn't already exist
        if self.calendar_popup is None or not self.calendar_popup.winfo_exists():
            self.calendar_popup = Calendar(self.root, selectmode='day', date_pattern='yyyy-mm-dd')
            self.calendar_popup.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

            # Bind the calendar selection event
            self.calendar_popup.bind("<<CalendarSelected>>", self.on_date_selected)

    def on_date_selected(self, event):
        # Get the selected date from the calendar and insert it into the entry widget
        selected_date = self.calendar_popup.get_date()
        self.date_entry.delete(0, tk.END)  # Clear current entry text
        self.date_entry.insert(0, selected_date)  # Insert the selected date

        # Hide the calendar after selecting the date
        self.calendar_popup.grid_forget()

# Create the main tkinter window
root = tk.Tk()
app = DatePickerApp(root)

# Start the tkinter event loop
root.mainloop()
