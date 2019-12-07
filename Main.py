"""
Programming Help Guide Project
"""

from tkinter import *


# Key down function
def click():
    entered_text = textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_dictionary[entered_text]
    except:
        definition = "sorry there is no word like that please try again"
    output.insert(END, definition)


# main:
window = Tk()
window.title("Programming Glossary")
window.configure(background="white")

# Create label
Label(window, text="Enter the definition of the word you would "
                   "like and then click submit", bg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)

# Create text entry box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

# Create a submit button
Button(window, text="Submit", width=6, command=click).grid(row=3, column=0, sticky=W)

# Create another label
Label(window, text="\nDefinition: ", bg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)

# Create a text box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

# the dictionary
my_dictionary = {
    'algorithm': 'Step by step instructions to complete a task', 'bug': 'piece of code that causes a program to fail'
}


# Exit function
def close_window():
    window.destroy()
    exit()


# Add exit button
Button(window, text="Exit", width=14, command=close_window, ).grid(row=7, column=0, sticky=W)

window.mainloop()
