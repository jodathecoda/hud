
import os
# Import module
from tkinter import *

# Create object
root = Tk()

global cwd
cwd = os.getcwd()

# Adjust size
root.geometry( "200x350" )

def sb_open():
    pass
    #sb_open_button.config(text="Open 20%")

selected = ""

# Change the label text
def show():
    label1.config( text = clicked.get() )
    f = open(cwd + "\\selected.txt", "w")
    f.write(label1.cget("text"))
    selected = label1.cget("text")
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
clicked.set( "Monday" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

# Create button, it will change label text
button = Button( root , text = "Select" , command = show ).pack()

# Create Label
label1 = Label( root , text = " " )
label1.pack()

label2 = Label( root , text = " ----- PREFLOP SB -----" )
label2.pack()
sb_open_button = Button( root , text = "Open" , command = sb_open ).pack()
sb_fold_button = Button( root , text = "Fold" , command = show ).pack()

label3 = Label( root , text = " ----- PREFLOP BB -----" )
label3.pack()
bb_fold_button = Button( root , text = "Fold" , command = show ).pack()
bb_call_button = Button( root , text = "Call" , command = show ).pack()
bb_raise_button = Button( root , text = "Raise" , command = show ).pack()

label4 = Label( root , text = " ----- POSTFLOP -----" )
label4.pack()
sb_cbet_button = Button( root , text = "Cbet" , command = show ).pack()
sb_check_button = Button( root , text = "Check" , command = show ).pack()

# Execute tkinter
root.mainloop()
