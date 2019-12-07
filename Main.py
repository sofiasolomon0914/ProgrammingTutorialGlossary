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
    'bug': 'An error in a program.', 'central processing unit': 'The heart of any computer. It is what runs the '
    'software that we write; also called "CPU" or "the processor". ', 'compile': 'To translate a program all'
    ' at once, in preparation for later execution.', 'high-level language': 'A programming language like Python that is'
    ' designed to be easy for humans to read or write.', 'interactive mode': 'A way of using the Python interpreter by '
    ' typing commands and expressions at the prompt.', 'interpret': 'To execute a program in a high-level language '
    'by translating it one line at a time.', 'low-level language': 'A programming language that is designed to be easy'
    ' for a computer to execute; also called "machine code" or "assembly language".', 'machine code': 'The lowest-level'
    ' language for software, which is the language that is directly executed by the Central Processing Unit(CPU).',
    'main memory': 'Stores programs and data. Main memory loses its information when the power is turned off.', 'parse':
    'To examine a program and analyze the syntactic structure.', 'portability': 'A property of a program that can run'
    ' on more than one kind of computer.', 'print function': 'An instruction that causes the Python interpreter to'
    ' display a value on the screen.', 'problem solving': 'The process of formulating a problem, finding a solution'
    ', and expressing the solution.', 'program': 'A set of instructions that specifies a computation.', 'prompt':
    'When a program displays a message and pauses for the user to type some input into the program.',
    'secondary memory': 'Stores programs and data and retains its information even when its power is turned off.'
    ' Generally slower than the main memory. Examples of secondary include disk drives and flash memory in USB sticks.',
    'semantics': 'The meaning of a program.', 'semantic error': 'An error in a program tat makes it do something other'
    ' than what the programmer intended.', 'source code': 'A program in a high-level language.', 'assignment':
    'A statement that assigns a value to a variable.', 'comment': 'Information in a program that is meant for'
    ' other programmers (or anyone reading the source code) and has no effect on the execution of the program.',
    'concatenate': 'To join two operands end to end.',
    'evaluate': 'To simplify an expression by performing the operations in order to yield a single value.',
    'expression': 'A combination of variables, operators, and values that represents a single result value.',
    'floating point': 'A type that represents numbers with fractional parts.',
    'integer': 'A type that represents whole numbers.', 'keyword': 'A reserved word that is used by the'
    ' compiler to parse a program; you cannot use keywords like if, def, and while as variable names.', 'mnemonic':
    'A memory aid. We often give variables mnemonic names to hep us remember what is stored in the variable.',
    'modulus operator': 'An operator, denoted with a percent sign (%), that works on integers and yields the remainder'
    ' when one number is divided by another.', 'operand': 'One of the values on which an operator operates.',
    'operator': 'A special symbol that represents a simple computation like addition, multiplication, or string'
    ' concentration.', 'rules of precedence': 'The set of rules governing the order in which expressions involving'
    ' multiple operators and operands are evaluated.', 'statement': 'A section of code that represents a command'
    ' or action.', 'string': 'A type that represents sequences of characters.', 'type': ' A category of values.'
    ' For example: type int, type float, and type str.', 'value': 'One of the basic units of data, like a number'
    ' or string, that a program manipulates.', 'variable': 'A name that refers to a value.'
}


# Exit function
def close_window():
    window.destroy()
    exit()


# Add exit button
Button(window, text="Exit", width=14, command=close_window, ).grid(row=7, column=0, sticky=W)

window.mainloop()
