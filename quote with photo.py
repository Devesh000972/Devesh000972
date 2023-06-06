import random
import requests
from tkinter import *
from PIL import ImageTk, Image

list = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "The best revenge is massive success. - Frank Sinatra",
    "The harder I work, the luckier I get. - Samuel Goldwyn",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb"
]


def append():
    new_quote = entry.get()
    if new_quote != "":
        list.append(new_quote)
        entry.delete(0, END)


def get_new():
    # Get a new random quote
    quote = random.choice(list)
    result_label.config(text=quote)

    # Get a new motivational image
    image_url = get_motivational_image()
    update_image(image_url)


def get_motivational_image():
    # Get a random motivational image URL from Unsplash API
    response = requests.get("https://api.unsplash.com/photos/random",
                            params={"query": "motivational", "client_id": "aCDGEzvquPQ5UtIOqu30nMZCS86V1-lFhGoZYm4OoFg"})
    data = response.json()
    image_url = data["urls"]["regular"]
    return image_url


def update_image(image_url):
    # Download the image and update the image label
    response = requests.get(image_url)
    image_data = response.content
    with open("motivational_image.jpg", "wb") as f:
        f.write(image_data)

    image = Image.open("motivational_image.jpg")
    image = image.resize((400, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo


root = Tk()

# Create image label
image_label = Label(root)
image_label.place(relx=0.5, rely=0.3, anchor=CENTER)

# Create quote label
result_label = Label(root, text="", wraplength=600, justify=CENTER, font=("Helvetica", 16))
result_label.place(relx=0.5, rely=0.7, anchor=CENTER)

# Create Next button
btn = Button(root, text='Next', bg='black', fg='white', command=get_new)
btn.place(relx=0.5, rely=0.9, anchor=CENTER)

entry = Entry(root)
entry.place(relx=0.5, rely=0.1, anchor=CENTER)

add_btn = Button(root, text='Add Quote', bg='black', fg='white', command=append)
add_btn.place(relx=0.8, rely=0.1, anchor=CENTER)

root.configure(background='black')
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Start the event loop
root.mainloop()
