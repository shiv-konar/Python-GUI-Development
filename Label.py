import tkinter as tk
from tkinter import ttk  #For creating themed widgets
win = tk.Tk()  #Create an instance of the Tk class
win.title("Python GUI")  #Set the title of the window

win.resizable(0, 0)  #Disable resizing the GUI

ttk.Label(win, text = 'A Label').grid(column = 0, row = 0)  #Create a Label object and pass the win instance

win.mainloop()  #The event which makes the window appear on screen