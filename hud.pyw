
import os
# Import module
import shutil
from tkinter import *
from pathlib import Path
from PIL import ImageTk, Image

# Create object
root = Tk()
root.title("HUD")
root.iconbitmap("icons\chameleon_small.ico")

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

#chameleons
img_chameleons = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\chameleons.png"))

#not supported
img_not_supported = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\not_supported.png"))
chosen_img = img_chameleons

#open-fold sb
img_of_0_100      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_0_100.png"))
img_of_5_95       = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_5_95.png"))
img_of_10_90      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_10_90.png"))
img_of_15_85      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_15_85.png"))
img_of_20_80      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_20_80.png"))
img_of_25_75      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_25_75.png"))
img_of_30_70      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_30_70.png"))
img_of_35_65      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_35_65.png"))
img_of_40_60      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_40_60.png"))
img_of_45_55      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_45_55.png"))
img_of_50_50      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_50_50.png"))
img_of_55_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_55_45.png"))
img_of_60_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_60_40.png"))
img_of_65_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_65_35.png"))
img_of_70_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_70_30.png"))
img_of_75_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_75_25.png"))
img_of_80_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_80_20.png"))
img_of_85_15      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_85_15.png"))
img_of_90_10      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_90_10.png"))
img_of_95_5       = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_95_5.png"))
img_of_100_0      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\of_100_0.png"))

#Raise-Call-Fold bb
#Fold = 0
img_RCF_100_0_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_100_0_0.png"))
img_RCF_95_5_0    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_95_5_0.png"))
img_RCF_90_10_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_90_10_0.png"))
img_RCF_85_15_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_85_15_0.png"))
img_RCF_80_20_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_80_20_0.png"))
img_RCF_75_25_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_75_25_0.png"))
img_RCF_70_30_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_70_30_0.png"))
img_RCF_65_35_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_65_35_0.png"))
img_RCF_60_40_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_60_40_0.png"))
img_RCF_55_45_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_55_45_0.png"))
img_RCF_50_50_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_50_50_0.png"))
img_RCF_45_55_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_45_55_0.png"))
img_RCF_40_60_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_60_0.png"))
img_RCF_35_65_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_65_0.png"))
img_RCF_30_70_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_70_0.png"))
img_RCF_25_75_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_75_0.png"))
img_RCF_20_80_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_80_0.png"))
img_RCF_15_85_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_85_0.png"))
img_RCF_10_90_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_90_0.png"))
img_RCF_5_95_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_95_0.png"))
img_RCF_0_100_0   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_100_0.png"))

#Fold = 5
img_RCF_95_0_5    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_95_0_5.png"))
img_RCF_90_5_5    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_90_5_5.png"))
img_RCF_85_10_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_85_10_5.png"))
img_RCF_80_15_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_80_15_5.png"))
img_RCF_75_20_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_75_20_5.png"))
img_RCF_70_25_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_70_25_5.png"))
img_RCF_65_30_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_65_30_5.png"))
img_RCF_60_35_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_60_35_5.png"))
img_RCF_55_40_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_55_40_5.png"))
img_RCF_50_45_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_50_45_5.png"))
img_RCF_45_50_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_45_50_5.png"))
img_RCF_40_55_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_55_5.png"))
img_RCF_35_60_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_60_5.png"))
img_RCF_30_65_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_65_5.png"))
img_RCF_25_70_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_70_5.png"))
img_RCF_20_75_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_75_5.png"))
img_RCF_15_80_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_80_5.png"))
img_RCF_10_85_5   = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_85_5.png"))
img_RCF_5_90_5    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_90_5.png"))
img_RCF_0_95_5    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_95_5.png"))

#Fold = 10
img_RCF_90_0_10     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_90_0_10.png"))
img_RCF_85_5_10     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_85_5_10.png"))
img_RCF_80_10_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_80_10_10.png"))
img_RCF_75_15_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_75_15_10.png"))
img_RCF_70_20_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_70_20_10.png"))
img_RCF_65_25_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_65_25_10.png"))
img_RCF_60_30_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_60_30_10.png"))
img_RCF_55_35_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_55_35_10.png"))
img_RCF_50_40_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_50_40_10.png"))
img_RCF_45_45_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_45_45_10.png"))
img_RCF_40_50_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_50_10.png"))
img_RCF_35_55_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_55_10.png"))
img_RCF_30_60_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_60_10.png"))
img_RCF_25_65_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_65_10.png"))
img_RCF_20_70_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_70_10.png"))
img_RCF_15_75_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_75_10.png"))
img_RCF_10_80_10    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_80_10.png"))
img_RCF_5_85_10     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_85_10.png"))
img_RCF_0_90_10     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_90_10.png"))

