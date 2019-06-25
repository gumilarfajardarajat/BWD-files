from ViewTraining import ViewTraining
from ViewTesting import ViewTesting
from ViewNavigation import ViewNavigation

from tkinter import *

if __name__ == '__main__':
    bgColor = "#202225"
    root = Tk()
    display1 = ViewTraining(root)
    display2 = ViewTesting(root)
    display3 = ViewNavigation(root)
    root.configure(bg=bgColor)
    root.title("BWD")
    root.mainloop()

