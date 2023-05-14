import cv2
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

frame = tk.Frame(root, bg='#45aaf2')

lbl_pic_path = tk.Label(frame, text='Image Path:', padx=50, pady=50,
                        font=('verdana', 16), bg='#45aaf2')
lbl_show_pic = tk.Label(frame, bg='#45aaf2')
lbl_filtered_pic = tk.Label(frame, bg='#45aaf2')
entry_pic_path = tk.Entry(frame, font=('verdana', 16))
btn_browse = tk.Button(frame, text='Select Image', bg='grey', fg='#ffffff',
                       font=('verdana', 16))
btn_filter = tk.Button(frame, text='Apply Filter', bg='grey', fg='#ffffff',
                       font=('verdana', 16))

img = None
filtered_img = None


def selectPic():
    global img
    filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                                          filetypes=(("png images", "*.png"), ("jpg images", "*.jpg")))
    img = Image.open(filename)
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    lbl_show_pic['image'] = img
    lbl_filtered_pic['image'] = None
    entry_pic_path.delete(0, END)
    entry_pic_path.insert(0, filename)


def applyFilter():
    global filtered_img
    if img:
        # Load the selected image file using OpenCV
        image = cv2.imread(entry_pic_path.get(), 0)
        a = image.copy() / 255

        m, n = a.shape

        b = np.zeros((m, n))
        i = 2
        j = 2

        for i in range(m - 1):
            for j in range(n - 1):
                b[i, j] = (a[i - 1, j - 1] + a[i - 1, j] + a[i - 1, j + 1]
                           + a[i, j - 1] + a[i, j] + a[i, j + 1]
                           + a[i + 1, j + 1] + a[i + 1, j] + a[i + 1, j + 1])
                b[i, j] = b[i, j] / 9

        # Convert the filtered image to PIL format and display it
        filtered_img = Image.fromarray(np.uint8(b * 255))
        filtered_img = filtered_img.resize((200, 200), Image.LANCZOS)
        filtered_img = ImageTk.PhotoImage(filtered_img)
        lbl_filtered_pic['image'] = filtered_img


btn_browse['command'] = selectPic
btn_filter['command'] = applyFilter

frame.pack()

lbl_pic_path.grid(row=0, column=0)
entry_pic_path.grid(row=0, column=1, padx=(0, 20))
lbl_show_pic.grid(row=1, column=0)
lbl_filtered_pic.grid(row=1, column=1)
btn_browse.grid(row=2, column=0, padx=10, pady=10)
btn_filter.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()

