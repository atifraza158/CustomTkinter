import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

def stretch_image(event):
    global resized_image_tk
    width = event.width
    height = event.height

    resized_image = cat_image.resize((width, height))
    resized_image_tk = ImageTk.PhotoImage(resized_image)

    image_canvas.create_image(0,0, image = resized_image_tk, anchor = 'nw')

window = tk.Tk()
window.title("Images in Tkinter")
window.geometry('600x400')

# Reading Images
cat_image = Image.open('images/cat2.jpg').resize((600, 400))
cat_image_tk = ImageTk.PhotoImage(cat_image)

python_image = Image.open('images/python.png').resize((20, 20))
python_image_tk = ImageTk.PhotoImage(python_image)

# Use CTk-Image for ctk widgets
cat_ctk_image = ctk.CTkImage(
    light_image=Image.open('images/python.png').resize((20, 20)),
    dark_image=Image.open('images/python.png').resize((20, 20)),
)

# label = ttk.Label(window, text='Cat', image=cat_image_tk)
# label.pack()

# Using grid layout method
window.columnconfigure((0,1,2,3), weight=1, uniform='a')
window.rowconfigure(0, weight=1)


buttons_frame = ttk.Frame(window)
buttons_frame.grid(row=0, column=0, sticky='nw')


button = ttk.Button(buttons_frame, text="Python", image=python_image_tk, compound='left')
button.pack(pady=10)

# CTk Button
ctk_button = ctk.CTkButton(buttons_frame, text="Python", image=cat_ctk_image, compound='left')
ctk_button.pack(pady=10)

# Image Canvas
image_canvas = tk.Canvas(window, background='black', relief='ridge', bd=0, highlightthickness=0)
image_canvas.grid(row=0, column=1, columnspan=3, sticky='nsew')

image_canvas.bind('<Configure>', stretch_image)

window.mainloop()