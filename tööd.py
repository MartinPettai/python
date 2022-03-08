



#4.4

kulalised=int(input("mitu külalist tuleb:"))
def tervitus(a):
    for i in range(a):
        print(i)
tervitus(kulalised)



#4.3

def eelarve(a):
    summa=a*10+55
    return summa
kutsutud=int(input("mitu inimest tuleb?: "))
tuleb=int(input("kindlalt osaleb (mitu inimest): "))
print("maskimaalne eelarve:",eelarve(kutsutud),"€")
print("maskimaalne eelarve:",eelarve(tuleb),"€")


#4.2

def mahlapakkide_arv():
    mahlapakkidearv=round(kogus*0.4/3,0)
    return mahlapakkidearv
kg = int(input("sisesta õunte kogus: "))
print(int(mahlapakkide_arv(kg)))



#4.1
kuva=int(input("mitu korda soovid kuvada? "))
def banner(t,k):
    for i in range(k):
        print(t.upper())
    
banner("osta ja sa ei kahetse!")






# 3.5

fail=open("nimekiri.txt",encoding="UTF-8")
jrk=1
from datetime import *
print(datetime.now().day)
for i in fail:
    if jrk==8:
        print(jrk)
    jrk+=1
    print(i)





#3.4
lugu=1
fail1=input("sisestage failinimi: ")
fail=open(fail1,encoding="UTF-8")
number=1
for i in fail:
    print(str(number)+". "+str(i),end="")
    number+=1


fail=open(fail1,encoding="UTF-8")
laul=int(input("\n mis laulu te sooviksite kuulata? "))
for i in fail:
    if lugu==1:
        print(i)
    lugu+=1
    
        
    


#3.3

fail=open("konto.txt",encoding="UTF-8")
for rida in fail:
    if int(rida)>0:
        print(rida,end="")
    


#3.2

porgand=0
ringid=int(input("sisestage ringide arv: "))
for i in range(1,ringid):
    if i%2==0:
        
        porgand+=i
        
print(f"saadavate porgandite koguarv on {porgand}")
#3.1
'''
fail=open("rabased.txt", encoding="UTF-8")
vastuvoetud=[]
for rida in fail:
    vastuvoetud.append(int(rida))
    
input("Mis aasta andmeid vajad? ")
print(f"{aasta}.aastal oli vastuvoetud {vastuvoetud} [int(aasta[3]-1")
'''
    




#2.6
import random
lumi=14
poial=int(input("palju neist tahab õuna?: "))
for i in range(poial):
    oun=random.randint(1,2)
    print(oun)
    lumi=lumi-oun
print(f"lumivalgukesele jäi {lumi} õuna") 
    


#2.5

arv=int(input("sisesta arv: "))
nisuterad=1
i=1

while i<=arv:
    
    nisuterad*=2
    i+=1
print(f"nisuteri on {nisuterad}. ruudu eest: {arv}")
    

#2.3

import random

taringud=int(input("Sisesta täringute arv: "))

for a in range(taringud):
    print(random.randint(1,6))

#2.2
    
ringid=int(input("Palju on ringe? "))
porgandid=0







i=1
while i<=ringid:
    if i%2==0:
        porgandid+=i
    i+=1
print(f"porgandite arv on {porgandid}")

#2.1



äratused=int(input("sisesta äratuste arv:"))
for a in range(äratused):
    print("tõuse ja sära!")
    
 #1.4
def bussid():
    inimesed=int(input("inimeste arv:"))
    istekohad=int(input("bussi kohtade arv:"))
    viimane=inimesed%istekohad
    if viimane==0:
        bussid=inimesed//istekohad
        viimane=istekohad
    else:
        bussid=inimesed//istekohad+1
    print(f"Busse vaja: {bussid}\nViimases bussis inimesi: {viimane}")

bussid()

#1.2
def liblikas():
    aasta=2020
    liblikas="teelehe-mosaiikliblikas"
    lause_keskosa=". aasta liblikas on"
    lause=str(aasta)+lause_keskosa+liblikas
    print(lause)
liblikas()
#1.1
print("Tere, maailm!")