from Padi import Padi
from PadiController import PadiController
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np
from ViewNavigation import ViewNavigation


class ViewTesting:
    def __init__(self,root):

        bgColor = "#202225"
        padi = PadiController()
        txColor = "#FFFFFF"
        self.tr_addroot = ""
        self.tr_path = padi.index_ts()[0]['img']
        self.tr_id = padi.index_ts()[0]['id']
        self.tr_idx = 0
        self.tr_load = Image.open(self.tr_path)
        self.tr_load = self.tr_load.resize((150, 200), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.tr_load)

        self.tr_frameinfo = Label(root, bg=bgColor, text="Data Testing", anchor="w",fg=txColor ,font=("Whiteney 18 bold")).grid(row=0, column=0+3,pady=20, sticky='WENS',padx=20)
        self.tr_btn_tr_add = Button(root, bg="#7289DA", text="Tambah" ,font=("Whiteney 10 bold") , width=10, fg=txColor,relief=FLAT, command= lambda: self.showTrainAdd(root)).grid(row=0, column=1+3)
        self.tr_photo = Label(root,  text="Photo" , fg=txColor, anchor="center", image = self.render)
        self.tr_photo.image = self.render
        self.tr_photo.grid(row=0, column=2+3, rowspan=5, sticky='WENS',padx=20,pady=20)
        self.tr_lmean = Label(root, bg=bgColor, text="Mean", anchor="w",font=("Whiteney 12 bold") , fg=txColor).grid(row=1, column=0+3, sticky='WENS',padx=20)

        self.tr_meanR = Label(root, bg=bgColor, text="R : 12345678910", anchor="w",font=("Whiteney 10 bold") , fg=txColor)
        self.tr_meanR.grid(row=2, column=0+3, sticky='WENS',padx=20)
        self.tr_meanG = Label(root, bg=bgColor, text="G : 1234567", anchor="w",font=("Whiteney 10 bold"), fg=txColor)
        self.tr_meanG.grid(row=3, column=0+3, sticky='WENS',padx=20)
        self.tr_meanB = Label(root, bg=bgColor, text="B : 12345678910", anchor="w",font=("Whiteney 10 bold"), fg=txColor)
        self.tr_meanB.grid(row=4, column=0+3, sticky='WENS',padx=20)

        self.tr_lmean = Label(root, bg=bgColor, text="Standar Deviasi", anchor="w",font=("Whiteney 12 bold"), fg=txColor).grid(row=1, column=1+3, sticky='WENS',padx=20)
        self.tr_stdR = Label(root, bg=bgColor, text="R : 12345678910", anchor="w",font=("Whiteney 10 bold"), fg=txColor)
        self.tr_stdR.grid(row=2, column=1+3, sticky='WENS',padx=20)
        self.tr_stdG = Label(root, bg=bgColor, text="G : 12310", anchor="w",font=("Whiteney 10 bold"), fg=txColor)
        self.tr_stdG.grid(row=3, column=1+3, sticky='WENS',padx=20)
        self.tr_stdB = Label(root, bg=bgColor, text="B : 12345678910", anchor="w",font=("Whiteney 10 bold"), fg=txColor)
        self.tr_stdB.grid(row=4, column=1+3, sticky='WENS',padx=20)

        self.tr_llevel = Label(root, bg=bgColor, text="Level :",anchor="w",font=("Whiteney 12 bold"), fg=txColor).grid(row=5, column=0+3, sticky='WENS',padx=20)
        self.tr_varlevel = StringVar(root)
        self.tr_varlevel.set("4")
        self.tr_ilevel = Spinbox(root, from_=2, to=5, width=5,textvariable=self.tr_varlevel, state="readonly",font=("Whiteney 9"),relief=FLAT)
        self.tr_ilevel.grid(row=5, column=1+3)

        self.ketwaktu = ['pagi', 'siang', 'sore']

        self.tr_varwaktu = "pagi"

        self.tr_lwaktu = Label(root, bg=bgColor, text="Waktu :",anchor="w",font=("Whiteney 12 bold"), fg=txColor).grid(row=6, column=0+3, sticky='WENS',padx=20)
        self.tr_iwaktu = ttk.Combobox(root,state="readonly")
        self.tr_iwaktu["values"] = ['Pagi','Siang','Sore']
        self.tr_iwaktu.current(self.ketwaktu.index(self.tr_varwaktu))
        self.tr_iwaktu.grid(row=6, column=1+3)
        # print(self.tr_iwaktu.current(), self.tr_iwaktu.get())

        self.tr_btn_change = Button(root, bg="#FFFFFF", text="Ganti Gambar",relief=FLAT,font=("Whiteney 10 bold"),width=18, command=lambda: self.uploadTrain()).grid(row=5, column=2+3)

        self.tr_btn_del = Button(root, bg="#FFFFFF", text="Hapus",font=("Whiteney 10 bold"),width=10,relief=FLAT, command=lambda : self.tr_delete(root)).grid(row=7, column=0+3)
        self.tr_btn_save = Button(root, bg="#FFFFFF", text="Simpan",font=("Whiteney 10 bold"),width=10,relief=FLAT, command=lambda : self.tr_save()).grid(row=7, column=1+3)
        self.tr_btn_detail = Button(root, bg="#FFFFFF", text="Detail",font=("Whiteney 10 bold"),width=10,relief=FLAT, command=lambda: self.showTrainDetail(self.tr_path)).grid(row=7, column=2+3)

        # self.tr_lchoose = Label(root, text="Data Testing",font=("Whiteney 18 bold"),bg=bgColor,fg=txColor).grid(row=8, column=0+3, columnspan=3, sticky='WENS',padx=20)
        self.tr_listbox = Listbox(root,bg="#36393F",relief=FLAT,fg="white",selectbackground="#43B581",activestyle="none",font=("Whiteney 10 bold"))
        self.tr_listbox.grid(row=9, column=0+3, columnspan=3, rowspan=3, sticky='WENS', padx=20)

        no = 0
        for i in padi.index_ts():
            no = no + 1
            self.tr_listbox.insert(END, [no,i["name"],i["id"]])
        self.tr_listbox.select_set(0)
        self.tr_listbox.bind('<ButtonRelease-1>', self.tr_onselect)

        self.update_tr_info(padi.index()[0]['id'])
        padder = Label(root, bg=bgColor, fg=txColor).grid(row=12,column=0,columnspan=3,sticky='WENS',padx=20)


    def tr_onselect(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        self.tr_idx = index
        id = w.get(index)[2]

        self.update_tr_info(id)


    def update_tr_info(self,id):
        self.tr_id = id
        padi = PadiController().show(id)
        path = padi.img
        load = Image.open(path)
        load = load.resize((150, 200), Image.ANTIALIAS)
        img = cv2.imread(path,1)
        feat = self.getfeature(img)

        render = ImageTk.PhotoImage(load)
        self.tr_photo.configure(image=render)
        self.tr_photo.image = render

        meanR = padi.meanr
        meanG = padi.meang
        meanB = padi.meanb
        stdR = padi.stdr
        stdG = padi.stdg
        stdB = padi.stdb

        self.tr_meanR["text"] = "R : "+ str(meanR)
        self.tr_meanG["text"] = "G : " + str(meanG)
        self.tr_meanB["text"] = "B : " + str(meanB)
        self.tr_stdR["text"] = "R : "+ str(stdR)
        self.tr_stdG["text"] = "G : " + str(stdG)
        self.tr_stdB["text"] = "B : " + str(stdB)
        self.tr_path = path
        self.tr_varlevel.set(str(padi.level))
        self.tr_varwaktu = padi.time
        self.tr_iwaktu.current(self.ketwaktu.index(self.tr_varwaktu))


    def tr_save(self):
        id = self.tr_id
        # name = self.tr_name


        path = self.tr_path
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
        category = "testing"
        time = self.ketwaktu[self.tr_iwaktu.current()]
        level = self.tr_ilevel.get()
        request = dict(id=id, name=name,meanr=meanr, meang=meang, meanb=meanb, stdr=stdr, stdg=stdg, stdb=stdb, img=img, category=category, time=time, level=level)
        result = PadiController().update(id, request)
        self.tr_listbox.delete(self.tr_idx)
        self.tr_listbox.insert(self.tr_idx, [self.tr_idx+1, result.name, result.id])
        # print(self.tr_iwaktu.current(), self.tr_iwaktu.get())

    def tr_delete(self,root):
        id = self.tr_id
        result = PadiController().destroy(id)
        self.tr_listbox.delete(self.tr_idx)
        ViewNavigation(root).labeljmlts['text'] = len(PadiController().index_ts())

    def tr_add(self,root):
        # name = self.tr_name
        id = str((Padi().last().id)+1)
        path = self.tr_addpath
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
        category = "testing"
        time = self.ketwaktu[self.tr_addiwaktu.current()]
        level = self.tr_addilevel.get()
        request = dict(id=id, name=name,meanr=meanr, meang=meang, meanb=meanb, stdr=stdr, stdg=stdg, stdb=stdb, img=img, category=category, time=time, level=level)
        result = PadiController().store(request)
        # self.tr_listbox.delete(self.tr_idx)
        self.tr_listbox.insert(len(Padi().all_ts()), [(len(Padi().all_ts())), result.name,id])
        self.tr_addroot.destroy()
        ViewNavigation(root).labeljmlts['text'] = len(PadiController().index_ts())

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

    def showTrainDetail(self,path):
        rtrain = Toplevel()
        rtrain.grab_set()
        img = cv2.imread(path, 1)
        img = cv2.resize(img, None, fx=0.3, fy=0.3)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        imgready = cv2.resize(img, None, fx=0.7, fy=0.7)
        im = Image.fromarray(imgready)
        render = ImageTk.PhotoImage(image=im)

        img1 = Label(rtrain, text="Photo", fg="white", anchor="center", image=render)
        img1.grid(row=0,column=0)
        img1.image = render

        label1 = Label (rtrain, text="")

        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

        imgready = cv2.resize(hsv, None, fx=0.7, fy=0.7)
        im = Image.fromarray(imgready)
        render = ImageTk.PhotoImage(image=im)

        img2 = Label(rtrain, text="Photo", fg="white", anchor="center", image=render)
        img2.grid(row=0,column=1)
        img2.image = render

        maxg = (100, 255, 255)
        ming = (34, 100, 10)
        mask = cv2.inRange(hsv, ming, maxg)

        imgready = cv2.resize(mask, None, fx=0.7, fy=0.7)
        im = Image.fromarray(imgready)
        render = ImageTk.PhotoImage(image=im)

        img3 = Label(rtrain, text="Photo", fg="white", anchor="center", image=render)
        img3.grid(row=0,column=3)
        img3.image = render

        kernel = np.ones([3, 3])
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        imgready = cv2.resize(mask, None, fx=0.7, fy=0.7)
        im = Image.fromarray(imgready)
        render = ImageTk.PhotoImage(image=im)

        img4 = Label(rtrain, text="Photo", fg="white", anchor="center", image=render)
        img4.grid(row=1,column=0)
        img4.image = render

        result = cv2.bitwise_and(img, img, mask=mask)
        imgready = cv2.resize(result, None, fx=0.7, fy=0.7)
        im = Image.fromarray(imgready)
        render = ImageTk.PhotoImage(image=im)


        img5 = Label(rtrain, text="Photo", fg="white", anchor="center", image=render)
        img5.grid(row=1,column=1)
        img5.image = render
        rtrain.title('Detail Training')
        rtrain.mainloop()


    def showTrainAdd(self,root):
        bgColor = "#202225"
        self.tr_addroot = Toplevel()
        self.tr_addroot.grab_set()
        txColor = "#FFFFFF"

        self.tr_addpath = "D:\Work\BWD-files\choose.png"

        self.tr_addload = Image.open(self.tr_addpath)
        self.tr_addload = self.tr_addload.resize((150, 200), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.tr_addload)

        self.tr_addframeinfo = Label(self.tr_addroot, bg=bgColor, text="Tambah Data", anchor="w",fg=txColor ,font=("Whiteney 18 bold")).grid(row=0, column=0,pady=20, sticky='WENS',padx=20)
        # self.tr_addbtn_tr_add = Button(self.tr_addroot, bg="#7289DA", text="Tambah" ,font=("Whiteney 10 bold") , width=10, fg=txColor,relief=FLAT, command= lambda: self.showTrainAdd()).grid(row=0, column=1)
        self.tr_addphoto = Label(self.tr_addroot,  text="Photo" , fg=txColor, anchor="center", image = self.render)
        self.tr_addphoto.image = self.render
        self.tr_addphoto.grid(row=0, column=2, rowspan=5, sticky='WENS',padx=20,pady=20)
        self.tr_addlmean = Label(self.tr_addroot, bg=bgColor, text="Mean", anchor="w",font=("Whiteney 11 bold") , fg=txColor).grid(row=1, column=0, sticky='WENS',padx=20)

        self.tr_addmeanR = Label(self.tr_addroot, bg=bgColor, text="R : ", anchor="w",font=("Whiteney 9") , fg=txColor)
        self.tr_addmeanR.grid(row=2, column=0, sticky='WENS',padx=20)
        self.tr_addmeanG = Label(self.tr_addroot, bg=bgColor, text="G : ", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.tr_addmeanG.grid(row=3, column=0, sticky='WENS',padx=20)
        self.tr_addmeanB = Label(self.tr_addroot, bg=bgColor, text="B : ", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.tr_addmeanB.grid(row=4, column=0, sticky='WENS',padx=20)

        self.tr_addlmean = Label(self.tr_addroot, bg=bgColor, text="Standar Deviasi", anchor="w",font=("Whiteney 11 bold"), fg=txColor).grid(row=1, column=1, sticky='WENS',padx=20)
        self.tr_addstdR = Label(self.tr_addroot, bg=bgColor, text="R : ", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.tr_addstdR.grid(row=2, column=1, sticky='WENS',padx=20)
        self.tr_addstdG = Label(self.tr_addroot, bg=bgColor, text="G : ", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.tr_addstdG.grid(row=3, column=1, sticky='WENS',padx=20)
        self.tr_addstdB = Label(self.tr_addroot, bg=bgColor, text="B : ", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.tr_addstdB.grid(row=4, column=1, sticky='WENS',padx=20)

        self.tr_addllevel = Label(self.tr_addroot, bg=bgColor, text="Level :",anchor="w",font=("Whiteney 10 bold"), fg=txColor).grid(row=5, column=0, sticky='WENS',padx=20)
        self.tr_addilevel = Spinbox(self.tr_addroot, from_=2, to=5, width=5, state="readonly",font=("Whiteney 9"))
        self.tr_addilevel.grid(row=5, column=1)
        self.tr_addwaktu = ['pagi', 'siang', 'sore']

        self.tr_addlwaktu = Label(self.tr_addroot, bg=bgColor, text="Waktu :",anchor="w",font=("Whiteney 10 bold"), fg=txColor).grid(row=6, column=0, sticky='WENS',padx=20)
        self.tr_addiwaktu = ttk.Combobox(self.tr_addroot,state="readonly")
        self.tr_addiwaktu["values"] = ['Pagi','Siang','Sore']
        self.tr_addiwaktu.current(0)
        self.tr_addiwaktu.grid(row=6, column=1)

        self.tr_addbtn_change = Button(self.tr_addroot, bg="#FFFFFF", text="Pilih Gambar",relief=FLAT,font=("Whiteney 10"),width=12, command=lambda: self.chooseTrain()).grid(row=5, column=2)

        self.tr_addbtn_del = Button(self.tr_addroot, bg="#FFFFFF", text="Batal",font=("Whiteney 10"),width=10,relief=FLAT, command=lambda: self.tr_addroot.destroy()).grid(row=7, column=0, pady=20)
        self.tr_addbtn_save = Button(self.tr_addroot, bg="#FFFFFF", text="Simpan",font=("Whiteney 10"),width=10,relief=FLAT, command=lambda: self.tr_add(root)).grid(row=7, column=1)

        self.tr_addroot.configure(bg=bgColor)
        self.tr_addroot.title("Tambah Data Testing")
        self.tr_addroot.mainloop()

    def chooseTrain(self):
        path = ""
        path = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("JPG files", "*.jpg"), ("all files", "*.*")))
        if path =="":
            return
        load = Image.open(path)
        load = load.resize((150, 200), Image.ANTIALIAS)
        img = cv2.imread(path,1)
        feat = self.getfeature(img)

        render = ImageTk.PhotoImage(load)
        self.tr_addphoto.configure(image=render)
        self.tr_addphoto.image = render

        meanR = feat[0]
        meanG = feat[1]
        meanB = feat[2]
        stdR = feat[3]
        stdG = feat[4]
        stdB = feat[5]

        self.tr_addmeanR["text"] = "R : "+ str(meanR)
        self.tr_addmeanG["text"] = "R : " + str(meanG)
        self.tr_addmeanB["text"] = "R : " + str(meanB)
        self.tr_addstdR["text"] = "R : "+ str(stdR)
        self.tr_addstdG["text"] = "R : " + str(stdG)
        self.tr_addstdB["text"] = "R : " + str(stdB)
        self.tr_addpath = path

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
        self.tr_path = path