import tkinter as tk
from tkinter import Label
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
PINK = "#e2979c"
BLUE = "#305be7"
BLACK = "#000000"
GRAY = "#808080"

# image uploader function
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)

    if len(path):
        pic = Image.open(path)
        width, height = pic.size
        drawing = ImageDraw.Draw(pic)
        font = ImageFont.truetype("arial.ttf", 200)
        Fill_Color = (128, 128, 128)
        watermark_text = text_input.get()
        x = 1800
        y = 2000
        position = (x, y)
        drawing.text(xy=position, text=watermark_text, font=font, fill=Fill_Color)
        fname = filename.get()
        pic.save(f'{fname}.jpg')
        img = pic.resize((500, 500))
        pic = ImageTk.PhotoImage(img)
        w_label["text"] = "Would you like to watermark another photo"
        # re-sizing the app window in order to fit picture
        # and button
        app.geometry("560x300")
        label.config(image=pic)
        label.image = pic
        # watermark_pic = Image.open('watermark_image.jpg')
        # watermark_pic.show()


    else:
        print("No file is chosen !! Please choose a file.")


app = Tk()
app.geometry("560x270")
app.minsize(width=500, height=300)
app.config(padx=100, pady=100)


label = tk.Label(app)
label.grid(column=1, row=0)
w_label = Label(text="Enter your watermark phrase below!")
w_label.grid(column=3, row=1)
# input for watermark phrase
text_input = Entry(width=40)
text_input.grid(column=3, row=2)
f_label = Label(text="What would you like the filename to be?")
f_label.grid(column=3, row=3)
filename = Entry(width=40)
filename.grid(column=3, row=4)
# defining our upload button
uploadButton = tk.Button(app, text="Locate Image", command=imageUploader)
uploadButton.grid(column=3, row=5)

app.title("Water Mark for Photos")

app.mainloop()
