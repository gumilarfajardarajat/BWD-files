import numpy as np
import cv2
from tkinter import *
from PIL import ImageTk, Image



def bgr2gray(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    lbl.configure(image=imgtk)
    lbl.image = imgtk

def bgr2hsv(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    im = Image.fromarray(img)

    imgtk = ImageTk.PhotoImage(image=im)
    lbl.configure(image=imgtk)
    lbl.image = imgtk

def hsv2bgr(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    lbl.configure(image=imgtk)
    lbl.image = imgtk

def addLux(img):

    img = img.astype('uint16')
    val = int(spin.get())*10
    print(val)
    img = img + val
    img = np.where(img <= 255, img, 255)
    img = img.astype('uint8')

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    lbl.configure(image=imgtk)
    lbl.image = imgtk
    print(img[0][0])


if __name__ == '__main__':

    path = "D:\imageproc\Level 4\lv4-8.jpg"
    # Load an color image
    img = cv2.imread(path,1)

    img = cv2.resize(img,None,fx=0.3,fy=0.3)
    #Rearrang the color channel

    imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    # A root window for displaying objects
    root = Tk()

    # Convert the Image object into a TkPhoto object
    im = Image.fromarray(imgrgb)
    imgtk = ImageTk.PhotoImage(image=im)


    # Put it in the display window
    lbl = Label(root, image=imgtk)
    fm = Frame(root)
    btn_bgr = Button(fm, text="RGB", command=lambda : hsv2bgr(img))
    btn_gray = Button(fm, text="Grayscale", command=lambda : bgr2gray(img))
    btn_hsv = Button(fm, text="HSV", command=lambda : bgr2hsv(img))
    spin = Spinbox(root, from_=0, to=100, width=5,command=lambda : addLux(img))


    lbl.pack(side=TOP)
    fm.pack(side=TOP,fill=X)
    btn_bgr.pack(side=LEFT,fill=X, expand=1)
    btn_gray.pack(side=LEFT,fill=X, expand=1)
    btn_hsv.pack(side=LEFT,fill=X, expand=1)
    spin.pack(side=TOP)

    root.mainloop() # Start the GUI

