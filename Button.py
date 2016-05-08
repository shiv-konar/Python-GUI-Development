import tkinter as tk
from tkinter import ttk  #For creating themed widgets
win = tk.Tk()  #Create an instance of the Tk class
win.title("Python GUI")  #Set the title of the window

win.resizable(0, 0)  #Disable resizing the GUI

aLabel = ttk.Label(win, text = 'A Label')  #Create a named Label instance to be used later
aLabel.grid(column = 0, row = 0)  #Create a Label object and pass the win instance

def clickMe():  #Called when the button is clicked
    aButton.configure(text = '** I have been clicked **')  #Changes the text on the button
    aLabel.configure(text = 'A Red Label', foreground = 'red')  #Changes the text and color on the label

aButton = ttk.Button(win, text = 'Click Me!', command = clickMe)  #Creates a button and binds an event handler to handle the click
aButton.grid(column = 1, row = 0)

win.mainloop()  #The event which makes the window appear on screen