
from ViewTraining import ViewTraining

from ViewNavigation import ViewNavigation
from DisplayMain import DisplayMain
from ButtonMain import ButtonMain

from tkinter import *


if __name__ == '__main__':
    root = Tk()

    # label = Label(root, text="").grid(row=0, column=0, padx=2)
    # label = Label(root, text="").grid(row=0, column=3, padx=2)
    # label = Label(root, text="").grid(row=5, column=0, padx=2)
    # label = Label(root, text="").grid(row=5, column=3, padx=2)

    DisplayMain(root)
    ButtonMain(root)

    root.title("BWD")
    root.mainloop()

