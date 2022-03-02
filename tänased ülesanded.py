
#3.4

fail=input("Palun sisestage faili nimi: ")
fail=open(fail,encoding="UTF-8")
for i in fail:
    print(i)
    

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



korrad=int(input("mitu äratust tahad? "))
for a in range(korrad):
    print("tõuse ja sära!")
    
