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
        self.tr_ilevel = Label(root, bg=bgColor, text="(kosong)",anchor="w",font=("Roboto 10 bold"), fg=txColor)
        self.tr_ilevel.grid(row=5, column=1+3, sticky='WENS', padx=20)

        self.ketwaktu = ['pagi', 'siang', 'sore']

        self.tr_varwaktu = "pagi"

        self.tr_lwaktu = Label(root, bg=bgColor, text="Waktu :",anchor="w",font=("Whiteney 12 bold"), fg=txColor).grid(row=6, column=0+3, sticky='WENS',padx=20)
        self.tr_iwaktu = Label(root, bg=bgColor, text="(kosong)",anchor="w",font=("Roboto 10 bold"), fg=txColor)
        self.tr_iwaktu.grid(row=6, column=1+3, sticky='WENS', padx=20)
        # print(self.tr_iwaktu.current(), self.tr_iwaktu.get())


        # self.tr_lchoose = Label(root, text="Data Testing",font=("Whiteney 18 bold"),bg=bgColor,fg=txColor).grid(row=8, column=0+3, columnspan=3, sticky='WENS',padx=20)
        self.tr_listbox = Listbox(root,bg="#36393F",relief=FLAT,fg="white",selectbackground="#43B581",activestyle="none",font=("Whiteney 10 bold"))
        self.tr_listbox.grid(row=9, column=0+3, columnspan=3, rowspan=3, sticky='WENS', padx=20)

        no = 0
        for i in padi.index_ts():
            no = no + 1
            self.tr_listbox.insert(END, [no,i["name"],i["id"]])
        self.tr_listbox.select_set(0)
        self.tr_listbox.bind('<ButtonRelease-1>', self.tr_onselect)

        self.update_tr_info(PadiController().index_ts()[0]['id'])
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
        self.tr_varlevel = padi.level
        self.tr_varwaktu = padi.time
        self.tr_iwaktu["text"] = self.tr_varwaktu.title()
        self.tr_ilevel["text"] = self.tr_varlevel