#Fold = 15
img_RCF_85_0_15      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_85_0_15.png"))
img_RCF_80_5_15      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_80_5_15.png"))
img_RCF_75_10_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_75_10_15.png"))
img_RCF_70_15_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_70_15_15.png"))
img_RCF_65_20_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_65_20_15.png"))
img_RCF_60_25_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_60_25_15.png"))
img_RCF_55_30_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_55_30_15.png"))
img_RCF_50_35_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_50_35_15.png"))
img_RCF_45_40_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_45_40_15.png"))
img_RCF_40_45_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_45_15.png"))
img_RCF_35_50_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_50_15.png"))
img_RCF_30_55_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_55_15.png"))
img_RCF_25_60_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_60_15.png"))
img_RCF_20_65_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_65_15.png"))
img_RCF_15_70_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_70_15.png"))
img_RCF_10_75_15     = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_75_15.png"))
img_RCF_5_80_15      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_80_15.png"))
img_RCF_0_85_15      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_85_15.png"))

#Fold = 20
img_RCF_80_0_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_80_0_20.png"))
img_RCF_75_5_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_75_5_20.png"))
img_RCF_70_10_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_70_10_20.png"))
img_RCF_65_15_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_65_15_20.png"))
img_RCF_60_20_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_60_20_20.png"))
img_RCF_55_25_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_55_25_20.png"))
img_RCF_50_30_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_50_30_20.png"))
img_RCF_45_35_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_45_35_20.png"))
img_RCF_40_40_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_40_20.png"))
img_RCF_35_45_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_45_20.png"))
img_RCF_30_50_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_50_20.png"))
img_RCF_25_55_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_55_20.png"))
img_RCF_20_60_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_60_20.png"))
img_RCF_15_65_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_65_20.png"))
img_RCF_10_70_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_70_20.png"))
img_RCF_5_75_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_75_20.png"))
img_RCF_0_80_20      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_80_20.png"))

#Fold = 25
img_RCF_75_0_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_75_0_25.png"))
img_RCF_70_5_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_70_5_25.png"))
img_RCF_65_10_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_65_10_25.png"))
img_RCF_60_15_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_60_15_25.png"))
img_RCF_55_20_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_55_20_25.png"))
img_RCF_50_25_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_50_25_25.png"))
img_RCF_45_30_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_45_30_25.png"))
img_RCF_40_35_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_35_25.png"))
img_RCF_35_40_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_40_25.png"))
img_RCF_30_45_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_45_25.png"))
img_RCF_25_50_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_50_25.png"))
img_RCF_20_55_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_55_25.png"))
img_RCF_15_60_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_60_25.png"))
img_RCF_10_65_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_65_25.png"))
img_RCF_5_70_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_70_25.png"))
img_RCF_0_75_25      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_75_25.png"))

#Fold = 30
img_RCF_70_0_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_70_0_30.png"))
img_RCF_65_5_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_65_5_30.png"))
img_RCF_60_10_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_60_10_30.png"))
img_RCF_55_15_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_55_15_30.png"))
img_RCF_50_20_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_50_20_30.png"))
img_RCF_45_25_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_45_25_30.png"))
img_RCF_40_30_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_30_30.png"))
img_RCF_35_35_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_35_30.png"))
img_RCF_30_40_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_40_30.png"))
img_RCF_25_45_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_45_30.png"))
img_RCF_20_50_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_50_30.png"))
img_RCF_15_55_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_55_30.png"))
img_RCF_10_60_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_60_30.png"))
img_RCF_5_65_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_65_30.png"))
img_RCF_0_70_30      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_70_30.png"))

#Fold = 35
img_RCF_65_0_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_65_0_35.png"))
img_RCF_60_5_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_60_5_35.png"))
img_RCF_55_10_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_55_10_35.png"))
img_RCF_50_15_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_50_15_35.png"))
img_RCF_45_20_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_45_20_35.png"))
img_RCF_40_25_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_25_35.png"))
img_RCF_35_30_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_30_35.png"))
img_RCF_30_35_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_35_35.png"))
img_RCF_25_40_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_40_35.png"))
img_RCF_20_45_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_45_35.png"))
img_RCF_15_50_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_50_35.png"))
img_RCF_10_55_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_55_35.png"))
img_RCF_5_60_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_60_35.png"))
img_RCF_0_65_35      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_65_35.png"))

#Fold = 40
img_RCF_60_0_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_60_0_40.png"))
img_RCF_55_5_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_55_5_40.png"))
img_RCF_50_10_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_50_10_40.png"))
img_RCF_45_15_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_45_15_40.png"))
img_RCF_40_20_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_20_40.png"))
img_RCF_35_25_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_25_40.png"))
img_RCF_30_30_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_30_40.png"))
img_RCF_25_35_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_35_40.png"))
img_RCF_20_40_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_40_40.png"))
img_RCF_15_45_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_45_40.png"))
img_RCF_10_50_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_50_40.png"))
img_RCF_5_55_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_55_40.png"))
img_RCF_0_60_40      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_60_40.png"))

