from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

class View:
    def __init__(self,root):
        txColor = "#FFFFFF"

        self.tr_path = "D:\imageproc\Level 4\lv4-6.jpg"

        self.tr_load = Image.open(self.tr_path)
        self.tr_load = self.tr_load.resize((150, 200), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.tr_load)

        self.tr_frameinfo = Label(root, bg=bgColor, text="Data Info", anchor="w",fg=txColor ,font=("Whiteney 13 bold")).grid(row=0, column=0,pady=20, sticky='WENS',padx=20)
        self.tr_btn_add = Button(root, bg="#7289DA", text="Tambah" ,font=("Whiteney 10 bold") , width=10, fg=txColor,relief=FLAT, command=lambda: self.showTrainAdd()).grid(row=0, column=1)
        self.tr_photo = Label(root,  text="Photo" , fg=txColor, anchor="center", image = self.render)
        self.tr_photo.image = self.render
        self.tr_photo.grid(row=0, column=2, rowspan=5, sticky='WENS',padx=20,pady=20)
        self.tr_lmean = Label(root, bg=bgColor, text="Mean", anchor="w",font=("Whiteney 11 bold") , fg=txColor).grid(row=1, column=0, sticky='WENS',padx=20)

        self.tr_meanR = Label(root, bg=bgColor, text="R : 12345678910", anchor="w",font=("Whiteney 9") , fg=txColor)
        self.tr_meanR.grid(row=2, column=0, sticky='WENS',padx=20)
        self.tr_meanG = Label(root, bg=bgColor, text="G : 1234567", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.tr_meanG.grid(row=3, column=0, sticky='WENS',padx=20)
        self.tr_meanB = Label(root, bg=bgColor, text="B : 12345678910", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.tr_meanB.grid(row=4, column=0, sticky='WENS',padx=20)

        self.tr_lmean = Label(root, bg=bgColor, text="Standar Deviasi", anchor="w",font=("Whiteney 11 bold"), fg=txColor).grid(row=1, column=1, sticky='WENS',padx=20)
        self.tr_stdR = Label(root, bg=bgColor, text="R : 12345678910", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.tr_stdR.grid(row=2, column=1, sticky='WENS',padx=20)
        self.tr_stdG = Label(root, bg=bgColor, text="G : 12310", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.tr_stdG.grid(row=3, column=1, sticky='WENS',padx=20)
        self.tr_stdB = Label(root, bg=bgColor, text="B : 12345678910", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.tr_stdB.grid(row=4, column=1, sticky='WENS',padx=20)

        self.tr_llevel = Label(root, bg=bgColor, text="Level :",anchor="w",font=("Whiteney 10 bold"), fg=txColor).grid(row=5, column=0, sticky='WENS',padx=20)
        self.tr_ilevel = Spinbox(root, from_=2, to=5, width=5, state="readonly",font=("Whiteney 9")).grid(row=5, column=1)
        self.tr_btn_change = Button(root, bg="#FFFFFF", text="Ganti Gambar",relief=FLAT,font=("Whiteney 10"),width=12, command=lambda: self.uploadTrain()).grid(row=5, column=2)

        self.tr_btn_del = Button(root, bg="#FFFFFF", text="Hapus",font=("Whiteney 10"),width=10,relief=FLAT).grid(row=6, column=0, pady=20)
        self.tr_btn_save = Button(root, bg="#FFFFFF", text="Simpan",font=("Whiteney 10"),width=10,relief=FLAT).grid(row=6, column=1)
        self.tr_btn_detail = Button(root, bg="#FFFFFF", text="Detail",font=("Whiteney 10"),width=10,relief=FLAT, command=lambda: self.showTrainDetail()).grid(row=6, column=2,padx=20)
        self.tr_lchoose = Label(root, text="Data Training",font=("Whiteney 10 bold"),bg="#F26522",fg="#FFFFFF").grid(row=7, column=0, columnspan=3, sticky='WENS',padx=20)
        self.tr_listbox = Listbox(root,bg="#36393F",relief=FLAT,fg="white",selectbackground="#43B581",activestyle="none",font=("Whiteney 10 bold"))
        self.tr_listbox.grid(row=8, column=0, columnspan=3, sticky='WENS', padx=20)
        self.tr_listbox.insert(END, "a list entry")
        for item in ["one", "two", "three", "four"]:
            self.tr_listbox.insert(END, item)

    def getfeature(self,img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        maxg = (100, 255, 255)
        ming = (34, 100, 10)
        mask = cv2.inRange(hsv, ming, maxg)
        kernel = np.ones([5, 5])
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        result = cv2.bitwise_and(img, img, mask=mask)
        r, g, b = cv2.split(result)
        ext = np.array([r.mean(), g.mean(), b.mean(), r.std(), g.std(), b.std()])
        ext = np.around(ext,decimals=4)
        return ext

    def showTrainDetail(self):
        rtrain = Tk()
        label = Label(rtrain,text="Detail Train")
        label.pack()
        rtrain.mainloop()

    def showTrainAdd(self):
        rtrain = Tk()
        label = Label(rtrain,text="Sanguan")
        label.pack()
        rtrain.mainloop()

    def uploadTrain(self):
        path = ""
        path = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("JPG files", "*.jpg"), ("all files", "*.*")))
        if path =="":
            return
        load = Image.open(path)
        load = load.resize((150, 200), Image.ANTIALIAS)
        img = cv2.imread(path,1)
        feat = self.getfeature(img)

        render = ImageTk.PhotoImage(load)
        self.tr_photo.configure(image=render)
        self.tr_photo.image = render
        meanR = feat[0]
        meanG = feat[1]
        meanB = feat[2]
        stdR = feat[3]
        stdG = feat[4]
        stdB = feat[5]

        self.tr_meanR["text"] = "R : "+ str(meanR)
        self.tr_meanG["text"] = "R : " + str(meanG)
        self.tr_meanB["text"] = "R : " + str(meanB)
        self.tr_stdR["text"] = "R : "+ str(stdR)
        self.tr_stdG["text"] = "R : " + str(stdG)
        self.tr_stdB["text"] = "R : " + str(stdB)

if __name__ == '__main__':
    bgColor = "#202225"
    root = Tk()
    display = View(root)
    root.configure(bg=bgColor)
    root.mainloop()