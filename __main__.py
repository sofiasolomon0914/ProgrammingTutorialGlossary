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
    ' or string, that a program manipulates.\n\n An object that appears in a dictionary as the second part '
    'of a key-value pair. This is more specific than our previous use of the word "value".',
    'variable': 'A name that refers to a value.', 'body': 'The sequence of '
    'statements within a compound statement or inside a function definition.',
    'boolean expression': 'An expression whose value is either True or'
    ' False.', 'branch': 'One of the alternative sequences of statements in a conditional statements.',
    'chained conditional': 'A conditional statement with a series of alternative branches.', 'comparison operator':
    'One of the operators that compares its operands: ==, !=, >, <, >=, and <=.', 'conditional statement': 'A statement'
    ' that controls the flow of execution depending on some condition.', 'condition': 'The boolean expression in a '
    'conditional statement that determined which branch is executed.', 'compound statement': 'A statement that consists'
    ' of a header ad a body. The header end with a colon(:). The body is indented relative to the header.',
    'guardian pattern': 'Where we construct a logical a logical expression with additional comparisons to take' ''
                        'advantage'
    ' of the short-circuit behavior.', 'logical operator': 'One of the operators that combines boolean expressions: '
    'and, or, and not.', 'nested conditional': 'A conditional statement that appears in one the branches of another '
    'conditional statement.', 'traceback': 'A list of the functions that are executing, printed when an exception '
    'occurs.', 'short circuit': 'When Python is part-way through evaluating a logical expression and stops the '
    'evaluation because Python knows the final value for the expression without needing to evaluate the rest of the '
    'expression.', 'algorithm': 'A general process for solving a category of problem.', 'argument': 'A value '
    'provided to a function when the function is called. This value is assigned to the corresponding parameter '
    'in the function.', 'composition': 'Using an expression as part of a larger expression, or a statement as part of '
    'a larger statement.', 'deterministic': 'Pertaining to a program that does the same thing each time it runs, '
    'given the same inputs.', 'dot notation': 'The syntax for calling a function in another module by '
    'specifying the module name followed by a dot (period) and the function name.', 'flow of execution':
    'The order in which statements are executed during a program run.', 'fruitful function': 'A function that returns '
    'a value.', 'function': 'A names sequence of statements that performs some useful operation. Functions may or may '
    'or may not produce a result.', 'function call': 'A statement that executes a function. It consists of the function'
    ' name followed by an argument list.', 'function definition': 'A statement that creates a new function,specifying '
    'its name, parameters, and the statements it executes.', 'function object': 'A value created by a function '
    'definition. The name of the function is a variable that refers to a function object.', 'header': 'The first '
    'of a function definition.', 'import statement': 'A statement that reads a module file and creates a module object.'
    , 'module object': 'A value created by an import statement tha provides access to the data and code defined in a '
    'module.', 'parameter': 'A name used inside a function to refer to a the value passed as an argument.',
    'pseudorandom': 'Pertaining to a sequence of numbers that appear to be random, but are generated by a '
    'deterministic program.', 'return value': 'The result of a function. If a function call is used as an expression, '
    'the return value is the value of the expression.',
    'void function': 'A function that does not return a value.', 'accumulator': 'A '
    'variable used in a loop to add or accumulate a result.', 'counter': 'A variable used in a loop to count the number'
    ' of times something happened. We initialize a counter to zero and then increment the counter each time we want'
    ' to "count" something.', 'decrement': 'An update that decreases the value of a variable.', 'initialize':
    'An assignment that gives an initial value to a variable that will be updated.', 'increment': 'An update'
    ' that increases the value of a variable(often one by one).', 'infinite loop': 'A loop in which the terminating '
    'condition is never satisfied or for which there is no terminating condition.', 'iteration': 'Repeated '
    'execution of a set of statements using either a function that calls itself or a loop.',
    'empty string': 'A string with no'
    ' characters and length 0, represented by two quotation marks.', 'format operator': 'An operator,%, that  takes '
    'a format string and a tuple and generates a string that includes the elements of the tuple formatted as specified '
    'by the format string.', 'format sequence': 'A sequence of characters in a format string, like %d, that specifies '
    'how a value should be formatted.', 'format string': 'A string, used with the format operator, that contains '
    'format sequences.', 'flag': 'A boolean variable used to indicate whether a condition is true or false.',
    'invocation': 'A statement that calls a method.', 'immutable': 'The property of a sequence whose items cannot be '
    'assigned.', 'index': 'An integer value used to select an item in a sequence, such as a character in a string.'
    '\nAn integer value that indicates a value on a list.\n\nAdditional data that the database software maintains as '
    'rows and inserts into a table to make lookups very fast.',
    'item': 'One of the values in a sequence.\n\nAnother name for a key-value pair.',
    'method': 'a function that is associated with an object and is '
    'called using dot notation.', 'object': 'Something a variable can refer to. For now, you can use "object" and '
    '"value" interchangeably.\nAn object has a type and a value.\n\nA constructed instance of a class. An object '
    'contains all of the attributes and methods that were defined by the class. Some object-oriented documentation '
    'uses the term "instance" interchangeably with "object".',
    'search': 'A pattern of traversal that stops when it finds what it is looking for.',
    'sequence': 'An ordered set; that is, a set of ordered values where each value is identified by an integer'
    ' index.', 'slice': 'A part of a string specified by a range of indices.', 'traverse': 'To iterate through the '
    'items in a sequence, performing a similar operation on each.', 'catch': 'To prevent an exception from '
    'terminating a program using the try and except statements.', 'newline': 'A special character used in files and '
    'and string to indicate the end of a line.', 'Pythonic': 'A technique that works elegantly in Python. '
    '"Using try and except is the Pythonic way to recover from missing files".', 'Quality Assurance': ' A person or '
    'team focused on ensuring the overall quality of a software product. QA is often involved in testing a product and '
    'identifying problems before the product is released.', 'text file': 'A sequence of characters stored in permanent'
    ' storage like a had drive.', 'aliasing': 'A circumstance where two or more variables refer to the same object.',
    'delimiter': 'A character or string used to indicate where a string should be split.', 'element': 'One of the '
    'values in a list (or other sequence); also called items.', 'equivalent': 'Having the same value.', 'identical':
    'Being the same object (which implies equivalence).', 'list': 'A sequence of values.', 'list traversal':
    'The sequential accessing of each element in a list.', 'nested list': 'A list that is an element of another list.',
    'reference': 'The association between a variable and its value.', 'dictionary': 'A mapping from a set of keys '
    'to their corresponding values.', 'hashtable': 'The algorithm used to implement Python dictionaries.',
    'hash function': 'A function used by a hashtable to compute the location for a key.', 'histogram':
    'A set of counters.', 'implementation': 'A way of performing a computation.', 'key': 'An object that appears in a '
    'dictionary as the first part of a key-value pair.', 'key-value pair': 'The representation of the mapping from '
    'a key and finds the corresponding value.', 'lookup': 'A dictionary operation that takes a key and finds the '
    'corresponding value.', 'nested loop': 'When there are one or more loop "inside" of another loop. '
    'The inner loop runs to completion each time the outer loop runs once.', 'comparable': 'A type where one value '
    'can be checked to see if it is greater than, less than, or equal to another value of the same type. Types which '
    'are comparable can be put in a list and sorted.', 'data structure': 'A collection of related values, often '
    'organized in lists, dictionaries, tuples, ect.', 'DSU': 'Abbreviation of "decorate-sort-undecorate", a pattern '
    'that involves building a list of tuples, sorting, and extracting part of the result.', 'gather':
    'The operation of assembling a variable-length argument tuple.', 'hashable': 'A type that has a hash function. '
    'Immutable types like integers, floats, and string are hashable; mutable types like lists and dictionaries are not.'
    , 'scatter': 'The operation of treating a sequence as a list of arguments.', 'shape': 'A summary of the type, size,'
    ' and composition of a data structure.', 'singleton': 'A list (or other sequence ) with a single element.',
    'tuple': 'An immutable sequence of elements.\n\nA single entry in a database table that is a set of attributes. '
             'More typically called "row".',
    'tuple assignment': 'An assignment with a sequence on the right '
    'side and a tuple of variable on the left. The right side is evaluated and then its elements are assigned to the '
    'variables on the left.',
    'brittle code': 'Code that works when the input data is in a particular format but is '
    'prone to breakage if there is some deviation from the correct format. We call this "brittle code" because it '
    'can be easily broken.', 'greedy matching': 'Te notion that the + and * characters in a regular expression '
    'expand outward to match the largest possible string.', 'grep': 'A command available in most Unix systems that '
    'searches for text files that match regular expression. The command name stands for "Generalized Regular Expression'
    ' Parser".', 'regular expression': 'A language for expressing more complex search strings. A regular expression '
    'may contain special characters that indicate that a search only matches at the beginning or end of a line or many '
    'other similar capabilities.', 'wild card': 'A special character that matches any character. In regular expressions'
    ' the wild-card character is the period.', 'BeautifulSoup': 'A Python library for passing HTML documents and '
    'extracting data from HTML documents that compensates fro the most of the imperfections in the HTML that '
    'browsers generally ignore. You can download the BeautifulSoup code from ww.crummy.com.', 'port': 'A number that '
    'generally indicates which application you are contacting when you make a socket connection to a server. As '
    'an example, web traffic usually uses port 80 while email uses port 25.', 'scrape': 'When a program pretends to be '
    'a web browser and retrieves a web page content. Often programs are following the links in one page to to find they'
    'can traverse a network of pages or a social network.', 'socket': 'A network connection between two applications '
    'can send and receive data in either direction.', 'spider': 'The act of a web search engine retrieving a page'
    ' and so on until they have nearly all of the pages on the Internet which they use to build search index.',
    'API': 'Application Program Interface - A contract between applications that defines the patterns of interaction '
    'between two application components.', 'ElementTree': 'A built-in Python library used to parse XML data.',
    'JSON': 'JavaScript Object Notation. A format that allows for the markup of structured data baaed on the syntax'
    ' on the syntax of JavaScript Objects.', 'SOA': 'Service-Oriented Architecture. When an application is made '
    'of components connect across a network.', 'XML': 'eXtensible Markup Language. A format that allows for the '
    'markup of structured data.', 'attribute': 'A variable that is part of a class.\n\nOne of the values within '
    'a tuple. More commonly called a "column" or "field".',
    'class': 'A template that can '
    'be used to construct a project. Defines the attributes and methods that will make up the object.',
    'child class': 'A new class created when a parent class in extended. The child class inherits all of the attributes'
    'and methods of the parent class.', 'constructor': 'An optional specially names method(__init__) that is called '
    'at the moment when a class is being used to construct an object. Usually this is used to set up initial values '
    'for the object.', 'destructor': 'An optional specially named method (__del__) that is called at the moment '
    'just before an object is destroyed.', 'inheritance': ' When we create a new class (child) by extending an '
    'existing class (parent). The child class has all the attributes and methods defined by the child class.',
    'parent class': 'The class which is being extended to create a new child class. The parent class contributes all '
    'of its methods and attributes to the new child class.', 'constraint': 'When we tell the database to enforce'
    ' a rule on a field or a row in a table. A common constraint is to insist that there can be no duplicate values '
    'in a particular field (i.e., all the values must be unique).', 'cursor': 'A cursor allows you to execute SQL '
    'commands in a database and retrieve data from the database. A cursor is similar to a socket or a file handle '
    'for network connections and files, respectively.', 'database browser': 'A piece of software that allows you to '
    'directly connect to a database and manipulate the database directly without writing a program.', 'foreign key':
    'A numeric key that points to the primary key of a row in another table. Foreign keys establish relationships '
    'between rows stored in different tables.', 'logical key': 'A key that the "outside word" uses to look up a '
    'particular row. For example in a table of user accounts, a persons email address might be a good candidate '
    'as the logical key for the users data.', 'normalization': 'Designing a data model so that no data is replicated '
    'We store each item of data at one place in the database and reference it elsewhere using a foreign key.',
    'primary key': 'A numeric key assigned to each row that is used to refer to one row in a table from another table. '
    'Often the database is configured to automatically assign primary keys as rows are inserted.', 'relation':
    'An area within a database that contains tuples and attributes. More typically called a "table".'



    }


# Exit function
def close_window():
    window.destroy()
    exit()


# Add exit button
Button(window, text="Exit", width=14, command=close_window, ).grid(row=7, column=0, sticky=W)

window.mainloop()