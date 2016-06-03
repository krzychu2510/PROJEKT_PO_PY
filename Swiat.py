import random
from window import *
class Swiat:
    pressedKey = -1
    turaNumer = 0
    sRX = 30
    sRY = 30
    newId = 0
    organizmy = []
    czlowiek = 0
    def __init__(self):
        self.organizmy = []
        self.info = []
    def SetR(self,x,y):
        self.sRX = x
        self.sRY = y
        self.window.setSize(x,y)
    def SetWindow(self, wind):
        self.window = wind

    def AddOrganizm(self,org):
        x = random.randint(0,self.sRX)
        y = random.randint(0,self.sRY)
        if (self.FreeSpace(x, y) == False):
            return
        org.posX = x
        org.posY = y
        org.id = self.newId
        self.organizmy.insert(self.newId,org)
        self.newId+=1
        self.info.insert(len(self.info), "Dodano organizm - " + org.name)

    def AddOrganizm(self, org,x=-1,y=-1):
        if(x>-1 and y>-1):
            org.posX = x
            org.posY = y
        else:
            x = random.randint(0, self.sRX)
            y = random.randint(0, self.sRY)
            org.posX = x
            org.posY = y
        if(self.FreeSpace(x,y)==False):
            return
        org.id = self.newId
        self.organizmy.insert(self.newId,org)
        self.newId += 1
        self.info.insert(len(self.info), "Dodano organizm - " + org.name)
    def FreeSpace(self,x,y):
        for i in range(len(self.organizmy)):
            if(self.organizmy[i].posX==x and self.organizmy[i].posY==y):
                return False
        return True
    def FreeSpaceP(self,x2,y2):
        xs = 0;
        ys = 0;
        if (x2 == 0):
            xs = 1

        if (y2 == 0):
            ys = 1

        for y in range(-1+ys, 2+ys):
            for x in range(-1+xs, 2+xs):
                if (self.FreeSpace((x2 + x), (y2 + y))):
                    yield x2+x
                    yield y2+y
                    return

        yield -1
        yield -1

    def podajOrganizm(self,x,y):
        for i in range(len(self.organizmy)):
            if(self.organizmy[i].posX==x and self.organizmy[i].posY==y):
                return self.organizmy[i]
        return False
    def UpdateLoop(self, key):
        self.WykonajTure(key)
        self.UpdateLog()
        self.window.Clear()
        self.RysujSwiat()
    def WykonajTure(self, key):
        if(key==87):
            self.pressedKey = 0
        if (key == 83):
            self.pressedKey = 1
        if (key == 65):
            self.pressedKey = 2
        if (key == 68):
            self.pressedKey = 3
        if (key == 85):
            self.pressedKey = 4
        for i in range(len(self.organizmy)):
            self.organizmy[i].akcja()
            self.organizmy[i].kolizja()
        return True
    def RysujSwiat(self):
        print len(self.organizmy)
        for i in range(0,len(self.organizmy)):
            self.window.hbox.itemAtPosition(self.organizmy[i].posX,self.organizmy[i].posY).widget().setStyleSheet("background-color: "+self.organizmy[i].color)
        return True
    def UpdateLog(self):
        return True
    def deleteOrganizm(self,id):
        deleteId = -1
        for i in range(len(self.organizmy)):
            if(self.organizmy[i].id == id):
                deleteId = id
        if(deleteId>-1):
            print deleteId
            self.organizmy.remove(self.organizmy[deleteId])