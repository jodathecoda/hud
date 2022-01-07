
import os
# Import module
from tkinter import *

# Create object
root = Tk()
root.title("HUD")

global cwd
cwd = os.getcwd()

# Adjust size
root.geometry( "250x300" )

def sb_open():
    sb_open_counter = 0
    f = open(cwd + "\\sb_open_counter.txt", "r")
    for line in f:
        sb_open_counter = int(line.strip())
    f.close()
    sb_open_counter += 1
    f = open(cwd + "\\sb_open_counter.txt", "w")
    f.write(str(sb_open_counter))
    f.close()
    lab_sb_open_button.config(text = str(sb_open_counter) + "%")

selected = ""

# Change the label text
def show():
    label1.config( text = clicked.get() )
    f = open(cwd + "\\selected.txt", "w")
    f.write(label1.cget("text"))
    selected = label1.cget("text")
    root.title("HUD " + selected)
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
drop.grid(column=0, row=0)
#drop.pack()

# Create button, it will change label text
button = Button( root , text = "Select" , command = show )#.pack()
button.grid(column=1, row=0)

preflop_counter_sb = 0 #number of hands
preflop_counter_bb = 0
flop_counter = 0


# Create Label
label1 = Label( root , text = " " )
label1.grid(column=2, row=0)

label2 = Label( root , text = " --- PREFLOP SB --- #" + str(preflop_counter_sb) )
label2.grid(column=0, row=1)
sb_open_button = Button( root , text = "Open" , command = sb_open )#.pack()
sb_open_button.grid(column=0, row=2)
lab_sb_open_button = Label( root , text = " 0%" )
lab_sb_open_button.grid(column=1, row=2)
sb_fold_button = Button( root , text = "Fold" , command = show )#.pack()
sb_fold_button.grid(column=0, row=3)

label3 = Label( root , text = " --- PREFLOP BB --- #" + str(preflop_counter_bb))
label3.grid(column=0, row=4)
bb_fold_button = Button( root , text = "Fold" , command = show )#.pack()
bb_fold_button.grid(column=0, row=5)
bb_call_button = Button( root , text = "Call" , command = show )#.pack()
bb_call_button.grid(column=0, row=6)
bb_raise_button = Button( root , text = "Raise" , command = show )#.pack()
bb_raise_button.grid(column=0, row=7)

label4 = Label( root , text = " --- POSTFLOP --- #" + str(flop_counter))
label4.grid(column=0, row=8)
sb_cbet_button = Button( root , text = "Cbet" , command = show )#.pack()
sb_cbet_button.grid(column=0, row=9)
sb_check_button = Button( root , text = "Check" , command = show )#.pack()
sb_check_button.grid(column=0, row=10)

entry_new_villain = Entry(root)
entry_new_villain.grid(column=0, row=11)
save_new_villain_button = Button( root , text = "Create new Villain" , command = show )
save_new_villain_button.grid(column=1, row=11)

# Execute tkinter
root.mainloop()
