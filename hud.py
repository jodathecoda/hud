
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

global sb_preflop_sum
global bb_preflop_sum
global sb_postflop_sum

global sb_pre_open_counter
global sb_pre_fold_counter

global bb_pre_fold_counter
global bb_pre_call_counter
global bb_pre_raise_counter

global sb_post_cbet_counter
global sb_post_check_counter

sb_preflop_sum = 0
bb_preflop_sum = 0
sb_postflop_sum = 0

sb_pre_open_counter = 0
sb_pre_fold_counter = 0

bb_pre_fold_counter = 0
bb_pre_call_counter = 0
bb_pre_raise_counter = 0

sb_post_cbet_counter = 0
sb_post_check_counter = 0

options = []

# Adjust size
root.geometry( "250x300" )

def del_vil():
    for_delete = entry_new_villain.get()
    if "template" in for_delete:
        pass
    elif len(for_delete) < 1:
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
    global sb_preflop_sum
    global sb_pre_open_counter
    global sb_pre_fold_counter

    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    #preflop counter
    sb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt", "r")
        sb_preflop_counter = float(f.read())
        f.close()
    sb_preflop_counter += 1
    sb_preflop_sum = sb_preflop_counter
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt", "w")
        f.write(str(sb_preflop_counter))
        f.close()
        label2.config(text = " --- PREFLOP SB --- #" + str(round(sb_preflop_sum)), fg='gold3')

    #preflop open counter
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_open.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_open.txt", "r")
        sb_pre_open_counter = float(f.read())
        f.close()
    sb_pre_open_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_open.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_open.txt", "w")
        f.write(str(sb_pre_open_counter))
        f.close()
        if sb_preflop_sum < 1:
            lab_sb_open_button.config(text = "0.0%")
        else:
            lab_sb_open_button.config(text = " " + str(round(sb_pre_open_counter/sb_preflop_sum * 100,1)) + "%")

    #Update also preflop fold counter
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_fold.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_fold.txt", "r")
        sb_pre_fold_counter = float(f.read())
        f.close()
        if sb_preflop_sum < 1:
            lab_sb_fold_button.config(text = " 0.0%")
        else:
            lab_sb_fold_button.config(text = " " + str(round(sb_pre_fold_counter/sb_preflop_sum * 100,1)) + "%")

def sb_fold():
    global sb_preflop_sum
    global sb_pre_open_counter
    global sb_pre_fold_counter

    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    #preflop sb counter
    sb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt", "r")
        sb_preflop_counter = float(f.read())
        f.close()
    sb_preflop_counter += 1
    sb_preflop_sum = sb_preflop_counter
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_counter.txt", "w")
        f.write(str(sb_preflop_counter))
        f.close()
        label2.config(text = " --- PREFLOP SB --- #" + str(round(sb_preflop_sum)), fg='gold3')

    #preflop sb fold %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_fold.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_fold.txt", "r")
        sb_pre_fold_counter = float(f.read())
        f.close()
    sb_pre_fold_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_fold.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_fold.txt", "w")
        f.write(str(sb_pre_fold_counter))
        f.close()
        if sb_preflop_sum < 1:
            lab_sb_fold_button.config(text = "0.0%")
        else:
            lab_sb_fold_button.config(text = " " + str(round(sb_pre_fold_counter/sb_preflop_sum * 100,1)) + "%")

    #Update also preflop sb open counter
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_open.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_open.txt", "r")
        sb_pre_open_counter = float(f.read())
        f.close()
        if sb_preflop_sum < 1:
            lab_sb_open_button.config(text = "0.0%")
        else:
            lab_sb_open_button.config(text = " " + str(round(sb_pre_open_counter/sb_preflop_sum * 100,1)) + "%")

