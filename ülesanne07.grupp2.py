import math
#martin pettai
#it21
#17.02.22
#ül7
#tervitus



def tervitus(nimi, keel="de"):
    
    if keel=="et":
        print("tere",nimi)
    elif keel=="en":
        print("hi",nimi)
    else:
        print("gutten morgen",nimi)
    
    
tervitus("nimi","et")
tervitus("nimi")

#ruumala

def kuup(a):
    v=kylg**3
    return v

def kera(r):
    v=round(4/3*math.pi*r**3,2)
    return v

def koonus(r,h):
    v=round(1/3*math.pi*r**2*h)
    return v

def silinder(r,h):
    v=math.pi*r**2*h
    return v


print("********** LEIAME RUUMALA **********")
print("Vali kujund")
print("1 Kuup")
print("2 Kera")
print("3 Koonus")
print("4 Silinder")
valik=int(input("Vali kujund 1-4: "))
if valik==1:
    k=int(input("sisesta kuubi külje pikkus: "))
    print("kuubi ruumala on: ",kuup(k))
    
elif valik==2:
    k=int(input("sisesta kera raadius: "))
    print("kera ruumala: ",kera(k))
    
elif valik==3:
    k=int(input("sisesta raadius: "))
    h=int(input("sisesta kõrgus: "))
    print("koonuse ruumala on: ",koonus(k,h))
    
else:
    k=int(input("sisesta raadius: "))
    h=int(input("sisesta kõrgus: "))
    print("silindri ruumala on: ",silinder(k,h))
    












    