
import os
# Import module
import shutil
from tkinter import *
from pathlib import Path

# Create object
root = Tk()
root.title("HUD")

global cwd
cwd = os.getcwd()

options = []

# Adjust size
root.geometry( "250x300" )

def del_vil():
    for_delete = entry_new_villain.get()
    if "template" in for_delete:
        pass
    else:
        if os.path.isdir(cwd + "\\villains\\" + for_delete):
            shutil.rmtree(cwd + "\\villains\\" + for_delete)

def new_vil():
    the_new_one = entry_new_villain.get()
    if os.path.isdir(cwd + "\\villains\\" + the_new_one):
        pass
    else:
        shutil.copytree(cwd + "\\villains\\template\\", cwd + "\\villains\\" + the_new_one)
        f = open(cwd + "\\villains\\names.txt", "a")
        f.write("\n")
        f.write(the_new_one)
        f.close()

#SB Preflop
def sb_open():
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    sb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt", "r")
        sb_preflop_counter = int(f.read())
        f.close()
    sb_preflop_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt", "w")
        f.write(str(sb_preflop_counter))
        f.close()
        label2.config(text = " --- PREFLOP SB --- #" + str(sb_preflop_counter))

def sb_fold():
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    sb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt", "r")
        sb_preflop_counter = int(f.read())
        f.close()
    sb_preflop_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt", "w")
        f.write(str(sb_preflop_counter))
        f.close()
        label2.config(text = " --- PREFLOP SB --- #" + str(sb_preflop_counter))

#BB Preflop
def bb_fold():
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    bb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "r")
        bb_preflop_counter = int(f.read())
        f.close()
    bb_preflop_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "w")
        f.write(str(bb_preflop_counter))
        f.close()
        label3.config(text = " --- PREFLOP BB --- #" + str(bb_preflop_counter))

def bb_call():
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    bb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "r")
        bb_preflop_counter = int(f.read())
        f.close()
    bb_preflop_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "w")
        f.write(str(bb_preflop_counter))
        f.close()
        label3.config(text = " --- PREFLOP BB --- #" + str(bb_preflop_counter))

def bb_raise():
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    bb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "r")
        bb_preflop_counter = int(f.read())
        f.close()
    bb_preflop_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "w")
        f.write(str(bb_preflop_counter))
        f.close()
        label3.config(text = " --- PREFLOP BB --- #" + str(bb_preflop_counter))

#SB Postflop
def sb_cbet():
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    sb_postflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_counter.txt", "r")
        sb_postflop_counter = int(f.read())
        f.close()
    sb_postflop_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_counter.txt", "w")
        f.write(str(sb_postflop_counter))
        f.close()
        label4.config(text = " --- POSTFLOP SB --- #" + str(sb_postflop_counter))

def sb_check():
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    sb_postflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_counter.txt", "r")
        sb_postflop_counter = int(f.read())
        f.close()
    sb_postflop_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_counter.txt", "w")
        f.write(str(sb_postflop_counter))
        f.close()
        label4.config(text = " --- POSTFLOP SB --- #" + str(sb_postflop_counter))


selected = ""

# Change the label text
def select():
    label1.config( text = clicked.get() )
    selected = label1.cget("text")
    root.title("HUD " + selected)
    f = open(cwd + "//neo.txt", "w")
    f.write(selected)
    f.close()
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    #sb_preflop_counter
    sb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt", "r")
        sb_preflop_counter = int(f.read())
        f.close()
        label2.config(text = " --- PREFLOP SB --- #" + str(sb_preflop_counter))
    #bb_preflop_counter
    bb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "r")
        bb_preflop_counter = int(f.read())
        f.close()
        label3.config(text = " --- PREFLOP BB --- #" + str(bb_preflop_counter))
    #sb_postflop_counter
    sb_postflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_counter.txt", "r")
        sb_postflop_counter = int(f.read())
        f.close()
        label4.config(text = " --- POSTFLOP SB --- #" + str(sb_postflop_counter))

def show():
    pass

for path in Path(cwd + "\\villains\\").iterdir():
    if path.is_dir():
        last_part = os.path.basename(path)
        if "template" not in last_part:
            options.append(last_part)
        else:
            pass

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Villain:" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.grid(column=0, row=0)
#drop.pack()

# Create button, it will change label text
button = Button( root , text = "Select" , command = select )#.pack()
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
sb_fold_button = Button( root , text = "Fold" , command = sb_fold )#.pack()
sb_fold_button.grid(column=0, row=3)

label3 = Label( root , text = " --- PREFLOP BB --- #" + str(preflop_counter_bb))
label3.grid(column=0, row=4)
bb_fold_button = Button( root , text = "Fold" , command = bb_fold )#.pack()
bb_fold_button.grid(column=0, row=5)
bb_call_button = Button( root , text = "Call" , command = bb_call )#.pack()
bb_call_button.grid(column=0, row=6)
bb_raise_button = Button( root , text = "Raise" , command = bb_raise )#.pack()
bb_raise_button.grid(column=0, row=7)

label4 = Label( root , text = " --- POSTFLOP SB --- #" + str(flop_counter))
label4.grid(column=0, row=8)
sb_cbet_button = Button( root , text = "Cbet" , command = sb_cbet )#.pack()
sb_cbet_button.grid(column=0, row=9)
sb_check_button = Button( root , text = "Check" , command = sb_check )#.pack()
sb_check_button.grid(column=0, row=10)

entry_new_villain = Entry(root)
entry_new_villain.grid(column=0, row=11)
save_new_villain_button = Button( root , text = "New" , command = new_vil )
save_new_villain_button.grid(column=1, row=11)
delete_villain_button = Button( root , text = "Delete" , command = del_vil )
delete_villain_button.grid(column=2, row=11)

# Execute tkinter
root.mainloop()
