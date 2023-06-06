import tkinter as tk
import phonenumbers
from phonenumbers import geocoder
import requests
import json
from PIL import ImageTk, Image
import io

# Create a new Tkinter window
window = tk.Tk()

def find_mo():
    # Parse the phone number
    parsed_number = phonenumbers.parse(entry.get())

    # Get the country name for the phone number
    country_name = geocoder.country_name_for_number(parsed_number, "en")

    # Get the region for the phone number
    region = geocoder.description_for_number(parsed_number, "en")

    # Construct the location details string
    location = f"Country: {country_name}\nRegion: {region}"

    # Update the result label with the location details
    result_label.config(text=location)

    # Get a random photo of the country from Unsplash
    response = requests.get(f"https://api.unsplash.com/search/photos?page=1&query={country_name}&orientation=landscape", headers={
        "Authorization": "Client-ID aCDGEzvquPQ5UtIOqu30nMZCS86V1-lFhGoZYm4OoFg"})
    data = json.loads(response.text)
    photo_url = data["results"][0]["urls"]["regular"]

    # Load the photo and resize it
    response = requests.get(photo_url)
    image_data = io.BytesIO(response.content)
    image = Image.open(image_data)
    image.thumbnail((600, 400))

    # Create a PhotoImage object with the resized image
    image_tk = ImageTk.PhotoImage(image)

    # Display the image label with the resized image
    image_label.config(image=image_tk)
    image_label.image = image_tk

# Set the window title
window.title("Phone Number Location Finder")

# Create an Entry widget
entry = tk.Entry(window, width=30)
entry.pack(pady=5)  # add a padding of 5 pixels above the entry

# Create a Button widget
button = tk.Button(window, text="Find Location", command=find_mo)  # Change button text and add command
button.pack()

# Create a Label widget for displaying the location result
result_label = tk.Label(window, text="",bg ='white' ,wraplength=600, justify=tk.CENTER, font=("Helvetica", 16))
result_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Create a Label widget for displaying the country image
image_label = tk.Label(window)
image_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Start the main event loop
window.mainloop()
