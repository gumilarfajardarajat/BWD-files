from tkinter import *
from Padi import Padi

class DisplayMain:
    def __init__(self,root):


        valtr = str(len(Padi().all_tr()))
        valts = str(len(Padi().all_ts()))

        label = Label(root, text="DATA TRAINING", font=("Roboto 10 bold")).grid(row=1, column=1)

        self.lbvaltr = Label(root, text=valtr, font=("Roboto 50 bold"))
        self.lbvaltr.grid(row=2, column=1)


        label = Label(root, text="DATA TESTING", borderwidth=2, font=("Roboto 10 bold")).grid(row=1, column=2)
        self.lbvalts = Label(root, text=valts, font=("Roboto 50 bold"))
        self.lbvalts.grid(row=2, column=2)