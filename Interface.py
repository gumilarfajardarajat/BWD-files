from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bwd"
)
mycursor = mydb.cursor()


class Padi:
    id = ""
    name = ""
    img = ""

    def alli(self):
        sql = "SELECT * FROM padi"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        alli = list(dict(id=id, name=name,meanr=meanr, meang=meang, meanb=meanb, stdr=stdr, stdg=stdg, stdb=stdb, img=img, category=category, time=time, level=level) for id, name, meanr, meang, meanb, stdr, stdg, stdb, img, category, time, level in myresult)
        return alli

    def all_tr(self):
        sql = "SELECT * FROM padi WHERE category='training'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        alli = list(dict(id=id, name=name,meanr=meanr, meang=meang, meanb=meanb, stdr=stdr, stdg=stdg, stdb=stdb, img=img, category=category, time=time, level=level) for id, name, meanr, meang, meanb, stdr, stdg, stdb, img, category, time, level in myresult)
        return alli

    def find(self, id=""):
        sql = "SELECT * FROM padi WHERE id=xid"
        id = str(id)
        sql = sql.replace("xid", id)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        self.id = myresult[0][0]
        self.name = myresult[0][1]
        self.meanr = myresult[0][2]
        self.meang = myresult[0][3]
        self.meanb = myresult[0][4]
        self.stdr = myresult[0][5]
        self.stdg = myresult[0][6]
        self.stdb = myresult[0][7]
        self.img = myresult[0][8]
        self.category = myresult[0][9]
        self.time = myresult[0][10]
        self.level = myresult[0][11]
        return self

    def last(self):
        sql = "SELECT * FROM padi ORDER BY id DESC LIMIT 1"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        self.id = myresult[0][0]
        self.name = myresult[0][1]
        self.meanr = myresult[0][2]
        self.meang = myresult[0][3]
        self.meanb = myresult[0][4]
        self.stdr = myresult[0][5]
        self.stdg = myresult[0][6]
        self.stdb = myresult[0][7]
        self.img = myresult[0][8]
        self.category = myresult[0][9]
        self.time = myresult[0][10]
        self.level = myresult[0][11]
        return self

    def save(self):
        if (self.id == ""):
            sql = "INSERT INTO padi (name, meanr, meang, meanb, stdr, stdg, stdb, img, category, time, level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (self.name, self.meanr, self.meang, self.meanb, self.stdr, self.stdg, self.stdb, self.img, self.category, self.time, self.level)
            mycursor.execute(sql, val)
            mydb.commit()
            print("data has been created")
        else:
            name = self.name
            meanr = self.meanr
            meang = self.meang
            meanb = self.meanb
            stdr = self.stdr
            stdg = self.stdg
            stdb = self.stdb
            img = self.img

            category = self.category
            time = self.time
            level = self.level
            id = str(self.id)
            # sql = "UPDATE padi SET name = |" + name + "|,img = |" + img + "| WHERE id = |" + id + "|"
            sql = "UPDATE padi SET name = |" + name + "|,meanr = |" + meanr + "|,meang = |" + meang + "|,meanb = |" + meanb + "|,stdr = |" + stdr + "|,stdg = |" + stdg + "|,stdb = |" + stdb + "|,img = |" + img + "|,category = |" + category + "|,time = |" + time + "|,level = |" + level + "| WHERE id = |" + id + "|"
            sql = sql.replace("|", "'")
            mycursor.execute(sql)
            mydb.commit()
            print("data has been updated")
        return self

    def delete(self):
        sql = "DELETE FROM padi WHERE id=xid"
        id = str(self.id)
        sql = sql.replace("xid", id)
        mycursor.execute(sql)
        mydb.commit()
        print("data has been deleted")
        return self


