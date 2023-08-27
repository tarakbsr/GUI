from cProfile import label
import serial as sr
import time
import numpy as np
import matplotlib.pyplot as plt 
from collections import defaultdict
import tkinter as tk
from ttkbootstrap import Style
from tkinter import Label, ttk
from ttkbootstrap.widgets import Meter
#import esp32_Code
import re

dct_collect = defaultdict(list) #dictionary for data collection


# ------Main GUI code---------
style = Style(theme='superhero')
root = style.master
root.title('Sole Measurements')
root.geometry("700x660")
style.configure('TButton', font= ('calibre', 13), borderwidth=4, foreground= 'white')
#-------------------------- BUTTONS AND ENTRIES-------------------------------

                    # --------Create text entry Collect Data-------
root.update()
el1 = ttk.Label(root, text='Time in seconds',style='info.TLabel', font=('calibre', 13), anchor='center').place(x=60, y=81)
entry1= ttk.Spinbox(root, from_=1, to=60, style='warning.TSpinbox', font=('calibre', 12), width=5)
entry1.place(x=225, y=80)    

                    # --------Create Button COLLECT DATA BUTTON1: Collect Data--------
root.update()
button1 = ttk.Button(root, text=' Collect data ', style='info.Outline.TButton', command=lambda: Label.config(text="Button Clicked!"))
button1.place(x=500, y=80)

                    # --------Create text entry NUMBER OF SENSORS-------
root.update()
el2 = ttk.Label(root, text='Number of sensors', style='info.TLabel',font=('calibre', 13)).place(x=60, y=133)
entry2 = ttk.Spinbox(root, from_=1, to=6, style='warning.TSpinbox', font=('calibre', 12), width=5)
entry2.place(x=225, y=133)    

                    # --------Create Button PLOT DATA BUTTON1: PLOT Data--------
root.update()
button2 = ttk.Button(root, text='    Plot data  ', style = 'info.Outline.TButton', command=lambda: label.config(text="Button Clicked!"))
button2.place(x=500, y=130)

                    # --------Create text entry SAVE Data-------
root.update()
el3 = ttk.Label(root, text='Filename',style='info.TLabel', font=('calibre', 13)).place(x=60, y=183)
entry3 = ttk.Entry(root, font=('calibre', 12), width = 15)
entry3.place(x=225, y=183)    

                    # --------Create Button SAVE DATA BUTTON1: SAVE Data--------
root.update()
button3 = ttk.Button(root, text='   Save data  ', style = 'info.Outline.TButton', command=lambda: label.config(text="Button Clicked!"))
button3.place(x=500, y=180)
root.mainloop()