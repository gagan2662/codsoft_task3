import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_special_chars):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length < 6:
            messagebox.showerror("Error", "Password length should be at least 6 characters.")
            return
        use_special_chars = special_chars_var.get()
        password = generate_password(length, use_special_chars)
        password_entry.config(state='normal')
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state='readonly')
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")
root.minsize(300,300)
root.configure(bg="#ffab91")

length_label = tk.Label(root, text="Enter Password Length", font=("Calibri",14,"bold"), bg="#ffab91")
length_label.pack(padx=10, pady=10)

length_entry = tk.Entry(root, width=20)
length_entry.pack(padx=10, pady=10)

special_chars_var = tk.IntVar()
special_chars_checkbox = tk.Checkbutton(root, text="Include special characters", variable=special_chars_var, bg="#ffab91")
special_chars_checkbox.pack(padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, font=("Verdana",10), bg="#c62828", activebackground="#b71c1c")
generate_button.pack(padx=10, pady=10)

password_label = tk.Label(root, text="Generated Password", font=("Calibri",14,"bold"), bg="#ffab91")
password_label.pack(padx=10, pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.pack(padx=10, pady=10) 
password_entry.config(state='readonly')

root.mainloop()