import math
from random import randint
import random
# Harjutus 2
# Martin Pettai
# 31.01.2022pank


#ruutude ja kuupide tabel
for a in range(1,11):
    print(f"{a:5} {a**2:5} {a**3:5}")


#pank
konto=0
intress=0.05
raha=int(input("Sisestage oma rahasumma: "))
konto+=raha
aastad=int(input("Sisestage oma raha hoiustamsie aastad: "))

print(f"{'aasta':4} {'algsumma':10} {'intress':10} {'Aasta lõpuks':10} ")

for i in range(aastad):
    kasum=konto*intress
    print(f"{i+1:4} {konto:10.2f} {kasum:10.2f} {konto+kasum:10.2f}")
    konto+=kasum
print(f"{'Summa kokku:'} {konto:.2f}")
print(f"Kasum:{konto-raha:.2f}")










'''

#arvamismäng

loop=1
arvamiskorrad=1
number=random.randint (1,10)
 
while loop==1:
    if arvamiskorrad<=3:
        arv = int(input('Sisesta arv (1-20): '))
    else:
        uuesti=input("kas sa tahad veel mängida? (mhm/mkm: ")
        if uuesti=="mhm":
            arvamiskorrad=0
        else:
            loop=0
    arvamiskorrad+=1
    if arv==number:
        print("oled uhke nüüd enda üle?")
    else:
        print("Mis sitasti see uuesti")
   
print ("game over")
            
        
    
    
    

#viisikud

for i in range(1,101):
    if i%5==0:
        print(i)
   

#korrutustabel
for i in range(1,11):
    print(f"5 x {i} = {i*5}")

    
#paarispaaritu

for i in range(1,101):
    if i%2==0:
        print(i,"paaris")
    else:
        print(i,"paaritu")
    

#loto

for i in range(1,6):
    print(randint(0,9),end="")
print()

#tärnid

for i in range(1,6):           #read
    for j in range(1,6):       #veerud
        print('* ', end='')
    print()

for i in range(1,6):
    print("* "*i)

konto=6
for i in range(1,6):
    konto = konto-1
    print(konto*"* ")
    
    


#jalgpalli meeskondf

sugu=input("sisestage oma sugu (soo esimene täht): ")
if sugu=="m":
    vanus=int(input("sisestage oma vanus: "))
    if vanus>=16 and vanus <=18:
        print("Te olete meeskonnas!")
    else:
        print ("Me ei taha teid siia")

else:
    print("Me ei taha sind siia :)")




#müük
hind=int(input("Sisesta toote hind: "))
if hind <= 10:
    ale=0.1
else:
    ale=0.2
hind=hind-hind*ale
print("hind on",hind,"eurot")







#Juubel
synd=input("Sisesta sünniaeg: ")
p, k, a=synd.split(".")
vanus=2022- int(a)
jaak=vanus%5
if jaak==0:
    print("Sul on juubel!")
else:
    print("Sul ei ole juubel :(")
    
    








#matemaatika
arv1= int(input("sisesta arv 1: "))
arv2=int(input("sisesta arv 2: "))
tehe=int(input("\n 1) liitmine\n 2) lahutamine\n 3) korrutamine\n 4) jagamine\nvali tehe: "))
if tehe==1:
    v=arv1 + arv2
elif tehe==2:
    v=arv1 - arv2
elif tehe==3:
    v=arv1 * arv2
else:
    v=arv1 / arv2
print(v)




#ruudu kontroll
a = int(input("sisesta ruudu üks külg: "))
b = int(input("sisesta ruudu teine külg: "))
if a == b:
    print("tegemist on ruuduga")
else:
    print("risttahukas")
    
   ''' 