#Fold = 45
img_RCF_55_0_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_55_0_45.png"))
img_RCF_50_5_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_50_5_45.png"))
img_RCF_45_10_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_45_10_45.png"))
img_RCF_40_15_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_15_45.png"))
img_RCF_35_20_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_20_45.png"))
img_RCF_30_25_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_25_45.png"))
img_RCF_25_30_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_30_45.png"))
img_RCF_20_35_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_35_45.png"))
img_RCF_15_40_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_40_45.png"))
img_RCF_10_45_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_45_45.png"))
img_RCF_5_50_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_50_45.png"))
img_RCF_0_55_45      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_55_45.png"))

#Fold = 50
img_RCF_50_0_50      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_50_0_50.png"))
img_RCF_45_5_50      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_45_5_50.png"))
img_RCF_40_10_50      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_10_50.png"))
img_RCF_35_15_50      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_15_50.png"))
img_RCF_30_20_50      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_20_50.png"))
img_RCF_25_25_50      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_25_50.png"))
img_RCF_20_30_50      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_30_50.png"))
img_RCF_15_35_50      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_35_50.png"))
img_RCF_10_40_50      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_40_50.png"))
img_RCF_5_45_50      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_45_50.png"))
img_RCF_0_50_50      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_50_50.png"))

#Fold = 55
img_RCF_45_0_55      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_45_0_55.png"))
img_RCF_40_5_55      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_5_55.png"))
img_RCF_35_10_55      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_10_55.png"))
img_RCF_30_15_55      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_15_55.png"))
img_RCF_25_20_55      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_20_55.png"))
img_RCF_20_25_55      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_25_55.png"))
img_RCF_15_30_55      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_30_55.png"))
img_RCF_10_35_55      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_35_55.png"))
img_RCF_5_40_55      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_40_55.png"))
img_RCF_0_45_55      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_45_55.png"))

#Fold = 60
img_RCF_40_0_60      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_40_0_60.png"))
img_RCF_35_5_60      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_5_60.png"))
img_RCF_30_10_60      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_10_60.png"))
img_RCF_25_15_60      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_15_60.png"))
img_RCF_20_20_60      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_20_60.png"))
img_RCF_15_25_60      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_25_60.png"))
img_RCF_10_30_60      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_30_60.png"))
img_RCF_5_35_60      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_35_60.png"))
img_RCF_0_40_60      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_40_60.png"))

#Fold = 65
img_RCF_35_0_65      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_35_0_65.png"))
img_RCF_30_5_65      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_5_65.png"))
img_RCF_25_10_65      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_10_65.png"))
img_RCF_20_15_65      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_15_65.png"))
img_RCF_15_20_65      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_20_65.png"))
img_RCF_10_25_65      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_25_65.png"))
img_RCF_5_30_65      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_30_65.png"))
img_RCF_0_35_65      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_35_65.png"))

#Fold = 70
img_RCF_30_0_70      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_30_0_70.png"))
img_RCF_25_5_70      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_5_70.png"))
img_RCF_20_10_70      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_10_70.png"))
img_RCF_15_15_70      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_15_70.png"))
img_RCF_10_20_70      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_20_70.png"))
img_RCF_5_25_70      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_25_70.png"))
img_RCF_0_30_70      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_30_70.png"))

#Fold = 75
img_RCF_25_0_75      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_25_0_75.png"))
img_RCF_20_5_75      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_5_75.png"))
img_RCF_15_10_75      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_10_75.png"))
img_RCF_10_15_75      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_15_75.png"))
img_RCF_5_20_75      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_20_75.png"))
img_RCF_0_25_75      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_25_75.png"))

#Fold = 80
img_RCF_20_0_80      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_20_0_80.png"))
img_RCF_15_5_80      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_5_80.png"))
img_RCF_10_10_80      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_10_80.png"))
img_RCF_5_15_80      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_15_80.png"))
img_RCF_0_20_80      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_20_80.png"))

#Fold = 85
img_RCF_15_0_85      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_15_0_85.png"))
img_RCF_10_5_85      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_5_85.png"))
img_RCF_5_10_85      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_10_85.png"))
img_RCF_0_15_85      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_15_85.png"))

#Fold = 90
img_RCF_10_0_90      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_10_0_90.png"))
img_RCF_5_5_90      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_5_90.png"))
img_RCF_0_10_90      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_10_90.png"))

#Fold = 95
img_RCF_5_0_95      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_5_0_95.png"))
img_RCF_0_5_95      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_5_95.png"))

#Fold = 100
img_RCF_0_0_100      = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\RCF_0_0_100.png"))

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
root.geometry( "440x305" )

