import tkinter as tk
import tkinter.messagebox
import random
import string
import pyperclip

def generate_password(complexity, length, include_special, include_numbers, include_uppercase, include_lowercase):
    if length == "":
        tk.messagebox.showwarning("Invalid Length", "Please enter a valid password length.")
        return

    length = int(length)

    if length < 4:
        tk.messagebox.showwarning("Invalid Length", "Password length must be at least 4 characters.")
        return

    characters = ""

    if include_lowercase:
        characters += string.ascii_lowercase

    if include_uppercase:
        characters += string.ascii_uppercase

    if complexity == "Medium":
        characters += string.digits if include_numbers else ""
    elif complexity == "Strong":
        characters += string.digits if include_numbers else ""
        if include_special:
            characters += string.punctuation

    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if is_password_secure(password, include_numbers, include_special, include_uppercase, include_lowercase):
            break
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    update_password_length(len(password))
    update_character_counts(password)


def is_password_secure(password, include_numbers, include_special, include_uppercase, include_lowercase):
    # Define your security rules here
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    return (not include_lowercase or has_lowercase) and (not include_uppercase or has_uppercase) and (
                not include_numbers or has_digit) and (not include_special or has_special)


def update_password_length(length):
    password_length_label.config(text=f"Password Length: {length}")


def update_character_counts(password):
    lowercase_count = sum(1 for char in password if char.islower())
    uppercase_count = sum(1 for char in password if char.isupper())
    numbers_count = sum(1 for char in password if char.isdigit())
    special_count = sum(1 for char in password if char in string.punctuation)

    lowercase_label.config(text=f"Lowercase Letters: {lowercase_count}")
    uppercase_label.config(text=f"Uppercase Letters: {uppercase_count}")
    numbers_label.config(text=f"Numbers: {numbers_count}")
    special_char_label.config(text=f"Special Characters: {special_count}")


def copy_password():
    generated_password = password_entry.get()
    pyperclip.copy(generated_password)


window = tk.Tk()
window.title("Password Generator")
window.geometry("400x400")
window.configure(bg='lightgray')
complexity_label = tk.Label(window, text="Select Complexity:", bg='lightgray')
complexity_label.pack()
complexity_var = tk.StringVar()
complexity_var.set("Weak")
complexity_menu = tk.OptionMenu(window, complexity_var, "Weak", "Medium", "Strong")
complexity_menu.pack()
length_label = tk.Label(window, text="Enter Password Length:", bg='lightgray')
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()
include_special_var = tk.BooleanVar()
include_special_var.set(False)
include_special_checkbox = tk.Checkbutton(window, text="Include Special Characters", variable=include_special_var,
                                          bg='lightgray')
include_special_checkbox.pack()
include_numbers_var = tk.BooleanVar()
include_numbers_var.set(False)
include_numbers_checkbox = tk.Checkbutton(window, text="Include Numbers", variable=include_numbers_var, bg='lightgray')
include_numbers_checkbox.pack()
include_uppercase_var = tk.BooleanVar()
include_uppercase_var.set(False)
include_uppercase_checkbox = tk.Checkbutton(window, text="Include Uppercase Letters", variable=include_uppercase_var,
                                            bg='lightgray')
include_uppercase_checkbox.pack()
include_lowercase_var = tk.BooleanVar()
include_lowercase_var.set(True)
include_lowercase_checkbox = tk.Checkbutton(window, text="Include Lowercase Letters", variable=include_lowercase_var,
                                            bg='lightgray')
include_lowercase_checkbox.pack()
generate_button = tk.Button(window, text="Generate Password",
                            command=lambda: generate_password(complexity_var.get(), length_entry.get(),
                                                              include_special_var.get(), include_numbers_var.get(),
                                                              include_uppercase_var.get(), include_lowercase_var.get()),
                            bg='white')
generate_button.pack()
copy_button = tk.Button(window, text="Copy Password", command=copy_password, bg='white')
copy_button.pack()
password_label = tk.Label(window, text="Generated Password:", bg='lightgray')
password_label.pack()
password_entry = tk.Entry(window)
password_entry.pack()
password_length_label = tk.Label(window, text="Password Length: 0", bg='lightgray')
password_length_label.pack()
lowercase_label = tk.Label(window, text="Lowercase Letters: 0", bg='lightgray')
lowercase_label.pack()
uppercase_label = tk.Label(window, text="Uppercase Letters: 0", bg='lightgray')
uppercase_label.pack()
numbers_label = tk.Label(window, text="Numbers: 0", bg='lightgray')
numbers_label.pack()
special_char_label = tk.Label(window, text="Special Characters: 0", bg='lightgray')
special_char_label.pack()
window.mainloop()





