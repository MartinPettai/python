import math
#martin pettai
#it21
#17.02.22
#ül08

class Auto:
    automark='puudub'
    aasta=0
    hind=0
    varv='puudub'
    kiirus=0
    
    def lisamark(self,x):
        self.automark=x
    
    def kuvamark(self):
        print(self.automark)
        
    def lisaaasta(self,x):
        self.aasta=x

    def kuvaaasta(self):
        print(self.aasta)

    def lisavarv(self,x):
        self.varv=x

    def kuvavarv(self):
        print(self.varv)

    def lisakiirus(self,x):
        self.kiirus=x

    def kuvakiirus(self):
        print(self.kiirus)


minuauto=Auto()
minuauto.lisamark("BMW")

minuauto.lisaaasta(1997)

minuauto.lisavarv("must")

minuauto.lisakiirus(225)

minuauto.kuvamark()
minuauto.kuvaaasta()
minuauto.kuvavarv()
minuauto.kuvakiirus()


    
    