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
    data = t.get()
    qr.add_data(data)
    qr.make(fit=True)
    # Create an image of the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    # Convert the image to PhotoImage format for tkinter
    global qr_image
    qr_image = ImageTk.PhotoImage(img)
    # Update the label with the new QR code image
    label.config(image=qr_image)

# Create a tkinter window
root = tk.Tk()
root.title("QR Code Display")

# Create an Entry widget to get input for QR code data
t = tk.Entry(root)
t.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Create a Button widget to trigger QR code generation
btn = tk.Button(root, text='Convert to QR',command=qr_making)
btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Create a label to display the QR code image
qr_image = None  # Placeholder for the QR code image
label = tk.Label(root)
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the tkinter event loop
root.mainloop()
