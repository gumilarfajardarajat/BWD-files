from Padi import Padi

class PadiController:

    def index(self):
        padi = Padi().alli()
        return padi

    def index_tr(self):
        padi = Padi().all_tr()
        return padi

    def index_ts(self):
        padi = Padi().all_ts()
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
        padi.category = request["category"]
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