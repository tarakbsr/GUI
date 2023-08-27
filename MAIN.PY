import tkinter as tk
root = tk.Tk()
root.title("")
root.geometry("700x660")

# Create a label widget
label = tk.Label(root, text='Time in seconds', font=('calibre', 13), anchor='center').place(x=60, y=81)


# Create a button widget
button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack()

# Start the GUI event loop
root.mainloop()