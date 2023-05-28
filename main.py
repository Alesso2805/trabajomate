import cv2
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

frame = tk.Frame(root, bg='#641425')

lbl_pic_path = tk.Label(frame, text='Image Path:', padx=100, pady=100,
                        font=('verdana', 16), bg='#641425')
lbl_show_pic = tk.Label(frame, bg='#641425')
lbl_filtered_pic = tk.Label(frame, bg='#641425')
lbl_filtered_pic2 = tk.Label(frame, bg='#641425')
lbl_filtered_pic3 = tk.Label(frame, bg='#641425')
lbl_filtered_pic4 = tk.Label(frame, bg='#641425')
entry_pic_path = tk.Entry(frame, font=('verdana', 16))
btn_browse = tk.Button(frame, text='Seleccione imagen', bg='grey', fg='#ffffff',
                       font=('verdana', 16))
btn_filter = tk.Button(frame, text='Filtro Mediana', bg='grey', fg='#ffffff',
                       font=('verdana', 16))
btn_filter2 = tk.Button(frame, text='Filtro Laplaciano', bg='grey', fg='#ffffff',
                        font=('verdana', 16))
btn_filter3 = tk.Button(frame, text='Filtro Sobel', bg='grey', fg='#ffffff',
                        font=('verdana', 16))
btn_filter4 = tk.Button(frame, text='Filtro Media', bg='grey', fg='#ffffff',
                        font=('verdana', 16))

img = None
filtered_img = None


def selectPic():
    global img
    filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                                          filetypes=(("png images", ".png"), ("jpg images", ".jpg")))
    img = Image.open(filename)
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    lbl_show_pic['image'] = img
    lbl_filtered_pic['image'] = None
    lbl_filtered_pic2['image'] = None
    lbl_filtered_pic3['image'] = None
    lbl_filtered_pic4['image'] = None
    entry_pic_path.delete(0, END)
    entry_pic_path.insert(0, filename)


def applyMedianFilter():
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


def applyLaplacianFilter():
    global filtered_img
    if img:
        # Load the selected image file using OpenCV
        image = cv2.imread(entry_pic_path.get(), 0)
        a = image.copy() / 255

        # Apply Laplacian filter
        laplacian_kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
        b = cv2.filter2D(a, -1, laplacian_kernel)

        # Convert the filtered image to PIL format and display it
        filtered_img = Image.fromarray(np.uint8(b * 255))
        filtered_img = filtered_img.resize((200, 200), Image.LANCZOS)
        filtered_img = ImageTk.PhotoImage(filtered_img)
        lbl_filtered_pic2['image'] = filtered_img


def applySobelFilter():
    global filtered_img
    if img:
        # Load the selected image file using OpenCV
        image = cv2.imread(entry_pic_path.get(), 0)

        # Apply Sobel filter to the image
        sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
        sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

        # Convert the filtered image to PIL format and display it
        filtered_img = Image.fromarray(np.uint8(sobel))
        filtered_img = filtered_img.resize((200, 200), Image.LANCZOS)
        filtered_img = ImageTk.PhotoImage(filtered_img)
        lbl_filtered_pic3['image'] = filtered_img


def applyMeanFilter():
    global filtered_img
    if img:
        # Load the selected image file using OpenCV
        image = cv2.imread(entry_pic_path.get(), 0)
        a = image.copy() / 255

        # Apply the filter
        kernel_size = 3
        c = cv2.boxFilter(a, -1, (kernel_size, kernel_size), normalize=False)

        # Convert the filtered image to PIL format and display it
        filtered_img = Image.fromarray(np.uint8(c * 255))
        filtered_img = filtered_img.resize((200, 200), Image.LANCZOS)
        filtered_img = ImageTk.PhotoImage(filtered_img)
        lbl_filtered_pic4['image'] = filtered_img


btn_browse['command'] = selectPic
btn_filter['command'] = applyMedianFilter
btn_filter2['command'] = applyLaplacianFilter
btn_filter3['command'] = applySobelFilter
btn_filter4['command'] = applyMeanFilter

frame.pack()

lbl_pic_path.grid(row=0, column=0)
entry_pic_path.grid(row=0, column=1, padx=(0, 20))
lbl_show_pic.grid(row=1, column=0)
lbl_filtered_pic.grid(row=1, column=1)
lbl_filtered_pic2.grid(row=1, column=2)
lbl_filtered_pic3.grid(row=1, column=3)
lbl_filtered_pic4.grid(row=1, column=4)
btn_browse.grid(row=2, column=0, padx=10, pady=10)
btn_filter.grid(row=2, column=1, padx=10, pady=10)
btn_filter2.grid(row=2, column=2, padx=10, pady=10)
btn_filter3.grid(row=2, column=3, padx=100, pady=10)
btn_filter4.grid(row=2, column=4, padx=10, pady=10)

root.mainloop()
