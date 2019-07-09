from tkinter import *
import pandas as pd
import numpy as np
from AddTraining import AddTraining
from AddTesting import AddTesting
from ViewTraining import ViewTraining
from ViewTesting import ViewTesting
import mysql.connector
from sklearn import *
import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ButtonMain:
    def __init__(self,root):

        label = Button(root, text="Tambah", font=("Roboto 10 bold"), width=12, command=lambda: AddTraining(root)).grid(
            row=3, column=1)
        label = Button(root, text="Tambah", font=("Roboto 10 bold"), width=12, command=lambda: AddTesting(root)).grid(row=3, column=2)

        label = Button(root, text="Lihat Data", font=("Roboto 10 bold"),command=lambda: self.showdata()).grid(row=4,column=1,columnspan=2,sticky='WE',pady=(10, 0))

        label = Button(root, text="Pengujian", font=("Roboto 10 bold"),command=lambda: self.testresult()).grid(row=5, column=1, columnspan=2, sticky='WE',
                                                                             pady=(10, 0))

    def showdata(self):
        bgColor = "#202225"
        root = Toplevel()
        root.grab_set()
        ViewTraining(root)
        ViewTesting(root)
        root.configure(bg = bgColor)
        root.mainloop()

    def viewStat(self,window, poscolumn,gamma,titleval=''):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="bwd"
        )
        mycursor = mydb.cursor()
        sql = "SELECT meanr,meang,meanb,stdr,stdg,stdb,level FROM padi WHERE category='training'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        training = np.array(myresult)

        sql = "SELECT meanr,meang,meanb,stdr,stdg,stdb,time,level FROM padi WHERE category='testing'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        testing = np.array(myresult)

        dftraining = pd.DataFrame(training, columns=['meanr', 'meang', 'meanb', 'stdr', 'stdg', 'stdb', 'level'])
        dftesting = pd.DataFrame(testing, columns=['meanr', 'meang', 'meanb', 'stdr', 'stdg', 'stdb', 'time', 'level'])

        xtrain = dftraining.drop(columns=['level']).to_numpy()
        ytrain = dftraining['level'].to_numpy()
        xtest = dftesting.drop(columns=['level', 'time']).to_numpy()
        ytest = dftesting['level'].to_numpy()

        clf = svm.SVC(gamma=float(gamma), decision_function_shape='ovr', kernel='rbf')
        clf.fit(xtrain, ytrain)
        result = clf.predict(xtest)

        laporan = np.insert(testing, len(testing[0]), result, axis=1)
        val = np.equal(ytest.astype(float),result)
        laporan = np.insert(laporan, len(laporan[0]), val, axis=1)

        dflaporan = pd.DataFrame(laporan,
                                 columns=['meanr', 'meang', 'meanb', 'stdr', 'stdg', 'stdb', 'time', 'level', 'pred',
                                          'result'])
        time = titleval
        if (time != ''):
            gagal = len(dflaporan.loc[(dflaporan['time'] == time) & (dflaporan['result'] == 'False')])
            berhasil = len(dflaporan.loc[(dflaporan['time'] == time) & (dflaporan['result'] == 'True')])
            jumlah = len(dflaporan.loc[(dflaporan['time'] == time)])
            lv2 = len(
                dflaporan.loc[
                    (dflaporan['time'] == time) & (dflaporan['level'] == '2') & (dflaporan['result'] == 'True')])
            lv3 = len(
                dflaporan.loc[
                    (dflaporan['time'] == time) & (dflaporan['level'] == '3') & (dflaporan['result'] == 'True')])
            lv4 = len(
                dflaporan.loc[
                    (dflaporan['time'] == time) & (dflaporan['level'] == '4') & (dflaporan['result'] == 'True')])
            lv5 = len(
                dflaporan.loc[
                    (dflaporan['time'] == time) & (dflaporan['level'] == '5') & (dflaporan['result'] == 'True')])
            akurasi = round((berhasil / jumlah),2)
        else:
            titleval = 'semua'
            gagal = len(dflaporan.loc[(dflaporan['result'] == 'False')])
            berhasil = len(dflaporan.loc[(dflaporan['result'] == 'True')])
            jumlah = len(dflaporan)
            lv2 = len(dflaporan.loc[(dflaporan['level'] == '2') & (dflaporan['result'] == 'True')])
            lv3 = len(dflaporan.loc[(dflaporan['level'] == '3') & (dflaporan['result'] == 'True')])
            lv4 = len(dflaporan.loc[(dflaporan['level'] == '4') & (dflaporan['result'] == 'True')])
            lv5 = len(dflaporan.loc[(dflaporan['level'] == '5') & (dflaporan['result'] == 'True')])
            akurasi = round((berhasil / jumlah),2)

        fig = matplotlib.figure.Figure(figsize=(3.4, 3.4))
        ax = fig.add_subplot(111)

        ax.pie([lv2, lv3, lv4, lv5])

        circle = matplotlib.patches.Circle((0, 0), 0.7, color='white')
        ax.add_artist(circle)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().grid(row=1, column=0 + poscolumn, columnspan=3)
        canvas.draw()

        bgColor = 'white'
        txColor = 'black'

        title = Label(window, text=str(titleval).title(), bg=bgColor, fg=txColor, font=("Whiteney 40 bold")).grid(row=0,
                                                                                                                  column=0 + poscolumn,
                                                                                                                  columnspan=3)

        clabelb = Label(window, text="  ", bg='#1F77B4', fg=txColor, anchor="w", font=("Whiteney 16 bold")).grid(row=2,
                                                                                                                 column=0 + poscolumn,
                                                                                                                 sticky='WE',
                                                                                                                 padx=(
                                                                                                                 40, 0))
        nameb = Label(window, text="Level 2", bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(row=2,
                                                                                                                  column=1 + poscolumn,
                                                                                                                  sticky='WENS')
        valb = Label(window, text=str(lv2), bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(row=2,
                                                                                                                column=2 + poscolumn,
                                                                                                                sticky='WENS',
                                                                                                                pady=(
                                                                                                                0, 5),
                                                                                                                padx=(
                                                                                                                0, 40))

        clabelo = Label(window, text="  ", bg='#FF7F0E', fg=txColor, anchor="w", font=("Whiteney 16 bold")).grid(row=3,
                                                                                                                 column=0 + poscolumn,
                                                                                                                 sticky='WE',
                                                                                                                 padx=(
                                                                                                                 40, 0))
        nameo = Label(window, text="Level 3", bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(row=3,
                                                                                                                  column=1 + poscolumn,
                                                                                                                  sticky='WENS')
        valo = Label(window, text=str(lv3), bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(row=3,
                                                                                                                column=2 + poscolumn,
                                                                                                                sticky='WENS',
                                                                                                                pady=5,
                                                                                                                padx=(
                                                                                                                0, 40))

        clabelg = Label(window, text="  ", bg='#2CA02C', fg=txColor, anchor="w", font=("Whiteney 16 bold")).grid(row=4,
                                                                                                                 column=0 + poscolumn,
                                                                                                                 sticky='WE',
                                                                                                                 padx=(
                                                                                                                 40, 0))
        name1g = Label(window, text="Level 4", bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(
            row=4, column=1 + poscolumn, sticky='WENS')
        valg = Label(window, text=str(lv4), bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(row=4,
                                                                                                                column=2 + poscolumn,
                                                                                                                sticky='WENS',
                                                                                                                pady=5,
                                                                                                                padx=(
                                                                                                                0, 40))

        clabelr = Label(window, text="  ", bg='#D62728', fg=txColor, anchor="w", font=("Whiteney 16 bold")).grid(row=5,
                                                                                                                 column=0 + poscolumn,
                                                                                                                 sticky='WE',
                                                                                                                 padx=(
                                                                                                                 40, 0))
        namer = Label(window, text="Level 5", bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(row=5,
                                                                                                                  column=1 + poscolumn,
                                                                                                                  sticky='WENS')
        valr = Label(window, text=str(lv5), bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(row=5,
                                                                                                                column=2 + poscolumn,
                                                                                                                sticky='WENS',
                                                                                                                pady=5,
                                                                                                                padx=(
                                                                                                                0, 40))

        lblberhasil = Label(window, text="Prediksi Berhasil", bg=bgColor, fg=txColor, anchor="e",
                            font=("Whiteney 16 bold")).grid(row=6, column=0 + poscolumn, columnspan=2, sticky='WE',
                                                            padx=(40, 0))
        varberhasil = Label(window, text=str(berhasil), bg=bgColor, fg=txColor, anchor="e",
                            font=("Whiteney 16 bold")).grid(row=6, column=2 + poscolumn, sticky='WENS', pady=2,
                                                            padx=(0, 40))

        lblgagal = Label(window, text="Prediksi Gagal", bg=bgColor, fg=txColor, anchor="e",
                         font=("Whiteney 16 bold")).grid(row=7, column=0 + poscolumn, columnspan=2, sticky='WE',
                                                         padx=(40, 0))
        vargagal = Label(window, text=str(gagal), bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(
            row=7, column=2 + poscolumn, sticky='WENS', pady=2, padx=(0, 40))

        lbljml = Label(window, text="Jumlah Data", bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(
            row=8, column=0 + poscolumn, columnspan=2, sticky='WE', padx=(40, 0))
        varjml = Label(window, text=str(jumlah), bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(
            row=8, column=2 + poscolumn, sticky='WENS', pady=2, padx=(0, 40))

        lblacc = Label(window, text="Akurasi", bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(
            row=9, column=0 + poscolumn, columnspan=2, sticky='WE', padx=(40, 0))
        varacc = Label(window, text=str(akurasi)+'%', bg=bgColor, fg=txColor, anchor="e", font=("Whiteney 16 bold")).grid(
            row=9, column=2 + poscolumn, sticky='WENS', pady=2, padx=(0, 40))

    def testresult(self,gamma=0.1):
        if gamma=="":
            gamma = 0.1
        window = Toplevel()
        self.viewStat(window, 0,gamma, 'pagi')
        self.viewStat(window, 3,gamma, 'siang')
        self.viewStat(window, 6,gamma, 'sore')
        self.viewStat(window, 9,gamma)
        window.configure(background='White')
        window.mainloop()