import tkinter as tk
from tkinter import ttk  # For creating themed widgets

win = tk.Tk()  # Create an instance of the Tk class
win.title("Python GUI")  # Set the title of the window

win.resizable(0, 0)  # Disable resizing the GUI

aLabel = ttk.Label(win, text='Enter a name:')  # Create a named Label instance to be used later
aLabel.grid(column=0, row=0)  # Create a Label object and pass the win instance


def clickMe():  # Called when the button is clicked
    ttk.Label(text='Hello ' + aTextBox.get()).grid(column=0, row=2)


aButton = ttk.Button(win, text='Click Me!',
                     command=clickMe)  # Creates a button and binds an event handler to handle the click

aButton.configure(state='disabled')  # Disables the button
aButton.grid(column=1, row=1)

aTextBox = tk.StringVar()  # Create a placeholder to hold the value being entered in the textbox
textEntered = ttk.Entry(win,
                        textvariable=aTextBox)  # Create a textbox and set the variable name which will hold the value

textEntered.focus()  # Focuses on the textbox i.e. adds a blinking cursor to add focus

textEntered.grid(column=0, row=1)

win.mainloop()  # The event which makes the window appear on screen
