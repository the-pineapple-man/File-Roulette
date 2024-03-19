import random
import os
import tkinter as tk
from tkinter import filedialog

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        output_text.insert(tk.END, f"File '{file_name}' has been deleted.\n")
    else:
        output_text.insert(tk.END, f"File '{file_name}' not found.\n")

def roll_dice():
    number = random.randint(1, 6)
    output_text.insert(tk.END, f"Rolled number: {number}\n")
    if number == 6:
        file_name = entry.get()
        output_text.insert(tk.END, f"Attempting to delete file '{file_name}'...\n")
        if not file_name:
            output_text.insert(tk.END, "Please enter a file name.\n")
            return
        delete_file(file_name)

def browse_file():
    file_name = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_name)

root = tk.Tk()
root.geometry('400x300+50+50')
root.title("File Deletion Roulette")

label = tk.Label(root, text="Enter the file name to delete:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

btn_browse = tk.Button(root, text="Browse", command=browse_file)
btn_browse.pack()

btn_roll = tk.Button(root, text="Start Roulette", command=roll_dice)
btn_roll.pack()

output_text = tk.Text(root, height=10, width=40)
output_text.pack()

root.mainloop()
