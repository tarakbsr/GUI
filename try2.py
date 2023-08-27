import tkinter as tk
from tkinter import messagebox
import random

class LightingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lighting Control")

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.age_label = tk.Label(root, text="Age:")
        self.age_label.pack()

        self.age_entry = tk.Entry(root)
        self.age_entry.pack()

        self.rating_label = tk.Label(root, text="Rating:")
        self.rating_label.pack()

        self.rating_entry = tk.Entry(root)
        self.rating_entry.pack()

        self.dim_button = tk.Button(root, text="Dim", command=self.dim_lights)
        self.dim_button.pack()

        self.save_button = tk.Button(root, text="Save", command=self.save_data)
        self.save_button.pack()

        self.intensity_listbox = tk.Listbox(root)
        self.intensity_listbox.pack()

    def dim_lights(self):
        # Simulate random lighting intensities and add them to the listbox
        random_intensities = [random.randint(0, 100) for _ in range(10)]
        self.intensity_listbox.delete(0, tk.END)  # Clear previous entries
        for intensity in random_intensities:
            self.intensity_listbox.insert(tk.END, f"Intensity: {intensity}%")

    def save_data(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        rating = self.rating_entry.get()

        if name and age and rating:
            # You can customize the saving logic here (e.g., save to a file, database, etc.)
            messagebox.showinfo("Saved", "Data saved successfully!")
        else:
            messagebox.showwarning("Missing Fields", "Please fill in all fields before saving.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LightingApp(root)
    root.mainloop()
