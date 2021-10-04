#===================================================================
#    Purpose:   Practice in using TKinter module
#===================================================================

from tkinter import *

# Main winow class
class WidgetExample(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.guielement()        

    def guielement(self):

        # Initialize and use grid layout manager
        self.grid()
        self.entryVariable = StringVar()
        self.entry = Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=0, sticky="EW")
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here.")

        # Add button to the grid
        button = Button(self, text=u"Click Here!", command=self.OnButtonClick)
        button.grid(column=1, row=0)

        # Define a lable and variable storage
        self.labelVariable = StringVar()
        label = Label(self, textvariable=self.labelVariable, anchor="w", fg="green", bg="black")
        label.grid(row=0, column=0)
        self.labelVariable.set(u"Our Python GUI, type something")

        # Reorganize grid
        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, END)

    # Button click event handler
    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get() + " (Button was clicked)")
        self.entry.focus_set()
        self.entry.selection_range(0, END)

    # Enter key pressed event handler
    def OnPressEnter(self, event):
            self.labelVariable.set(self.entryVariable.get() + " (ENTER was pressed")
            self.entry.focus_set()
            self.entry.selection_range(0, END)

# Main function with message loop
if __name__ == "__main__":
    app = WidgetExample(None)
    app.title("Python GUI Application")
    app.mainloop()