def constructRCF(r,c,f):
    temp_img = img_not_supported
    # Fold = 0
    if f < 1:
        if c < 1:
            temp_img = img_RCF_100_0_0
        elif c < 6:
            temp_img = img_RCF_95_5_0
        elif c < 11:
            temp_img = img_RCF_90_10_0
        elif c < 16:
            temp_img = img_RCF_85_15_0
        elif c < 21:
            temp_img = img_RCF_80_20_0
        elif c < 26:
            temp_img = img_RCF_75_25_0
        elif c < 31:
            temp_img = img_RCF_70_30_0
        elif c < 36:
            temp_img = img_RCF_65_35_0
        elif c < 41:
            temp_img = img_RCF_60_40_0
        elif c < 46:
            temp_img = img_RCF_55_45_0
        elif c < 51:
            temp_img = img_RCF_50_50_0
        elif c < 56:
            temp_img = img_RCF_45_55_0
        elif c < 61:
            temp_img = img_RCF_40_60_0
        elif c < 67:
            temp_img = img_RCF_35_65_0
        elif c < 71:
            temp_img = img_RCF_30_70_0
        elif c < 76:
            temp_img = img_RCF_25_75_0
        elif c < 81:
            temp_img = img_RCF_20_80_0
        elif c < 86:
            temp_img = img_RCF_15_85_0
        elif c < 91:
            temp_img = img_RCF_10_90_0
        elif c < 96:
            temp_img = img_RCF_5_95_0
        elif c < 101:
            temp_img = img_RCF_0_100_0
        else:
            temp_img = img_not_supported
    # Fold = 5
    elif f < 6:
        if c < 1:
            temp_img = img_RCF_95_0_5
        elif c < 6:
            temp_img = img_RCF_90_5_5
        elif c < 11:
            temp_img = img_RCF_85_10_5
        elif c < 16:
            temp_img = img_RCF_80_15_5
        elif c < 21:
            temp_img = img_RCF_75_20_5
        elif c < 26:
            temp_img = img_RCF_70_25_5
        elif c < 31:
            temp_img = img_RCF_65_30_5
        elif c < 36:
            temp_img = img_RCF_60_35_5
        elif c < 41:
            temp_img = img_RCF_55_40_5
        elif c < 46:
            temp_img = img_RCF_50_45_5
        elif c < 51:
            temp_img = img_RCF_45_50_5
        elif c < 56:
            temp_img = img_RCF_40_55_5
        elif c < 61:
            temp_img = img_RCF_35_60_5
        elif c < 67:
            temp_img = img_RCF_30_65_5
        elif c < 71:
            temp_img = img_RCF_25_70_5
        elif c < 76:
            temp_img = img_RCF_20_75_5
        elif c < 81:
            temp_img = img_RCF_15_80_5
        elif c < 86:
            temp_img = img_RCF_10_85_5
        elif c < 91:
            temp_img = img_RCF_5_90_5
        elif c < 96:
            temp_img = img_RCF_0_95_5
        else:
            temp_img = img_not_supported
    # Fold = 10
    elif f < 11:
        if c < 1:
            temp_img = img_RCF_90_0_10
        elif c < 6:
            temp_img = img_RCF_85_5_10
        elif c < 11:
            temp_img = img_RCF_80_10_10
        elif c < 16:
            temp_img = img_RCF_75_15_10
        elif c < 21:
            temp_img = img_RCF_70_20_10
        elif c < 26:
            temp_img = img_RCF_65_25_10
        elif c < 31:
            temp_img = img_RCF_60_30_10
        elif c < 36:
            temp_img = img_RCF_55_35_10
        elif c < 41:
            temp_img = img_RCF_50_40_10
        elif c < 46:
            temp_img = img_RCF_45_45_10
        elif c < 51:
            temp_img = img_RCF_40_50_10
        elif c < 56:
            temp_img = img_RCF_35_55_10
        elif c < 61:
            temp_img = img_RCF_30_60_10
        elif c < 67:
            temp_img = img_RCF_25_65_10
        elif c < 71:
            temp_img = img_RCF_20_70_10
        elif c < 76:
            temp_img = img_RCF_15_75_10
        elif c < 81:
            temp_img = img_RCF_10_80_10
        elif c < 86:
            temp_img = img_RCF_5_85_10
        elif c < 91:
            temp_img = img_RCF_0_90_10
        else:
            temp_img = img_not_supported
    # Fold = 15
    elif f < 16:
        if c < 1:
            temp_img = img_RCF_85_0_15
        elif c < 6:
            temp_img = img_RCF_80_5_15
        elif c < 11:
            temp_img = img_RCF_75_10_15
        elif c < 16:
            temp_img = img_RCF_70_15_15
        elif c < 21:
            temp_img = img_RCF_65_20_15
        elif c < 26:
            temp_img = img_RCF_60_25_15
        elif c < 31:
            temp_img = img_RCF_55_30_15
        elif c < 36:
            temp_img = img_RCF_50_35_15
        elif c < 41:
            temp_img = img_RCF_45_40_15
        elif c < 46:
            temp_img = img_RCF_40_45_15
        elif c < 51:
            temp_img = img_RCF_35_50_15
        elif c < 56:
            temp_img = img_RCF_30_55_15
        elif c < 61:
            temp_img = img_RCF_25_60_15
        elif c < 67:
            temp_img = img_RCF_20_65_15
        elif c < 71:
            temp_img = img_RCF_15_70_15
        elif c < 76:
            temp_img = img_RCF_10_75_15
        elif c < 81:
            temp_img = img_RCF_5_80_15
        elif c < 86:
            temp_img = img_RCF_0_85_15
        else:
            temp_img = img_not_supported
    # Fold = 20
    elif f < 21:
        if c < 1:
            temp_img = img_RCF_80_0_20
        elif c < 6:
            temp_img = img_RCF_75_5_20
        elif c < 11:
            temp_img = img_RCF_70_10_20
        elif c < 16:
            temp_img = img_RCF_65_15_20
        elif c < 21:
            temp_img = img_RCF_60_20_20
        elif c < 26:
            temp_img = img_RCF_55_25_20
        elif c < 31:
            temp_img = img_RCF_50_30_20
        elif c < 36:
            temp_img = img_RCF_45_35_20
        elif c < 41:
            temp_img = img_RCF_40_40_20
        elif c < 46:
            temp_img = img_RCF_35_45_20
        elif c < 51:
            temp_img = img_RCF_30_50_20
        elif c < 56:
            temp_img = img_RCF_25_55_20
        elif c < 61:
            temp_img = img_RCF_20_60_20
        elif c < 67:
            temp_img = img_RCF_15_65_20
        elif c < 71:
            temp_img = img_RCF_10_70_20
        elif c < 76:
            temp_img = img_RCF_5_75_20
        elif c < 81:
            temp_img = img_RCF_0_80_20
        else:
            temp_img = img_not_supported
    # Fold = 25
    elif f < 26:
        if c < 1:
            temp_img = img_RCF_75_0_25
        elif c < 6:
            temp_img = img_RCF_70_5_25
        elif c < 11:
            temp_img = img_RCF_65_10_25
        elif c < 16:
            temp_img = img_RCF_60_15_25
        elif c < 21:
            temp_img = img_RCF_55_20_25
        elif c < 26:
            temp_img = img_RCF_50_25_25
        elif c < 31:
            temp_img = img_RCF_45_30_25
        elif c < 36:
            temp_img = img_RCF_40_35_25
        elif c < 41:
            temp_img = img_RCF_35_40_25
        elif c < 46:
            temp_img = img_RCF_30_45_25
        elif c < 51:
            temp_img = img_RCF_25_50_25
        elif c < 56:
            temp_img = img_RCF_20_55_25
        elif c < 61:
            temp_img = img_RCF_15_60_25
        elif c < 67:
            temp_img = img_RCF_10_65_25
        elif c < 71:
            temp_img = img_RCF_5_70_25
        elif c < 76:
            temp_img = img_RCF_0_75_25
        else:
            temp_img = img_not_supported
    # Fold = 30
    elif f < 31:
        if c < 1:
            temp_img = img_RCF_77_0_30
        elif c < 6:
            temp_img = img_RCF_65_5_30
        elif c < 11:
            temp_img = img_RCF_60_10_30
        elif c < 16:
            temp_img = img_RCF_55_15_30
        elif c < 21:
            temp_img = img_RCF_50_20_30
        elif c < 26:
            temp_img = img_RCF_45_25_30
        elif c < 31:
            temp_img = img_RCF_40_30_30
        elif c < 36:
            temp_img = img_RCF_35_35_30
        elif c < 41:
            temp_img = img_RCF_30_40_30
        elif c < 46:
            temp_img = img_RCF_25_45_30
        elif c < 51:
            temp_img = img_RCF_20_50_30
        elif c < 56:
            temp_img = img_RCF_15_55_30
        elif c < 61:
            temp_img = img_RCF_10_60_30
        elif c < 67:
            temp_img = img_RCF_5_65_30
        elif c < 71:
            temp_img = img_RCF_0_70_30
        else:
            temp_img = img_not_supported
    # Fold = 35
    elif f < 36:
        if c < 1:
            temp_img = img_RCF_65_0_35
        elif c < 6:
            temp_img = img_RCF_60_5_35
        elif c < 11:
            temp_img = img_RCF_55_10_35
        elif c < 16:
            temp_img = img_RCF_50_15_35
        elif c < 21:
            temp_img = img_RCF_45_20_35
        elif c < 26:
            temp_img = img_RCF_40_25_35
        elif c < 31:
            temp_img = img_RCF_35_30_35
        elif c < 36:
            temp_img = img_RCF_30_35_35
        elif c < 41:
            temp_img = img_RCF_25_40_35
        elif c < 46:
            temp_img = img_RCF_20_45_35
        elif c < 51:
            temp_img = img_RCF_15_50_35
        elif c < 56:
            temp_img = img_RCF_10_55_35
        elif c < 61:
            temp_img = img_RCF_5_60_35
        elif c < 67:
            temp_img = img_RCF_0_65_35
        else:
            temp_img = img_not_supported
    # Fold = 40
    elif f < 41:
        if c < 1:
            temp_img = img_RCF_60_0_40
        elif c < 6:
            temp_img = img_RCF_55_5_40
        elif c < 11:
            temp_img = img_RCF_50_10_40
        elif c < 16:
            temp_img = img_RCF_45_15_40
        elif c < 21:
            temp_img = img_RCF_40_20_40
        elif c < 26:
            temp_img = img_RCF_35_25_40
        elif c < 31:
            temp_img = img_RCF_30_30_40
        elif c < 36:
            temp_img = img_RCF_25_35_40
        elif c < 41:
            temp_img = img_RCF_20_40_40
        elif c < 46:
            temp_img = img_RCF_15_45_40
        elif c < 51:
            temp_img = img_RCF_10_50_40
        elif c < 56:
            temp_img = img_RCF_5_55_40
        elif c < 61:
            temp_img = img_RCF_0_60_40
        else:
            temp_img = img_not_supported
    # Fold = 45
    elif f < 46:
        if c < 1:
            temp_img = img_RCF_55_0_45
        elif c < 6:
            temp_img = img_RCF_50_5_45
        elif c < 11:
            temp_img = img_RCF_45_10_45
        elif c < 16:
            temp_img = img_RCF_40_15_45
        elif c < 21:
            temp_img = img_RCF_35_20_45
        elif c < 26:
            temp_img = img_RCF_30_25_45
        elif c < 31:
            temp_img = img_RCF_25_30_45
        elif c < 36:
            temp_img = img_RCF_20_35_45
        elif c < 41:
            temp_img = img_RCF_15_40_45
        elif c < 46:
            temp_img = img_RCF_10_45_45
        elif c < 51:
            temp_img = img_RCF_5_50_45
        elif c < 56:
            temp_img = img_RCF_0_55_45
        else:
            temp_img = img_not_supported
    # Fold = 50
    elif f < 51:
        if c < 1:
            temp_img = img_RCF_50_0_50
        elif c < 6:
            temp_img = img_RCF_45_5_50
        elif c < 11:
            temp_img = img_RCF_40_10_50
        elif c < 16:
            temp_img = img_RCF_35_15_50
        elif c < 21:
            temp_img = img_RCF_30_20_50
        elif c < 26:
            temp_img = img_RCF_25_25_50
        elif c < 31:
            temp_img = img_RCF_20_30_50
        elif c < 36:
            temp_img = img_RCF_15_35_50
        elif c < 41:
            temp_img = img_RCF_10_40_50
        elif c < 46:
            temp_img = img_RCF_5_45_50
        elif c < 51:
            temp_img = img_RCF_0_50_50
        else:
            temp_img = img_not_supported
    # Fold = 55
    elif f < 56:
        if c < 1:
            temp_img = img_RCF_45_0_55
        elif c < 6:
            temp_img = img_RCF_40_5_55
        elif c < 11:
            temp_img = img_RCF_35_10_55
        elif c < 16:
            temp_img = img_RCF_30_15_55
        elif c < 21:
            temp_img = img_RCF_25_20_55
        elif c < 26:
            temp_img = img_RCF_20_25_55
        elif c < 31:
            temp_img = img_RCF_15_30_55
        elif c < 36:
            temp_img = img_RCF_10_35_55
        elif c < 41:
            temp_img = img_RCF_5_40_55
        elif c < 46:
            temp_img = img_RCF_0_45_55
        else:
            temp_img = img_not_supported
    # Fold = 60
    elif f < 61:
        if c < 1:
            temp_img = img_RCF_40_0_60
        elif c < 6:
            temp_img = img_RCF_35_5_60
        elif c < 11:
            temp_img = img_RCF_30_10_60
        elif c < 16:
            temp_img = img_RCF_25_15_60
        elif c < 21:
            temp_img = img_RCF_20_20_60
        elif c < 26:
            temp_img = img_RCF_15_25_60
        elif c < 31:
            temp_img = img_RCF_10_30_60
        elif c < 36:
            temp_img = img_RCF_5_35_60
        elif c < 41:
            temp_img = img_RCF_0_40_60
        else:
            temp_img = img_not_supported
    # Fold = 65
    elif f < 67:
        if c < 1:
            temp_img = img_RCF_35_0_65
        elif c < 6:
            temp_img = img_RCF_30_5_65
        elif c < 11:
            temp_img = img_RCF_25_10_65
        elif c < 16:
            temp_img = img_RCF_20_15_65
        elif c < 21:
            temp_img = img_RCF_15_20_65
        elif c < 26:
            temp_img = img_RCF_10_25_65
        elif c < 31:
            temp_img = img_RCF_5_30_65
        elif c < 36:
            temp_img = img_RCF_0_35_65
        else:
            temp_img = img_not_supported
    # Fold = 70
    elif f < 71:
        if c < 1:
            temp_img = img_RCF_30_0_70
        elif c < 6:
            temp_img = img_RCF_25_5_70
        elif c < 11:
            temp_img = img_RCF_20_10_70
        elif c < 16:
            temp_img = img_RCF_15_15_70
        elif c < 21:
            temp_img = img_RCF_10_20_70
        elif c < 26:
            temp_img = img_RCF_5_25_70
        elif c < 31:
            temp_img = img_RCF_0_30_70
        else:
            temp_img = img_not_supported
    # Fold = 75
    elif f < 76:
        if c < 1:
            temp_img = img_RCF_25_0_75
        elif c < 6:
            temp_img = img_RCF_20_5_75
        elif c < 11:
            temp_img = img_RCF_15_10_75
        elif c < 16:
            temp_img = img_RCF_10_15_75
        elif c < 21:
            temp_img = img_RCF_5_20_75
        elif c < 26:
            temp_img = img_RCF_0_25_75
        else:
            temp_img = img_not_supported
    # Fold = 80
    elif f < 81:
        if c < 1:
            temp_img = img_RCF_20_0_80
        elif c < 6:
            temp_img = img_RCF_15_5_80
        elif c < 11:
            temp_img = img_RCF_10_10_80
        elif c < 16:
            temp_img = img_RCF_5_15_80
        elif c < 21:
            temp_img = img_RCF_0_20_80
        else:
            temp_img = img_not_supported
    # Fold = 85
    elif f < 86:
        if c < 1:
            temp_img = img_RCF_15_0_85
        elif c < 6:
            temp_img = img_RCF_10_5_85
        elif c < 11:
            temp_img = img_RCF_5_10_85
        elif c < 16:
            temp_img = img_RCF_0_15_85
        else:
            temp_img = img_not_supported
    # Fold = 90
    elif f < 91:
        if c < 1:
            temp_img = img_RCF_10_0_90
        elif c < 6:
            temp_img = img_RCF_5_5_90
        elif c < 11:
            temp_img = img_RCF_0_10_90
        else:
            temp_img = img_not_supported
    # Fold = 95
    elif f < 96:
        if c < 1:
            temp_img = img_RCF_5_0_95
        elif c < 6:
            temp_img = img_RCF_0_5_95
        else:
            temp_img = img_not_supported
    # Fold = 100
    elif f < 101:
        if c < 1:
            temp_img = img_RCF_0_0_100
        else:
            temp_img = img_not_supported
    else:
            temp_img = img_not_supported
    return temp_img

