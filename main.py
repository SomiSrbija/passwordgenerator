import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip
import tkinter.messagebox as messagebox

def generate_password():
    length = int(length_entry.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    messagebox.showinfo("Generated Password", password)
    pyperclip.copy(password)

root = tk.Tk()
root.title("Password Generator")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the center position of the root window
x = (screen_width - 400) // 2
y = (screen_height - 300) // 2

# Set the size and position of the root window
root.geometry(f"300x200+{x}+{y}")
# Create a themed style
style = ttk.Style(root)
style.theme_use("default")

frame = ttk.Frame(root, padding=10)
frame.pack()

length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky="w")

length_entry = ttk.Entry(frame)
length_entry.grid(row=0, column=1, sticky="w")

lowercase_var = tk.IntVar()
lowercase_checkbox = ttk.Checkbutton(frame, text="Include Lowercase", variable=lowercase_var)
lowercase_checkbox.grid(row=1, column=0, sticky="w")

uppercase_var = tk.IntVar()
uppercase_checkbox = ttk.Checkbutton(frame, text="Include Uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=2, column=0, sticky="w")

digits_var = tk.IntVar()
digits_checkbox = ttk.Checkbutton(frame, text="Include Digits", variable=digits_var)
digits_checkbox.grid(row=3, column=0, sticky="w")

symbols_var = tk.IntVar()
symbols_checkbox = ttk.Checkbutton(frame, text="Include Symbols", variable=symbols_var)
symbols_checkbox.grid(row=4, column=0, sticky="w")

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)



root.mainloop()
