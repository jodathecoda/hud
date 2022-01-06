
import os
# Import module
from tkinter import *

# Create object
root = Tk()

global cwd
cwd = os.getcwd()

# Adjust size
root.geometry( "300x300" )

selected = ""

# Change the label text
def show():
    label1.config( text = clicked.get() )
    f = open(cwd + "\\selected.txt", "w")
    f.write(label1.cget("text"))
    f.close()
	

options = []
f = open(cwd + "\\names.txt", "r")
for line in f:
    #print(line)
    options.append(line.strip())
f.close()

# Dropdown menu options
'''
options = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
]
'''

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Pick up" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

# Create button, it will change label text
button = Button( root , text = "Select" , command = show ).pack()

# Create Label
label1 = Label( root , text = " " )
label1.pack()

# Execute tkinter
root.mainloop()
