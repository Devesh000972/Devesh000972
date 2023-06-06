import requests
import os
import tkinter.filedialog
import tkinter as tk # import tkinter with an alias
from PIL import ImageTk, Image

# API key for Unsplash
API_KEY = "aCDGEzvquPQ5UtIOqu30nMZCS86V1-lFhGoZYm4OoFg"

def get_new():
    # Get the search query from the entry widget
    query = entry.get()

    # Get a random image URL from Unsplash API
    response = requests.get(f"https://api.unsplash.com/search/photos/?client_id={API_KEY}&query={query}&orientation=landscape")
    data = response.json()
    image_url = data["results"][0]["urls"]["regular"]

    # Call the updated update_image function to save the downloaded image automatically
    update_image(image_url)


def get_image(query):
    # Get a random motivational image URL from Unsplash API
    response = requests.get(f"https://api.unsplash.com/search/photos/?client_id={API_KEY}&query={query}&orientation=landscape")
    data = response.json()
    image_url = data["results"][0]["urls"]["regular"] # use "results" instead of "urls" for a list of images
    return image_url



def update_image(image_url):
    # Download the image and save it to a file in the current working directory
    response = requests.get(image_url)
    file_path = "motivational_image.jpg"
    with open(file_path, "wb") as f:
        f.write(response.content)

    # Open the downloaded image, resize it, and display it in the image label
    image = Image.open(file_path)
    image = image.resize((400, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo



root = tk.Tk() # capitalize Tk()
root.title('Image searcher')    
txt = tk.Label(root, text='Search image:') # capitalize Label() and use the tkinter alias
txt.place(relx=0.5, rely=0.04, anchor=tk.CENTER)

entry = tk.Entry(root, width=30)
entry.place(relx=0.5, rely=0.08, anchor=tk.CENTER)

btn = tk.Button(root, text='Search', command=get_new) # capitalize Button() and use the tkinter alias
btn.place(relx=0.5, rely=0.13, anchor=tk.CENTER) # adjust the y-position

image_label = tk.Label(root)
image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
