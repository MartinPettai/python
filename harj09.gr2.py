#Martin Pettai
#IT21
#harj9

import datetime
valik=input("Vali keel (eesti, inglis)\n").upper()
if valik=="eesti":
    kuud=["Jaanuar","Veeburar","Märts"]
    kuup=datetime.date.today()
    kuu=int(kuup.month)
    kuup2=datetime.date(kuup.year, kuu , kuup.day)
    print(kuup2.strftime("%d")+". "+str(kuud[kuu-1])+" "+kuup2.strftime("%Y"))
elif valik=="inglis":
    kuud=["January","Veburary","March"]
    kuup=datetime.date.today()
    kuu=int(kuup.month)
    kuup2=datetime.date(kuup.year, kuu , kuup.day)
    print(kuup2.strftime("%d")+". "+str(kuud[kuu-1])+" "+kuup2.strftime("%Y"))

isikukood="50431050673"
isikukood=input("Sisesta isikukood: ")
aasta=int("20"+isikukood[1]+isikukood[2])
kuu=int(isikukood[3]+isikukood[4])
paev=int(isikukood[5]+isikukood[6])
sp=datetime.date(aasta, kuu, paev)


now=datetime.date.today().year
vanus=now-aasta
print("Teie vanus: ",vanus)
print("Sündisite:",datetime.date(aasta,kuu,paev))