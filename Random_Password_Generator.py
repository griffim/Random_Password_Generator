import random
import tkinter as tk
from tkinter import *

#
# This code takes an integer value and generates a string password of that length
#

# Defines overall program, title, and initial geometry
root = Tk()
root.title("Random Password Generator")
root.geometry('330x380')
root.minsize(330, 380)
root.columnconfigure(0, weight=1)
for i in range(1, 15):
    root.rowconfigure(i, weight=1)


# Defines all possible character for generated password
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase = "abcdefghijklmnopqrstuvwxyz"
allNum = "01234567890123456789"
allPunc = "!@#$%&!@#$%&"

# allChar variable stores all four cases above into one variable as a list
allChar = list(upperCase + lowerCase + allNum + allPunc)


# Defines the open space(s) on the program
Label1 = Label(root, text="          ")
Label1.grid(row=0, column=0)
Label2 = Label(root, text="          ")
Label2.grid(row=2, column=0)
Label3 = Label(root, text="          ")
Label3.grid(row=4, column=0)
Label4 = Label(root, text="          ")
Label4.grid(row=6, column=0)
Label5 = Label(root, text="          ")
Label5.grid(row=7, column=0)
Label6 = Label(root, text="          ")
Label6.grid(row=9, column=0)
Label7 = Label(root, text="          ")
Label7.grid(row=11, column=0)
Label8 = Label(root, text="          ")
Label8.grid(row=13, column=0)
Label9 = Label(root, text="          ")
Label9.grid(row=15, column=0)


# Gives context to user input text box
contextInputLabel = Label(root, text="Please enter length of password:", padx=40, pady=5)
contextInputLabel.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

# Gives context to the output password box
contextOutputLabel = Label(root, text="Here is the generated password:", padx=40, pady=5)
contextOutputLabel.grid(row=8, column=0)


# Defines user input text box
userInput = Entry(root)
userInput.grid(row=3, column=0)

# Defines the text box for the generated password output
outputPass = Entry(root, bg="white", fg="black")
outputPass.insert(-1, '')
outputPass.grid(row=10, column=0)
outputPass.config(state='disabled', width=30)


# Defines the 'Generate' button functionality
def genPassBtn():
    # Allows the button to only be accessible if it has not been run yet
    try:
        # Checks if input length is between 1 and 20
        if int(userInput.get()) <= 20 and int(userInput.get()) > 0:
            # Readies the output site
            outputPass.config(state='normal')
            outputPass.delete(0, END)

            # Runs the pseudorandom password generation functionality
            passLen = int(userInput.get())
            random.shuffle(allChar)

            finalPass = []

            for i in range(passLen):
                finalPass.append(random.choice(allChar))

            random.shuffle(finalPass)

            # Change the output field to the output password
            outputPass.insert(-1, "".join(finalPass))
            outputPass.config(state='disabled')
            genButton.config(state='disabled')

        # Catch case if input length is greater than 20
        elif int(userInput.get()) > 20:
            outputPass.config(state='normal')
            outputPass.insert(-1, "Try again with value <=20") # 24 characters long
            outputPass.config(state='disabled')
            genButton.config(state='disabled')

        # Catch case if input length is greater than or equal to 0
        elif int(userInput.get()) <= 0:
            outputPass.config(state='normal')
            outputPass.insert(-1, "Try again with value >0") # 23 characters long
            outputPass.config(state='disabled')
            genButton.config(state='disabled')

    # Catch case for any unassigned error or miscellaneous case
    except:
        outputPass.insert(-1, "Error, please try again") # 24 characters long
        outputPass.config(state='disabled')
        genButton.config(state='disabled')


# Defines the 'Copy to clipboard' button functionality
def copyPassBtn():
    root.clipboard_clear()
    root.clipboard_append(str(outputPass.get()))
    root.update()


# Defines the 'Clear' button functionality
def clearPassBtn():
    outputPass.config(state='normal')
    outputPass.delete(0, END)
    outputPass.insert(-1, '')
    outputPass.config(state='disabled')
    # Reactivates the 'Generate' button
    genButton.config(state='normal')


# Structures 'Generate' button
genButton = Button(root, text="Generate!", padx=20, pady=5, command=genPassBtn)
genButton.grid(row=5, column=0)

# Structures copy to clipboard button
copyButton = Button(root, text="Copy to clipboard", padx=20, pady=5, command=copyPassBtn)
copyButton.grid(row=12, column=0)

# Structures 'Clear' button
clearButton = Button(root, text="Clear", padx=20, pady=5, command=clearPassBtn)
clearButton.grid(row=14, column=0)


# Executes the program
root.mainloop()
