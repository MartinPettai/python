import math
# Harjutus 2
# Martin Pettai
# 31.01.2022

#Juubel
sp=input("sisesta oma sünnikuupäev")








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
    
    
