import hashlib
import tkinter as tk

def generate_hash():
    # Get the user input password from the entry widget
    password = password_entry.get()

    # Generate the hash code for the password using SHA-256 algorithm
    hash_code = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Update the label with the generated hash code
    hash_label.config(text=f"Hash code: {hash_code}")

# Create the Tkinter window
window = tk.Tk()
window.title("Password Hash Generator")
window.geometry('400x150')

# Disable window resizing
window.resizable(False, False)

# Create the password label and entry widgets
password_label = tk.Label(window, text="Enter Password:", font=("TkDefaultFont", 12), wraplength=600)
password_label.place(relx=0.5, rely=0.04, anchor=tk.CENTER)
password_entry = tk.Entry(window, show="*", width=30)
password_entry.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Create the show/hide password button
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        toggle_button.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        toggle_button.config(text="Show Password")

toggle_button = tk.Button(window, text="Show Password", command=toggle_password)
toggle_button.place(relx=0.5, rely=0.18, anchor=tk.CENTER)

# Create the generate button
generate_button = tk.Button(window, text="Generate Hash", command=generate_hash)
generate_button.place(relx=0.5, rely=0.23, anchor=tk.CENTER)
# Create the label for displaying the hash code
hash_label = tk.Label(window, text="", wraplength=600)
hash_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Center the window
window.eval('tk::PlaceWindow . center')

# Start the GUI
window.mainloop()
