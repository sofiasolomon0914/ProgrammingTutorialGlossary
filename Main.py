# Programming Help Guide Project

from tkinter import *

# main:
window = Tk()
window.title("Programming Help Guide")
window.configure(background="white")

# Create Welcome Page
Label(window, text="Welcome to Programming Help Guide!\nYou can use this program to search for tutorials and "
                   "programming definitions.", bg="white", fg="black", font=("times", 150, "bold"))