#BB Preflop
def bb_fold():
    global bb_preflop_sum
    global sb_pre_open_counter
    global bb_pre_fold_counter
    global bb_pre_call_counter

    #preflop bb counter
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    bb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "r")
        bb_preflop_counter = float(f.read())
        bb_preflop_sum = bb_preflop_counter
        f.close()
    bb_preflop_counter += 1
    bb_preflop_sum = bb_preflop_counter
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "w")
        f.write(str(bb_preflop_counter))
        f.close()
        label3.config(text = " --- PREFLOP BB --- #" + str(round(bb_preflop_sum)), fg='purple')

    #preflop bb fold %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_fold.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_fold.txt", "r")
        bb_pre_fold_counter = float(f.read())
        f.close()
    bb_pre_fold_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_fold.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_fold.txt", "w")
        f.write(str(bb_pre_fold_counter))
        f.close()
        if bb_preflop_sum < 1:
            lab_bb_fold_button.config(text = "0.0%")
        else:
            lab_bb_fold_button.config(text = " " + str(round(bb_pre_fold_counter/bb_preflop_sum * 100,1)) + "%")

    #Update also preflop bb & call % raise
    #call %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_call.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_call.txt", "r")
        bb_pre_call_counter = float(f.read())
        f.close()
        if bb_preflop_sum < 1:
            lab_bb_call_button.config(text = "0.0%")
        else:
            lab_bb_call_button.config(text = " " + str(round(bb_pre_call_counter/bb_preflop_sum * 100,1)) + "%")
    #raise %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_raise.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_raise.txt", "r")
        bb_pre_raise_counter = float(f.read())
        f.close()
        if bb_preflop_sum < 1:
            lab_bb_raise_button.config(text = "0.0%")
        else:
            lab_bb_raise_button.config(text = " " + str(round(bb_pre_raise_counter/bb_preflop_sum * 100,1)) + "%")
    

def bb_call():
    global bb_preflop_sum
    global sb_pre_open_counter
    global bb_pre_fold_counter
    global bb_pre_call_counter

    #preflop bb counter
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    bb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "r")
        bb_preflop_counter = float(f.read())
        bb_preflop_sum = bb_preflop_counter
        f.close()
    bb_preflop_counter += 1
    bb_preflop_sum = bb_preflop_counter
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "w")
        f.write(str(bb_preflop_counter))
        f.close()
        label3.config(text = " --- PREFLOP BB --- #" + str(round(bb_preflop_sum)) , fg='purple')
    
    #preflop bb call %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_call.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_call.txt", "r")
        bb_pre_call_counter = float(f.read())
        f.close()
    bb_pre_call_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_call.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_call.txt", "w")
        f.write(str(bb_pre_call_counter))
        f.close()
        if bb_preflop_sum < 1:
            lab_bb_call_button.config(text = "0.0%")
        else:
            lab_bb_call_button.config(text = " " + str(round(bb_pre_call_counter/bb_preflop_sum * 100,1)) + "%")
    
    #Update also preflop bb & fold % raise
    #fold %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_fold.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_fold.txt", "r")
        bb_pre_fold_counter = float(f.read())
        f.close()
        if bb_preflop_sum < 1:
            lab_bb_fold_button.config(text = "0.0%")
        else:
            lab_bb_fold_button.config(text = " " + str(round(bb_pre_fold_counter/bb_preflop_sum * 100,1)) + "%")
    #raise %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_raise.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_raise.txt", "r")
        bb_pre_raise_counter = float(f.read())
        f.close()
        if bb_preflop_sum < 1:
            lab_bb_raise_button.config(text = "0.0%")
        else:
            lab_bb_raise_button.config(text = " " + str(round(bb_pre_raise_counter/bb_preflop_sum * 100,1)) + "%")

def bb_raise():
    global bb_preflop_sum
    global sb_pre_open_counter
    global bb_pre_fold_counter
    global bb_pre_call_counter

    #preflop bb counter
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    bb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "r")
        bb_preflop_counter = float(f.read())
        bb_preflop_sum = bb_preflop_counter
        f.close()
    bb_preflop_counter += 1
    bb_preflop_sum = bb_preflop_counter
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "w")
        f.write(str(bb_preflop_counter))
        f.close()
        label3.config(text = " --- PREFLOP BB --- #" + str(round(bb_preflop_sum)), fg='purple')
    
    #preflop bb raise %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_raise.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_raise.txt", "r")
        bb_pre_raise_counter = float(f.read())
        f.close()
    bb_pre_raise_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_raise.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_raise.txt", "w")
        f.write(str(bb_pre_raise_counter))
        f.close()
        if bb_preflop_sum < 1:
            lab_bb_raise_button.config(text = "0.0%")
        else:
            lab_bb_raise_button.config(text = " " + str(round(bb_pre_raise_counter/bb_preflop_sum * 100,1)) + "%")

    #Update also preflop bb & fold % call
    #fold %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_fold.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_fold.txt", "r")
        bb_pre_fold_counter = float(f.read())
        f.close()
        if bb_preflop_sum < 1:
            lab_bb_fold_button.config(text = "0.0%")
        else:
            lab_bb_fold_button.config(text = " " + str(round(bb_pre_fold_counter/bb_preflop_sum * 100,1)) + "%")

    #call %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_call.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_call.txt", "r")
        bb_pre_call_counter = float(f.read())
        f.close()
        if bb_preflop_sum < 1:
            lab_bb_call_button.config(text = "0.0%")
        else:
            lab_bb_call_button.config(text = " " + str(round(bb_pre_call_counter/bb_preflop_sum * 100,1)) + "%")