def construct_of(o,f):
    temp_img = img_not_supported
    if o > 96:
        temp_img = img_of_100_0
    elif o > 91:
        temp_img = img_of_95_5
    elif o > 86:
        temp_img = img_of_90_10
    elif o > 81:
        temp_img = img_of_85_15
    elif o > 76:
        temp_img = img_of_80_20
    elif o > 71:
        temp_img = img_of_75_25
    elif o > 67:
        temp_img = img_of_70_30
    elif o > 61:
        temp_img = img_of_65_35
    elif o > 56:
        temp_img = img_of_60_40
    elif o > 51:
        temp_img = img_of_55_45
    elif o > 46:
        temp_img = img_of_50_50
    elif o > 41:
        temp_img = img_of_45_55
    elif o > 36:
        temp_img = img_of_40_60
    elif o > 31:
        temp_img = img_of_35_65
    elif o > 26:
        temp_img = img_of_30_70
    elif o > 21:
        temp_img = img_of_25_75
    elif o > 16:
        temp_img = img_of_20_80
    elif o > 11:
        temp_img = img_of_15_85
    elif o > 6:
        temp_img = img_of_10_90
    elif o > 1:
        temp_img = img_of_5_95
    else:
        temp_img = img_of_0_100
    return temp_img

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

    #preflop open %
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

    #Update also preflop fold %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_fold.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\preflop_sb_fold.txt", "r")
        sb_pre_fold_counter = float(f.read())
        f.close()
        if sb_preflop_sum < 1:
            lab_sb_fold_button.config(text = " 0.0%")
        else:
            lab_sb_fold_button.config(text = " " + str(round(sb_pre_fold_counter/sb_preflop_sum * 100,1)) + "%")
    chosen_img = construct_of(round(sb_pre_open_counter/sb_preflop_sum * 100,1),round(sb_pre_fold_counter/sb_preflop_sum * 100,1))
    label_image.config(image = chosen_img)

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
    chosen_img = construct_of(round(sb_pre_open_counter/sb_preflop_sum * 100,1),round(sb_pre_fold_counter/sb_preflop_sum * 100,1))
    label_image.config(image = chosen_img)

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
    chosen_img = constructRCF(round(bb_pre_raise_counter/bb_preflop_sum * 100,1),round(bb_pre_call_counter/bb_preflop_sum * 100,1),round(bb_pre_fold_counter/bb_preflop_sum * 100,1))
    label_image.config(image = chosen_img)
    

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
    chosen_img = constructRCF(round(bb_pre_raise_counter/bb_preflop_sum * 100,1),round(bb_pre_call_counter/bb_preflop_sum * 100,1),round(bb_pre_fold_counter/bb_preflop_sum * 100,1))
    label_image.config(image = chosen_img)

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
    chosen_img = constructRCF(round(bb_pre_raise_counter/bb_preflop_sum * 100,1),round(bb_pre_call_counter/bb_preflop_sum * 100,1),round(bb_pre_fold_counter/bb_preflop_sum * 100,1))
    label_image.config(image = chosen_img)