class PadiController:

    def index(self):
        padi = Padi().alli()
        return padi

    def index_tr(self):
        padi = Padi().all_tr()
        return padi

    def show(self, id):
        padi = Padi().find(id)
        return padi

    def store(self,request):
        padi = Padi()
        padi.name = request["name"]
        padi.meanr = request["meanr"]
        padi.meang = request["meang"]
        padi.meanb = request["meanb"]
        padi.stdr = request["stdr"]
        padi.stdg = request["stdg"]
        padi.stdb = request["stdb"]
        padi.img = request["img"]
        padi.category = "training"
        padi.time = request["time"]
        padi.level = request["level"]
        padi.save()
        return padi

    def update(self, id,request):
        # print(type(request["name"]))
        padi = Padi().find(id)
        padi.name = request["name"]
        padi.meanr = request["meanr"]
        padi.meang = request["meang"]
        padi.meanb = request["meanb"]
        padi.stdr = request["stdr"]
        padi.stdg = request["stdg"]
        padi.stdb = request["stdb"]
        padi.img = request["img"]
        padi.category = request["category"]
        padi.time = request["time"]
        padi.level = request["level"]
        padi.save()
        return padi

    def destroy(self, id):
        padi = Padi().find(id)
        padi.delete()


class View:
    def __init__(self,root):
        padi = PadiController()
        txColor = "#FFFFFF"
        self.tr_path = padi.index()[0]['img']
        self.tr_id = padi.index()[0]['id']
        self.tr_idx = 0
        self.tr_load = Image.open(self.tr_path)
        self.tr_load = self.tr_load.resize((150, 200), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.tr_load)

        self.tr_frameinfo = Label(root, bg=bgColor, text="Data Info", anchor="w",fg=txColor ,font=("Whiteney 18 bold")).grid(row=0, column=0,pady=20, sticky='WENS',padx=20)
        self.tr_btn_add = Button(root, bg="#7289DA", text="Tambah" ,font=("Whiteney 10 bold") , width=10, fg=txColor,relief=FLAT, command= lambda: self.showTrainAdd()).grid(row=0, column=1)
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
        self.tr_varlevel = StringVar(root)
        self.tr_varlevel.set("4")
        self.tr_ilevel = Spinbox(root, from_=2, to=5, width=5,textvariable=self.tr_varlevel, state="readonly",font=("Whiteney 9"))
        self.tr_ilevel.grid(row=5, column=1)

        self.ketwaktu = ['pagi', 'siang', 'sore']

        self.tr_varwaktu = "pagi"

        self.tr_lwaktu = Label(root, bg=bgColor, text="Waktu :",anchor="w",font=("Whiteney 10 bold"), fg=txColor).grid(row=6, column=0, sticky='WENS',padx=20)
        self.tr_iwaktu = ttk.Combobox(root,state="readonly")
        self.tr_iwaktu["values"] = ['Pagi','Siang','Sore']
        self.tr_iwaktu.current(self.ketwaktu.index(self.tr_varwaktu))

        self.tr_iwaktu.grid(row=6, column=1)
        # print(self.tr_iwaktu.current(), self.tr_iwaktu.get())

        self.tr_btn_change = Button(root, bg="#FFFFFF", text="Ganti Gambar",relief=FLAT,font=("Whiteney 10"),width=12, command=lambda: self.uploadTrain()).grid(row=5, column=2)

        self.tr_btn_del = Button(root, bg="#FFFFFF", text="Hapus",font=("Whiteney 10"),width=10,relief=FLAT, command=lambda : self.tr_delete()).grid(row=7, column=0, pady=20)
        self.tr_btn_save = Button(root, bg="#FFFFFF", text="Simpan",font=("Whiteney 10"),width=10,relief=FLAT, command=lambda : self.tr_save()).grid(row=7, column=1)
        self.tr_btn_detail = Button(root, bg="#FFFFFF", text="Detail",font=("Whiteney 10"),width=10,relief=FLAT, command=lambda: self.showTrainDetail(self.tr_path)).grid(row=7, column=2,padx=20)

        self.tr_lchoose = Label(root, text="Data Training",font=("Whiteney 13 bold"),bg="#F26522",fg="#FFFFFF").grid(row=8, column=0, columnspan=3, sticky='WENS',padx=20)
        self.tr_listbox = Listbox(root,bg="#36393F",relief=FLAT,fg="white",selectbackground="#43B581",activestyle="none",font=("Whiteney 10 bold"))
        self.tr_listbox.grid(row=9, column=0, columnspan=3, sticky='WENS', padx=20)

        no = 0
        for i in padi.index_tr():
            no = no + 1
            self.tr_listbox.insert(END, [no,'gambar',i["id"]])
        self.tr_listbox.select_set(0)
        self.tr_listbox.bind('<ButtonRelease-1>', self.tr_onselect)

        self.update_tr_info(padi.index()[0]['id'])



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
        self.tr_meanG["text"] = "R : " + str(meanG)
        self.tr_meanB["text"] = "R : " + str(meanB)
        self.tr_stdR["text"] = "R : "+ str(stdR)
        self.tr_stdG["text"] = "R : " + str(stdG)
        self.tr_stdB["text"] = "R : " + str(stdB)
        self.tr_path = path
        self.tr_varlevel.set(str(padi.level))
        self.tr_varwaktu = padi.time
        self.tr_iwaktu.current(self.ketwaktu.index(self.tr_varwaktu))


    def tr_save(self):
        id = self.tr_id
        # name = self.tr_name
        name = "gambar"+str(id)
        path = self.tr_path
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
        time = self.ketwaktu[self.tr_iwaktu.current()]
        level = self.tr_ilevel.get()
        request = dict(id=id, name=name,meanr=meanr, meang=meang, meanb=meanb, stdr=stdr, stdg=stdg, stdb=stdb, img=img, category=category, time=time, level=level)
        result = PadiController().update(id, request)
        self.tr_listbox.delete(self.tr_idx)
        self.tr_listbox.insert(self.tr_idx, [self.tr_idx+1, 'gambar', result.id])
        # print(self.tr_iwaktu.current(), self.tr_iwaktu.get())

    def tr_delete(self):
        id = self.tr_id
        result = PadiController().destroy(id)
        self.tr_listbox.delete(self.tr_idx)

    def tr_add(self):
        # name = self.tr_name
        id = str((Padi().last().id)+1)
        name = "gambar"+str(id)
        path = self.addpath
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
        time = self.ketwaktu[self.addiwaktu.current()]
        level = self.addilevel.get()
        request = dict(id=id, name=name,meanr=meanr, meang=meang, meanb=meanb, stdr=stdr, stdg=stdg, stdb=stdb, img=img, category=category, time=time, level=level)
        result = PadiController().store(request)
        # self.tr_listbox.delete(self.tr_idx)
        self.tr_listbox.insert(len(Padi().all_tr())+1, [(len(Padi().all_tr())+1), 'gambar',id])
        self.addroot.destroy()

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

    def showTrainDetail(self,path):
        rtrain = Toplevel()
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

        rtrain.mainloop()


    def showTrainAdd(self):
        bgColor = "#202225"
        self.addroot = Toplevel()
        txColor = "#FFFFFF"

        self.addpath = "D:\Work\BWD-files\choose.png"

        self.addload = Image.open(self.addpath)
        self.addload = self.addload.resize((150, 200), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.addload)

        self.addframeinfo = Label(self.addroot, bg=bgColor, text="Tambah Data", anchor="w",fg=txColor ,font=("Whiteney 18 bold")).grid(row=0, column=0,pady=20, sticky='WENS',padx=20)
        # self.addbtn_add = Button(self.addroot, bg="#7289DA", text="Tambah" ,font=("Whiteney 10 bold") , width=10, fg=txColor,relief=FLAT, command= lambda: self.showTrainAdd()).grid(row=0, column=1)
        self.addphoto = Label(self.addroot,  text="Photo" , fg=txColor, anchor="center", image = self.render)
        self.addphoto.image = self.render
        self.addphoto.grid(row=0, column=2, rowspan=5, sticky='WENS',padx=20,pady=20)
        self.addlmean = Label(self.addroot, bg=bgColor, text="Mean", anchor="w",font=("Whiteney 11 bold") , fg=txColor).grid(row=1, column=0, sticky='WENS',padx=20)

        self.addmeanR = Label(self.addroot, bg=bgColor, text="R : ", anchor="w",font=("Whiteney 9") , fg=txColor)
        self.addmeanR.grid(row=2, column=0, sticky='WENS',padx=20)
        self.addmeanG = Label(self.addroot, bg=bgColor, text="G : ", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.addmeanG.grid(row=3, column=0, sticky='WENS',padx=20)
        self.addmeanB = Label(self.addroot, bg=bgColor, text="B : ", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.addmeanB.grid(row=4, column=0, sticky='WENS',padx=20)

        self.addlmean = Label(self.addroot, bg=bgColor, text="Standar Deviasi", anchor="w",font=("Whiteney 11 bold"), fg=txColor).grid(row=1, column=1, sticky='WENS',padx=20)
        self.addstdR = Label(self.addroot, bg=bgColor, text="R : ", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.addstdR.grid(row=2, column=1, sticky='WENS',padx=20)
        self.addstdG = Label(self.addroot, bg=bgColor, text="G : ", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.addstdG.grid(row=3, column=1, sticky='WENS',padx=20)
        self.addstdB = Label(self.addroot, bg=bgColor, text="B : ", anchor="w",font=("Whiteney 9"), fg=txColor)
        self.addstdB.grid(row=4, column=1, sticky='WENS',padx=20)

        self.addllevel = Label(self.addroot, bg=bgColor, text="Level :",anchor="w",font=("Whiteney 10 bold"), fg=txColor).grid(row=5, column=0, sticky='WENS',padx=20)
        self.addilevel = Spinbox(self.addroot, from_=2, to=5, width=5, state="readonly",font=("Whiteney 9"))
        self.addilevel.grid(row=5, column=1)
        self.addwaktu = ['pagi', 'siang', 'sore']

        self.addlwaktu = Label(self.addroot, bg=bgColor, text="Waktu :",anchor="w",font=("Whiteney 10 bold"), fg=txColor).grid(row=6, column=0, sticky='WENS',padx=20)
        self.addiwaktu = ttk.Combobox(self.addroot,state="readonly")
        self.addiwaktu["values"] = ['Pagi','Siang','Sore']
        self.addiwaktu.current(1)
        self.addiwaktu.grid(row=6, column=1)

        # print(self.addiwaktu.current(), self.addiwaktu.get())

        self.addbtn_change = Button(self.addroot, bg="#FFFFFF", text="Pilih Gambar",relief=FLAT,font=("Whiteney 10"),width=12, command=lambda: self.chooseTrain()).grid(row=5, column=2)

        self.addbtn_del = Button(self.addroot, bg="#FFFFFF", text="Batal",font=("Whiteney 10"),width=10,relief=FLAT, command=lambda: self.addroot.destroy()).grid(row=7, column=0, pady=20)
        self.addbtn_save = Button(self.addroot, bg="#FFFFFF", text="Simpan",font=("Whiteney 10"),width=10,relief=FLAT, command=lambda: self.tr_add()).grid(row=7, column=1)

        # self.addbtn_detail = Button(self.addroot, bg="#FFFFFF", text="Detail",font=("Whiteney 10"),width=10,relief=FLAT, command=lambda: self.showTrainDetail(self.addpath)).grid(row=6, column=2,padx=20)

        self.addroot.configure(bg=bgColor)
        self.addroot.mainloop()

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
        self.addphoto.configure(image=render)
        self.addphoto.image = render

        meanR = feat[0]
        meanG = feat[1]
        meanB = feat[2]
        stdR = feat[3]
        stdG = feat[4]
        stdB = feat[5]

        self.addmeanR["text"] = "R : "+ str(meanR)
        self.addmeanG["text"] = "R : " + str(meanG)
        self.addmeanB["text"] = "R : " + str(meanB)
        self.addstdR["text"] = "R : "+ str(stdR)
        self.addstdG["text"] = "R : " + str(stdG)
        self.addstdB["text"] = "R : " + str(stdB)
        self.addpath = path

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



if __name__ == '__main__':
    bgColor = "#202225"
    root = Tk()
    display = View(root)
    root.configure(bg=bgColor)
    root.mainloop()