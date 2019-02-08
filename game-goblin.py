import random
import sys
import copy
#random buat ntar menentukan menghindar berhasil atau tidak range(4)
spab = lambda x: [print("") for i in range(x)]
import shutil
memoryview(b"0").tolist()
class musuhh:
    def __init__(self):
        self.darah = 3
        self.sr = 2
        self.mr = 2
        
    def serang(self):
        
        __serang = []
        for i in range(self.sr):
            __serang.append(random.randint(0, 4))
        return __serang
    def menghindar(self):
        __menghindar = []
        for i in range(self.mr):
            __menghindar.append(i)
        return __menghindar
def gameover():
    print("GAME OVER!!!")
    sys.exit(0)
def menang():
    print("anda menang")
    sys.exit(0)
class tuyul(musuhh):
    name = "tuyul"
    darah = 10
    mr = 0
    sr = 1
    dg = 3 #damage
class monster(musuhh):
    name = "Monster"
    darah = 25
    mr = 1
    dg = 4
    sr = 3
class dirisendiri:
    darah = 100
class kevin:
    darah = 1000
class game:
    def __init__(self):
        self.game_name = "Kill Each Other"
        print("nama game : %s" %(self.game_name))
        self.tindakan = ["menghindar", "pukul", "tendang", "tusuk pakai pisau"]

        listmusuh = {"tuyul": tuyul, "monster": monster}
        print("List Enemy: ", end="")
        [print(z, end = ", ") for z in listmusuh]
        print("\n")
        musuhinp = input("pilih Musuh: ")
        self.diri = kevin()
        self.musuh = listmusuh[musuhinp]
        self.darah_musuh = copy.copy(self.musuh.darah)
        print("Darah musuh: %s" %(self.darah_musuh))
        self.darah_sendiri = copy.copy(kevin.darah)
        print(self.musuh.name)
        self.interaksi()
    def interaksi(self):
        #giliran
        #g k b
        #random dulu
        giliran = random.randint(0, 1)
        
        if giliran:
            print("Giliranmu duluan untuk menyerang!\n")
            self.menyerang()
        else:
            print("dia menyerang duluan")
            self.menghindar()
                #except:
                #    gameover()
    def menghindar(self):
        self.incoming = self.musuh().serang()
        dodge = int(input("ketik 1 angka in range(0, 4): "))
        if dodge in self.incoming:
            print("Anda berhasil menghindar\n")
        else:
            print("Anda Terkena serangan\n")
            if (self.darah_sendiri <= 0):
                print("darah habis")
                gameover()
            self.darah_sendiri -= self.musuh.dg
            print("Darah anda sisa %d" %(self.darah_sendiri))
        self.menyerang()
    def menyerang(self):
            a = 0
            if self.musuh.darah <= 0:
                menang()
            for i in self.tindakan:
                print("%d %s " %(a, i))
                a += 1
            a = 0
                
            if True:#try:
                serang = int(input("Apa yang anda lakukan: "))
                #serang = int(self.tindakan[serang]
                if serang == 0:
                    print("lu sekarang giliran menyerang tapi malah menghindar?\n")
                    gameover()
                cobasr = random.randint(0, 4)
                hindarmusuh = self.musuh().menghindar()
                if cobasr in hindarmusuh:
                    print("di berhasil menghindar\n")
                else:
                    print("Kena!\n")
                    if ((self.darah_musuh == 0) and (self.darah_musuh < 0)):
                        menang()
                    self.darah_musuh -= serang
                    print("darah musuh: %d\n" %(self.darah_musuh))
            self.menghindar()
        
            
game()