#SB Postflop
def sb_cbet():
    global sb_postflop_sum
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    sb_postflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_counter.txt", "r")
        sb_postflop_counter = float(f.read())
        sb_postflop_sum = sb_postflop_counter
        f.close()
    sb_postflop_counter += 1
    sb_postflop_sum = sb_postflop_counter
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_counter.txt", "w")
        f.write(str(sb_postflop_counter))
        f.close()
        label4.config(text = " --- POSTFLOP SB --- #" + str(round(sb_postflop_sum)),fg='gold3')

def sb_check():
    global sb_postflop_sum
    f = open(cwd + "\\neo.txt", "r")
    chosen_one = f.read().strip()
    f.close()
    sb_postflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_counter.txt", "r")
        sb_postflop_counter = float(f.read())
        sb_postflop_sum = sb_postflop_counter
        f.close()
    sb_postflop_counter += 1
    sb_postflop_sum = sb_postflop_counter
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_counter.txt", "w")
        f.write(str(sb_postflop_counter))
        f.close()
        label4.config(text = " --- POSTFLOP SB --- #" + str(round(sb_postflop_sum)),fg='gold3')


selected = ""

# Change the label text
def select():
    global sb_preflop_sum
    global bb_preflop_sum
    global sb_postflop_sum

    global sb_pre_open_counter
    global sb_pre_fold_counter

    global bb_pre_fold_counter
    global bb_pre_call_counter
    global bb_pre_raise_counter

    global sb_post_cbet_counter
    global sb_post_check_counter

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
        sb_preflop_counter = float(f.read())
        sb_preflop_sum = sb_preflop_counter
        f.close()
        label2.config(text = " --- PREFLOP SB --- #" + str(round(sb_preflop_counter)),fg='gold3')
    #bb_preflop_counter
    bb_preflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_counter.txt", "r")
        bb_preflop_counter = float(f.read())
        bb_preflop_sum = bb_preflop_counter
        f.close()
        label3.config(text = " --- PREFLOP BB --- #" + str(round(bb_preflop_counter)), fg='purple')
    #sb_postflop_counter
    sb_postflop_counter = 0
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_counter.txt", "r")
        sb_postflop_counter = float(f.read())
        sb_postflop_sum = sb_postflop_counter
        f.close()
        label4.config(text = " --- POSTFLOP SB --- #" + str(round(sb_postflop_counter)),fg='gold3')
    #preflop sb open %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_open.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_open.txt", "r")
        sb_pre_open_counter = float(f.read())
        f.close()
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_open.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_open.txt", "w")
        f.write(str(sb_pre_open_counter))
        f.close()
        if sb_preflop_sum < 1:
            lab_sb_open_button.config(text = " 0.0%")
        else:
            lab_sb_open_button.config(text = " " + str(round(sb_pre_open_counter/sb_preflop_sum * 100,1)) + "%")
    #preflop sb fold %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_fold.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_fold.txt", "r")
        sb_pre_fold_counter = float(f.read())
        f.close()
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_fold.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_fold.txt", "w")
        f.write(str(sb_pre_fold_counter))
        f.close()
        if sb_preflop_sum < 1:
            lab_sb_fold_button.config(text = " 0.0%")
        else:
            lab_sb_fold_button.config(text = " " + str(round(sb_pre_fold_counter/sb_preflop_sum * 100,1)) + "%")
    #preflop bb fold %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_fold.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_fold.txt", "r")
        bb_pre_fold_counter = float(f.read())
        f.close()
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_fold.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_fold.txt", "w")
        f.write(str(bb_pre_fold_counter))
        f.close()
        if bb_preflop_sum < 1:
            lab_bb_fold_button.config(text = " 0.0%")
        else:
            lab_bb_fold_button.config(text = " " + str(round(bb_pre_fold_counter/bb_preflop_sum * 100,1)) + "%")
    #preflop bb call %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_call.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_call.txt", "r")
        bb_pre_call_counter = float(f.read())
        f.close()
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_call.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_call.txt", "w")
        f.write(str(bb_pre_call_counter))
        f.close()
        if bb_preflop_sum < 1:
            lab_bb_call_button.config(text = " 0.0%")
        else:
            lab_bb_call_button.config(text = " " + str(round(bb_pre_call_counter/bb_preflop_sum * 100,1)) + "%")
    #preflop bb raise %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_raise.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_raise.txt", "r")
        bb_pre_raise_counter = float(f.read())
        f.close()
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_raise.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_bb_raise.txt", "w")
        f.write(str(bb_pre_raise_counter))
        f.close()
        if bb_preflop_sum < 1:
            lab_bb_raise_button.config(text = " 0.0%")
        else:
            lab_bb_raise_button.config(text = " " + str(round(bb_pre_raise_counter/bb_preflop_sum * 100,1)) + "%")
    #postlop sb cbet %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_cbet.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_cbet.txt", "r")
        sb_post_cbet_counter = float(f.read())
        f.close()
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_cbet.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_cbet.txt", "w")
        f.write(str(bb_pre_raise_counter))
        f.close()
        if bb_preflop_sum < 1:
            lab_sb_cbet_button.config(text = " 0.0%")
        else:
            lab_sb_cbet_button.config(text = " " + str(round(sb_post_cbet_counter/sb_postflop_sum * 100,1)) + "%")

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

