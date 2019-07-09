from Padi import Padi
from PadiController import PadiController
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import *
import mysql.connector
from tkinter import *
from DisplayMain import DisplayMain
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np


class AddTraining:
    def __init__(self,dmroot):
        root = Toplevel()
        root.grab_set()

        self.path = ""
        label = Label(root, text="TAMBAH DATA TRAINING", font=("Roboto 11 bold"), anchor="w").grid(row=0, column=0,sticky="WENS", columnspan=3)

        self.photo = Label(root,text="Gambar Kosong",borderwidth=1,image="",relief="solid",font=("Roboto 10"))
        self.photo.grid(row=1,column=0,rowspan=3,columnspan=2,sticky="WENS")
        label = Button(root, text="Upload Gambar", font=("Roboto 10 bold"), command=lambda : self.uploadTrain(root)).grid(row=1,column=2)

        # label = Label(root, text="Hasil Prediksi", font=("Roboto 10 bold"), anchor="s").grid(row=2, column=2,sticky="WENS")
        # self.predict = Label(root, text="(kosong)", font=("Roboto 10 "), anchor="n")
        # self.predict.grid(row=3, column=2,sticky="WENS")

        label = Label(root, text="Level", font=("Roboto 10 bold")).grid(row=4,column=0)
        self.level = Label(root, text="(Input Level)", font=("Roboto 10"))
        self.level.grid(row=4,column=1)

        label = Button(root, text="Simpan", font=("Roboto 10 bold"),command=lambda: self.savedata(dmroot,root)).grid(row=4,column=2)

        label = Label(root, text="Waktu", font=("Roboto 10 bold")).grid(row=5,column=0)
        self.waktu = Label(root, text="(Input Waktu)", font=("Roboto 10"))
        self.waktu.grid(row=5,column=1)
        label = Button(root, text="Batal", font=("Roboto 10 bold"), command=lambda : root.destroy()).grid(row=5,column=2)

        label = Label(root, text="PREPROCESSING", font=("Roboto 11 bold"), anchor="w").grid(row=6, column=0,sticky="WENS", columnspan=3)

        label = Label(root, text="CITRA ASLI", font=("Roboto 10")).grid(row=7, column=0)
        label = Label(root, text="HSV", font=("Roboto 10")).grid(row=7, column=1)
        label = Label(root, text="HSV HIJAU", font=("Roboto 10")).grid(row=7, column=2)

        self.img1 = Label(root, text="(Kosong)", font=("Roboto 10"))
        self.img1.grid(row=8, column=0)
        self.img2 = Label(root, text="(Kosong)", font=("Roboto 10"))
        self.img2.grid(row=8, column=1)
        self.img3 = Label(root, text="(Kosong)", font=("Roboto 10"))
        self.img3.grid(row=8, column=2)

        label = Label(root, text="CLOSING", font=("Roboto 10")).grid(row=9, column=0)
        label = Label(root, text="HASIL SELEKSI", font=("Roboto 10")).grid(row=9, column=1)
        # label = Label(root, text="HASIL SELEKSI", font=("Roboto 10")).grid(row=9, column=2)

        self.img4 = Label(root, text="(Kosong)", font=("Roboto 10"))
        self.img4.grid(row=10, column=0)
        self.img5 = Label(root, text="(Kosong)", font=("Roboto 10"))
        self.img5.grid(row=10, column=1)
        # self.img6 = Label(root, text="(Kosong)", font=("Roboto 10"))
        # self.img6.grid(row=10, column=2)

        label = Label(root, text="EKSTRAKSI FITUR", font=("Roboto 11 bold"), anchor="w").grid(row=11, column=0,sticky="WENS", columnspan=3)

        label = Label(root, text="MEAN R", font=("Roboto 10 bold")).grid(row=12, column=0)
        label = Label(root, text="MEAN G", font=("Roboto 10 bold")).grid(row=12, column=1)
        label = Label(root, text="MEAN B", font=("Roboto 10 bold")).grid(row=12, column=2)

        self.nmr = Label(root, text="(Kosong)", font=("Roboto 10"))
        self.nmr.grid(row=13, column=0)
        self.nmg = Label(root, text="(Kosong)", font=("Roboto 10"))
        self.nmg.grid(row=13, column=1)
        self.nmb = Label(root, text="(Kosong)", font=("Roboto 10"))
        self.nmb.grid(row=13, column=2)

        label = Label(root, text="STD R", font=("Roboto 10 bold")).grid(row=14, column=0)
        label = Label(root, text="STD G", font=("Roboto 10 bold")).grid(row=14, column=1)
        label = Label(root, text="STD B", font=("Roboto 10 bold")).grid(row=14, column=2)

        self.nsr = Label(root, text="(Kosong)", font=("Roboto 10"))
        self.nsr.grid(row=15, column=0)
        self.nsg = Label(root, text="(Kosong)", font=("Roboto 10"))
        self.nsg.grid(row=15, column=1)
        self.nsb = Label(root, text="(Kosong)", font=("Roboto 10"))
        self.nsb.grid(row=15, column=2)

        root.mainloop()

    def savedata(self,dmroot,root):

        id = str((Padi().last().id)+1)
        path = self.path
        slicepost = path.rfind('/') + 1
        name = path[slicepost:]
        image = cv2.imread(path,1)
        feat = self.getfeature(image)

        meanr = str(feat[0])
        meang = str(feat[1])
        meanb = str(feat[2])
        stdr = str(feat[3])
        stdg = str(feat[4])
        stdb = str(feat[5])
        img = path
        category = "training"
        ketwaktu = ["pagi","siang","sore"]
        time = ketwaktu[self.waktu.current()]
        print(time)
        level = self.level.get()
        request = dict(id=id, name=name,meanr=meanr, meang=meang, meanb=meanb, stdr=stdr, stdg=stdg, stdb=stdb, img=img, category=category, time=time, level=level)
        result = PadiController().store(request)
        DisplayMain(dmroot).lbvaltr["text"] = len(PadiController().index_tr())
        root.destroy()



    def getfeature(self,img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, None, fx=0.3, fy=0.3)
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        maxg = (100, 255, 255)
        ming = (34, 100, 10)
        mask = cv2.inRange(hsv, ming, maxg)
        kernel = np.ones([3, 3])
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        result = cv2.bitwise_and(img, img, mask=mask)
        r, g, b = cv2.split(result)
        ext = np.array([r.mean(), g.mean(), b.mean(), r.std(), g.std(), b.std()])
        ext = np.around(ext,decimals=4)
        return ext

    def uploadTrain(self,root):
        path = ""
        path = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("JPG files", "*.jpg"), ("all files", "*.*")))
        if path =="":
            return
        self.setprep(path)
        load = Image.open(path)
        load = load.resize((150, 200), Image.ANTIALIAS)
        img = cv2.imread(path,1)
        feat = self.getfeature(img)

        render = ImageTk.PhotoImage(load)
        self.photo.configure(image=render)
        self.photo.image = render
        meanR = feat[0]
        meanG = feat[1]
        meanB = feat[2]
        stdR = feat[3]
        stdG = feat[4]
        stdB = feat[5]

        self.nmr["text"] = str(meanR)
        self.nmg["text"] = str(meanG)
        self.nmb["text"] = str(meanB)
        self.nsr["text"] = str(stdR)
        self.nsg["text"] = str(stdG)
        self.nsb["text"] = str(stdB)

        self.level.grid_remove()
        self.waktu.grid_remove()

        self.level = Spinbox(root, from_=2, to=5, state="readonly", font=("Roboto 10"))
        self.level.grid(row=4, column=1,sticky="WENS")
        self.waktu = ttk.Combobox(root,state="readonly")
        self.waktu["values"] = ['Pagi','Siang','Sore']
        self.waktu.grid(row=5, column=1,sticky="WENS")
        self.waktu.current(0)
        self.path = path



    def setprep(self,path):
        img = cv2.imread(path, 1)
        img = cv2.resize(img, None, fx=0.3, fy=0.3)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        imgready = cv2.resize(img, None, fx=0.3, fy=0.3)
        im = Image.fromarray(imgready)
        render = ImageTk.PhotoImage(image=im)

        self.img1.configure(image=render)
        self.img1.image = render



        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

        imgready = cv2.resize(hsv, None, fx=0.3, fy=0.3)
        im = Image.fromarray(imgready)
        render = ImageTk.PhotoImage(image=im)

        self.img2.configure(image=render)
        self.img2.image = render

        maxg = (100, 255, 255)
        ming = (34, 100, 10)
        mask = cv2.inRange(hsv, ming, maxg)

        imgready = cv2.resize(mask, None, fx=0.3, fy=0.3)
        im = Image.fromarray(imgready)
        render = ImageTk.PhotoImage(image=im)

        self.img3.configure(image=render)
        self.img3.image = render

        kernel = np.ones([3, 3])
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        imgready = cv2.resize(mask, None, fx=0.3, fy=0.3)
        im = Image.fromarray(imgready)
        render = ImageTk.PhotoImage(image=im)

        self.img4.configure(image=render)
        self.img4.image = render

        result = cv2.bitwise_and(img, img, mask=mask)
        imgready = cv2.resize(result, None, fx=0.3, fy=0.3)
        im = Image.fromarray(imgready)
        render = ImageTk.PhotoImage(image=im)


        self.img5.configure(image=render)
        self.img5.image = render


    # def testdata(self,feat):
    #
    #     mydb = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         passwd="",
    #         database="bwd"
    #     )
    #     mycursor = mydb.cursor()
    #     sql = "SELECT meanr,meang,meanb,stdr,stdg,stdb,level FROM padi WHERE category='training'"
    #     mycursor.execute(sql)
    #     myresult = mycursor.fetchall()
    #     training = np.array(myresult)
    #
    #     sql = "SELECT meanr,meang,meanb,stdr,stdg,stdb,time,level FROM padi WHERE category='testing'"
    #     mycursor.execute(sql)
    #     myresult = mycursor.fetchall()
    #     testing = np.array(myresult)
    #
    #     dftraining = pd.DataFrame(training, columns=['meanr', 'meang', 'meanb', 'stdr', 'stdg', 'stdb', 'level'])
    #     dftesting = pd.DataFrame(testing, columns=['meanr', 'meang', 'meanb', 'stdr', 'stdg', 'stdb', 'time', 'level'])
    #
    #     xtrain = dftraining.drop(columns=['level']).to_numpy()
    #     ytrain = dftraining['level'].to_numpy()
    #     xtest = dftesting.drop(columns=['level', 'time']).to_numpy()
    #     ytest = dftesting['level'].to_numpy()
    #
    #     gamma = 0.1
    #
    #     clf = svm.SVC(gamma=float(gamma), decision_function_shape='ovr', kernel='rbf')
    #     clf.fit(xtrain, ytrain)
    #     result = clf.predict([feat])
    #
    #     self.predict["text"] = str(int(result[0]))
    #     self.predict["font"] = "Roboto 30 bold"