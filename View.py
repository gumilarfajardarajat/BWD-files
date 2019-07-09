from tkinter import *
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
        alli = list(dict(id=id, name=name, img=img) for id, name, img in myresult)
        return alli

    def find(self, id=""):
        sql = "SELECT * FROM padi WHERE id=xid"
        id = str(id)
        sql = sql.replace("xid", id)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        self.id = myresult[0][0]
        self.name = myresult[0][1]
        self.img = myresult[0][2]
        return self

    def save(self):
        if (self.id == ""):
            sql = "INSERT INTO padi (name, img) VALUES (%s, %s)"
            val = (self.name, self.img)
            mycursor.execute(sql, val)
            mydb.commit()
            print("data has been created")
        else:
            name = self.name
            img = self.img
            id = str(self.id)
            sql = "UPDATE padi SET name = |" + name + "|,img = |" + img + "| WHERE id = |" + id + "|"
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

    def show(self, id):
        padi = Padi().find(id)
        return padi

    def store(self):
        padi = Padi()
        padi.name = " "
        padi.img = " "
        padi.save()
        return padi

    def update(self, id,request):
        # print(type(request["name"]))
        padi = Padi().find(id)
        padi.name = request["name"]
        padi.img = request["img"]
        padi.save()
        return padi

    def destroy(self, id):
        padi = Padi().find(id)
        padi.delete()


class View:
    def __init__(self, master):
        padi = PadiController()
        self.tr_ip_id = Entry(master,state="disabled")
        self.tr_ip_name = Entry(master)
        self.tr_ip_img = Entry(master)
        self.Lb1 = Listbox(master, selectmode=BROWSE)
        self.btn = Button(master, text="Kirim", command=lambda: self.update())
        for i in padi.index():
            self.Lb1.insert(END, [i["id"],i["name"]])

        self.Lb1.bind('<ButtonRelease-1>', self.onselect)
        self.tr_ip_id.pack()
        self.tr_ip_name.pack()
        self.tr_ip_img.pack()
        self.btn.pack()
        self.Lb1.pack()



    def onselect(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        self.idx_lb_training = index
        self.id = w.get(index)[0]
        padi = PadiController().show(self.id)

        self.tr_ip_id.delete(0, END)
        self.tr_ip_name.delete(0, END)
        self.tr_ip_img.delete(0, END)

        self.tr_ip_id.insert(END,padi.id)
        self.tr_ip_name.insert(END,padi.name)
        self.tr_ip_img.insert(END,padi.img)


    def update(self):
        id = self.id
        name = self.tr_ip_name.get()
        img = self.tr_ip_img.get()
        request = dict(id=id, name=name, img=img)
        result = PadiController().update(id,request)
        self.Lb1.delete(self.idx_lb_training)
        self.Lb1.insert(self.idx_lb_training, [result.id,result.name])



if __name__ == '__main__':
    root = Tk()
    display = View(root)
    root.mainloop()
    # p = PadiController().show(1)
    # p.name = "SGGG"
    # p.img = "se3"
    # p.save()
    # print(p.id,' ',p.name,' ',p.img)