label2 = Label( root , text = " --- PREFLOP SB --- #" + str(round(preflop_counter_sb)), fg='gold3' )
label2.grid(column=0, row=1)
sb_open_button = Button( root , text = "open" , command = sb_open, fg='orange' )
sb_open_button.grid(column=0, row=2)
lab_sb_open_button = Label( root , text = " 0.0%" )
lab_sb_open_button.grid(column=1, row=2)

sb_fold_button = Button( root , text = "fold" , command = sb_fold, fg='RoyalBlue3' )
sb_fold_button.grid(column=0, row=3)
lab_sb_fold_button = Label( root , text = " 0.0%" )
lab_sb_fold_button.grid(column=1, row=3)

label3 = Label( root , text = " --- PREFLOP BB --- #" + str(round(preflop_counter_bb)), fg='purple')
label3.grid(column=0, row=4)

bb_fold_button = Button( root , text = "FOLD" , command = bb_fold, fg='blue' )
bb_fold_button.grid(column=0, row=5)
lab_bb_fold_button = Label( root , text = " 0.0%" )
lab_bb_fold_button.grid(column=1, row=5)

bb_call_button = Button( root , text = "CALL" , command = bb_call, fg='green' )
bb_call_button.grid(column=0, row=6)
lab_bb_call_button = Label( root , text = " 0.0%" )
lab_bb_call_button.grid(column=1, row=6)


bb_raise_button = Button( root , text = "RAISE" , command = bb_raise, fg='red' )
bb_raise_button.grid(column=0, row=7)
lab_bb_raise_button = Label( root , text = " 0.0%" )
lab_bb_raise_button.grid(column=1, row=7)

label4 = Label( root , text = " --- POSTFLOP SB --- #" + str(round(flop_counter)),fg='gold3')
label4.grid(column=0, row=8)

sb_cbet_button = Button( root , text = "cbet" , command = sb_cbet, fg='orange' )
sb_cbet_button.grid(column=0, row=9)
lab_sb_cbet_button = Label( root , text = " 0.0%" )
lab_sb_cbet_button.grid(column=1, row=9)

sb_check_button = Button( root , text = "check" , command = sb_check, fg='RoyalBlue3' )
sb_check_button.grid(column=0, row=10)
lab_sb_check_button = Label( root , text = " 0.0%" )
lab_sb_check_button.grid(column=1, row=10)

entry_new_villain = Entry(root)
entry_new_villain.grid(column=0, row=11)
save_new_villain_button = Button( root , text = "New" , command = new_vil )
save_new_villain_button.grid(column=1, row=11)
delete_villain_button = Button( root , text = "Delete" , command = del_vil )
delete_villain_button.grid(column=2, row=11)

# Execute tkinter
root.mainloop()
