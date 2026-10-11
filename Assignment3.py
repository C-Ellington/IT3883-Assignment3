# Program Name: Assignment3.py
# Course: IT3883
# Student Name: Cobyanne Ellington
# Assignment Number: Assignment 3
# Due Date: 10/10/26
# Purpose: This program converts miles per gallon into kilometers per liter using a GUI
# Resources: Course notes and Python textbook

import tkinter as tk


# Converts MPG to km/L
def convert(event=None):
    mpg = entry.get()

    # Clears result if box is empty
    if mpg == "":
        result.config(text="")
        return

    try:
        mpg = float(mpg)
        kml = mpg * 0.425143707
        result.config(text=f"{kml:.2f} km/L")

    # Handles letters or bad input
    except ValueError:
        result.config(text="Invalid input")


# Creates window
window = tk.Tk()
window.title("MPG Converter")
window.geometry("300x170")

# MPG label
label1 = tk.Label(window, text="Miles per Gallon:")
label1.pack(pady=(20, 5))

# Inputs box
entry = tk.Entry(window)
entry.pack()

# km/L label
label2 = tk.Label(window, text="Kilometers per Liter:")
label2.pack(pady=(15, 5))

# Result!
result = tk.Label(window, text="")
result.pack()

# Update when user types:
entry.bind("<KeyRelease>", convert)

# Keeps the window open:
window.mainloop()