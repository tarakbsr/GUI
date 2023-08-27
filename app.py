import tkinter as tk
from tkinter import Label, messagebox

import random

# ------Main GUI code---------

root = tk.Tk()
root.title('subject study')
root.geometry("700x660")
options1 = ["Male", "Female", "Divers"]
selected_option1 = tk.StringVar()
selected_option1.set(options1[0])
options2 = ["Experienced", "Beginner"]
selected_option2 = tk.StringVar()
selected_option2.set(options2[0])

#-------------------------- BUTTONS AND ENTRIES-------------------------------

                    # --------Create text entry name-------

el1 = tk.Label(root, text='Name', font=('calibre', 13), anchor='center').place(x=30, y=80)
entry1= tk.Entry(root,  font=('calibre', 12), width=30)
entry1.place(x=100, y=80)  

                    # --------Create text entry AGE-------
el2 = tk.Label(root, text='Age',font=('calibre', 13)).place(x=30, y=120)
entry2 = tk.Entry(root,   font=('calibre', 12), width=30)
entry2.place(x=100, y=120) 
                    # --------Create text entry Gender-------
el3 = tk.Label(root, text='Gender',font=('calibre', 13)).place(x=30, y=160)
optionmenu1 = tk.OptionMenu(root, selected_option1, *options1)
optionmenu1.place(x=100, y=160) 
                    # --------Create text entry Eperience-------
el4 = tk.Label(root, text='Experience',font=('calibre', 13)).place(x=30, y=200)
optionmenu2 = tk.OptionMenu(root, selected_option2, *options2)
optionmenu2.place(x=100, y=200)

                    # --------Create Button COLLECT DATA BUTTON1: Collect Data--------
button1 = tk.Button(root, text=' Collect data ', command=lambda: Label.config(text="Button Clicked!"))
button1.place(x=500, y=80)   

                    # --------Create Button PLOT DATA BUTTON1: PLOT Data--------
button2 = tk.Button(root, text='    Plot data  ', command=lambda: Label.config(text="Button Clicked!"))
button2.place(x=500, y=130)

                    # --------Create text entry SAVE Data-------
el3 = tk.Label(root, text='Filename', font=('calibre', 13)).place(x=60, y=183)
entry3 = tk.Entry(root, font=('calibre', 12), width = 15)
entry3.place(x=225, y=183)    

                    # --------Create Button SAVE DATA BUTTON1: SAVE Data--------
button3 = tk.Button(root, text='   Save data  ', command=lambda: Label.config(text="Button Clicked!"))
button3.place(x=500, y=180)
root.mainloop()
  