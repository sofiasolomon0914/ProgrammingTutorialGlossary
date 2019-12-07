"""
Programming Help Guide Project
"""

from tkinter import *


# Key down function
def click():
    entered_text = textentry.get()


# main:
window = Tk()
window.title("Programming Help Guide")
window.configure(background="white")

# Create label
Label(window, text="Enter the tutorial you would "
                   "like: ", bg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)

# Create text entry box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

# Create a submit button
Button(window, text="Submit", width=6, command=click) .grid(row=3, column=0, sticky=W)

window.mainloop()
