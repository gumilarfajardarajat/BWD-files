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

    def all_ts(self):
        sql = "SELECT * FROM padi WHERE category='testing'"
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