import tkinter as tk
import gui_design as gui

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.insert(0, placeholder)
        self.bind("<FocusIn>", self.clear_placeholder)
        self.bind("<FocusOut>", self.restore_placeholder)

    def clear_placeholder(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)

    def restore_placeholder(self, event):
        if self.get() == "":
            self.insert(0, self.placeholder)


# Create the main window
root = tk.Tk()
root.title("Textbox with Placeholder")

# Create an instance of PlaceholderEntry
entry = PlaceholderEntry(root, placeholder="Enter your text here")
entry.pack(padx=10, pady=10)


gui = gui.GuiDesign(root)
gui.textbox_design2(100, 100)
# Start the Tkinter main loop
root.mainloop()

