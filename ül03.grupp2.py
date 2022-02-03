# harjutus 03
# Martin Pettai
# 01.02.2022


#Palindroom
p = input("sisesta palindroom: ")
print(p == p[::-1])

#tundide ajad
start= input("algusaeg: ")
lopp= input("lõppaeg: ")
hh1,mm1=start.split(":")
hh2,mm2=lopp.split(":")

minutid=int(hh1)*60+int(mm1)
minutid2=int(hh2)*60+int(mm2)
print(minutid)

ajavahe = abs(minutid-minutid2)
hh=ajavahe // 60
mm = ajavahe % 60 #jääk

print(f"õpilase päeva pikkus on {hh}:{mm} tundi")
#emaili kontroll

email = input("Sisesta oma email")
print("@" in email)

 

#TRUE/FALSE in/not in


#vandumine
#vandumine
vanne=input("Ära kurat ütle: ")
vanne=vanne.lower().replace("kurat","*****")
print(vanne)



#korralik kasutajanimi
nimi=input("Sisesta nimi: ")
nimi=nimi.strip().capitalize()

print("Tere "+nimi+"!")