#SB Postflop
def sb_cbet():
    global sb_postflop_sum
    global sb_post_cbet_counter
    global sb_post_check_counter

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
    
    #postflop cbet %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_cbet.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_cbet.txt", "r")
        sb_post_cbet_counter = float(f.read())
        f.close()
    sb_post_cbet_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_cbet.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_cbet.txt", "w")
        f.write(str(sb_post_cbet_counter))
        f.close()
        if sb_postflop_sum < 1:
            lab_sb_cbet_button.config(text = "0.0%")
        else:
            lab_sb_cbet_button.config(text = " " + str(round(sb_post_cbet_counter/sb_postflop_sum * 100,1)) + "%")
    #update also postflop check %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_check.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_check.txt", "r")
        sb_post_check_counter = float(f.read())
        f.close()
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_check.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_check.txt", "w")
        f.write(str(sb_post_check_counter))
        f.close()
        if sb_postflop_sum < 1:
            lab_sb_check_button.config(text = "0.0%")
        else:
            lab_sb_check_button.config(text = " " + str(round(sb_post_check_counter/sb_postflop_sum * 100,1)) + "%")

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

    #update check %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_check.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_check.txt", "r")
        sb_post_check_counter = float(f.read())
        f.close()
        sb_post_check_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_check.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_check.txt", "w")
        f.write(str(sb_post_check_counter))
        f.close()
        if sb_postflop_sum < 1:
            lab_sb_check_button.config(text = "0.0%")
        else:
            lab_sb_check_button.config(text = " " + str(round(sb_post_check_counter/sb_postflop_sum * 100,1)) + "%")
    #postflop also cbet %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_cbet.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_cbet.txt", "r")
        sb_post_cbet_counter = float(f.read())
        f.close()
    #sb_post_cbet_counter += 1
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_cbet.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_cbet.txt", "w")
        f.write(str(sb_post_cbet_counter))
        f.close()
        if sb_postflop_sum < 1:
            lab_sb_cbet_button.config(text = "0.0%")
        else:
            lab_sb_cbet_button.config(text = " " + str(round(sb_post_cbet_counter/sb_postflop_sum * 100,1)) + "%")


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
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_counter.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_counter.txt", "r")
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
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_cbet.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_cbet.txt", "r")
        sb_post_cbet_counter = float(f.read())
        f.close()
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_cbet.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_cbet.txt", "w")
        f.write(str(sb_post_cbet_counter))
        f.close()
        if sb_postflop_sum < 1:
            lab_sb_cbet_button.config(text = " 0.0%")
        else:
            lab_sb_cbet_button.config(text = " " + str(round(sb_post_cbet_counter/sb_postflop_sum * 100,1)) + "%")
    #postlop sb check %
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_check.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_check.txt", "r")
        sb_post_check_counter = float(f.read())
        f.close()
    if os.path.isfile(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_check.txt"):
        f = open(cwd + "\\villains\\" + chosen_one + "\\postflop_sb_check.txt", "w")
        f.write(str(sb_post_check_counter))
        f.close()
        if sb_postflop_sum < 1:
            lab_sb_check_button.config(text = " 0.0%")
        else:
            lab_sb_check_button.config(text = " " + str(round(sb_post_check_counter/sb_postflop_sum * 100,1)) + "%")

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

label_image = Label(root, image = chosen_img)
label_image.grid(row=1, column=2, columnspan=10, rowspan=10,
           sticky=W+E+N+S, padx=5, pady=5)


# Execute tkinter
root.mainloop()
