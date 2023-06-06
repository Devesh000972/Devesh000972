import random
import string
import hashlib
import tkinter as tk

def generate_password(length, charset):
    # Generate a random password using the defined characters
    password = ''.join(random.choice(charset) for i in range(length))

    # Return the generated password
    return password

def generate_hash(password):
    # Generate a SHA-256 hash of the password
    hash_object = hashlib.sha256(password.encode('utf-8'))
    hash_code = hash_object.hexdigest()

    # Return the hash code
    return hash_code

# Define the function to generate the password and update the label
def generate():
    # Get the values of the entry widgets
    length = int(length_entry.get())
    uppercase = uppercase_var.get()
    lowercase = lowercase_var.get()
    numbers = numbers_var.get()
    special_chars = special_chars_var.get()

    # Build the character set based on the user's inputs
    charset = ''
    if uppercase:
        charset += string.ascii_uppercase
    if lowercase:
        charset += string.ascii_lowercase
    if numbers:
        charset += string.digits
    if special_chars:
        charset += string.punctuation

    # Generate the password using the generated character set
    password = generate_password(length=length, charset=charset)

    # Generate the hash code for the password
    hash_code = generate_hash(password)

    # Update the label with the generated password and hash code
    password_label.config(text=password)
    hash_label.config(text=f"Hash code: {hash_code}")
    if len(password) > 20:
        password_label.config(font=("TkDefaultFont", 10))

# Create the Tkinter window
window = tk.Tk()
window.title("Password Generator")
window.geometry('400x150')

# Disable window resizing
window.resizable(False, False)
window.pack_propagate(0)

# Create the length label and entry widgets
length_label = tk.Label(window, text="Password length:")
length_label.grid(column=0, row=0)
length_entry = tk.Entry(window, width=10)
length_entry.insert(0, "8")
length_entry.grid(column=1, row=0)

# Create the checkboxes for selecting the character types
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()

uppercase_cb = tk.Checkbutton(window, text="Uppercase", variable=uppercase_var)
uppercase_cb.grid(column=0, row=1)

lowercase_cb = tk.Checkbutton(window, text="Lowercase", variable=lowercase_var)
lowercase_cb.grid(column=1, row=1)

numbers_cb = tk.Checkbutton(window, text="Numbers", variable=numbers_var)
numbers_cb.grid(column=2, row=1)

special_chars_cb = tk.Checkbutton(window, text="Special Characters", variable=special_chars_var)
special_chars_cb.grid(column=3, row=1)

# Create the generate button
generate_button = tk.Button(window, text="Generate Password", command=generate)
generate_button.grid(column=2, row=2)

# Create the label for displaying the generated password
password_label = tk.Label(window, text="", font=("TkDefaultFont", 12),wraplength=600)
password_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER) 

# Create the label for displaying the hash code
hash_label = tk.Label(window, text="",wraplength=600)
hash_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Start the GUI
window.mainloop()
