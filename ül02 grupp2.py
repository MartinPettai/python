import math
# Harjutus 2
# Martin Pettai
# 31.01.2022


#arvusüsteemid
ks=input



#ajateisendus
aeg=int(input("sisesta aeg minutites: "))
tunnid=aeg//60
minutid=aeg%60
print(tunnid,":",minutid)


#Kolmnurga hüpotenuus
a=16
b=9
c=math.sqrt(a **2+b **2)
print("hüpotenuus: ",c,)


#rulluisiutajad
kiirus=29.9
aeg=24
vahemaa=(kiirus*aeg)
print("rulluisutaja jõuab 24 minutiga:",vahemaa,"meetri kaugusele")

#pitsa
hind=12.90
protsent=0.1
inimesed=3
kokku=((hind*protsent)+hind)/inimesed
print("igaüks peab maksma:",kokku,"€")


#toote hind
toode=36.75
soodushind=0.4
tooteid=3
summa=(toode-toode*soodushind)*tooteid
print("kõik tooted kokku:",summa,"€")

#kolmnurga ümbermõõt
a,b,c= 5,6,8
P=a+b+c
print("kolmnurga ümbermõõt: ",P)
