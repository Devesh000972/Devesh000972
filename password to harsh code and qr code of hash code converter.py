import hashlib
import qrcode
import tkinter as tk
from PIL import ImageTk, Image

# Create a QR code instance
def qr_making():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    data = hash_code_label['text'] # Get the hash code from the label
    qr.add_data(data)
    qr.make(fit=True)
    # Create an image of the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    # Convert the image to PhotoImage format for tkinter
    global qr_image
    qr_image = ImageTk.PhotoImage(img)
    # Update the label with the new QR code image
    qr_label.config(image=qr_image)


def generate_hash():
    # Get the user input password from the entry widget
    password = password_entry.get()

    # Generate the hash code for the password using SHA-256 algorithm
    hash_code = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Update the label with the generated hash code
    hash_code_label.config(text=f"Hash code: {hash_code}")

    # Generate and display the QR code of the hash code
    qr_making()

# Create the Tkinter window
window = tk.Tk()
window.title("Password Hash Generator")
window.geometry('400x200')

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
hash_code_label = tk.Label(window, text="", wraplength=600)
hash_code_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Create a label to display the QR code image
qr_label = tk.Label(window, image=None)
qr_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Center the window
window.eval('tk::PlaceWindow . center')

# Start the GUI
window.mainloop()
