import tkinter as tk
from tkinter import Label, ttk
from tkinter import messagebox

def button_click(button):
    # Change the button color to green
    button.config(bg='green')
    # After a delay, reset the button color to its original state
    window.after(10, lambda: reset_button_color(button))

def reset_button_color(button):
    button.config(bg=original_button_color)

window = tk.Tk()
window.title("Subject study ")
window.geometry("700x660")

frame = tk.Frame(window)
frame.pack()




original_button_color = window.cget('bg')

# Saving User Info
user_info_frame =tk.LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tk.Label(user_info_frame, text=" Name")
first_name_label.grid(row=0, column=0)
Gender_label = tk.Label(user_info_frame, text="Gender")
Gender_label.grid(row=0, column=1)

first_name_entry = tk.Entry(user_info_frame)
Gender_combobox = ttk.Combobox(user_info_frame, values=["Male", "Female", "Divers"])
first_name_entry.grid(row=1, column=0)
Gender_combobox.grid(row=1, column=1)

Correction_label = tk.Label(user_info_frame, text="Correction")
Correction_combobox = ttk.Combobox(user_info_frame, values=["None", "glasses", "contact lenses",])
Correction_label.grid(row=0, column=2)
Correction_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, text="Age")
age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

Experience_label = tk.Label(user_info_frame, text="Experience")
Experience_combobox = ttk.Combobox(user_info_frame, values=["beginner", "Experienced"])
Experience_label.grid(row=2, column=1)
Experience_combobox.grid(row=3, column=1)


# Saving Ratings
Rating_frame = tk.LabelFrame(frame)
Rating_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

ratebrightness_label = tk.Label(Rating_frame, text= "brightness Rate")
ratebrightness_spinbox = tk.Spinbox(Rating_frame, from_=1, to=9)
ratebrightness_label.grid(row=0, column=0)
ratebrightness_spinbox.grid(row=1, column=0)

ratevisiblity_label = tk.Label(Rating_frame, text="visibilty Rate")
ratevisiblity_spinbox = tk.Spinbox(Rating_frame, from_=1, to=9)
ratevisiblity_label.grid(row=0, column=1)
ratevisiblity_spinbox.grid(row=1, column=1)


save_button = tk.Button(Rating_frame, text="Save")
save_button.grid( row=1,column=2)



# dimming 
dimming_frame = tk.LabelFrame(frame, text="Dimming")
dimming_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

dimLeft_button = tk.Button(dimming_frame, text="Dim Left")
dimLeft_button.grid( row=1,column=0)
dimRight_button = tk.Button(dimming_frame, text="Dim Right")
dimRight_button.grid( row=1,column=1)

# Save data
Data_button = tk.Button(frame, text="Save data")
Data_button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
connect_button = ttk.Button(frame, text="connect Rb" ,command=lambda: button_click(connect_button))
connect_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
