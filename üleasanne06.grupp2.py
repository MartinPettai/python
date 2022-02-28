import urllib.request
#martin pettai
#it21
#16.02.22
erakonnad=[]
re=0
ke=0

        
with open('s6pru_l6ustaraamatus.txt', 'r') as minu_fail:
    for rida in minu_fail:
        eesnimi, perekonnanimi, erakond, number = rida.split(" ")
        print (f"{eesnimi:15} {perekonnanimi:15} {erakond:6} {number:7}")
        if erakond=="RE":
            re+=1
        if erakond=="KE":
            ke+=1
            
        if erakond not in erakonnad:
            erakonnad.append(erakond)
        with open('nimed.txt','a')as fail_kirjutamiseks:
            fail_kirjutamiseks.write(str(eesnimi)+" "+str(perekonnanimi)+'\n')



print ( )
print (f"Reformikaid:  {re}")
print (f"Kesikuid:  {ke}")
print (f"Erakondi kokku:  {len(erakonnad)}")
