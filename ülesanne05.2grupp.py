import random
#martin pettai
#it21
#ülesanne 5

#vanused/tärnid

vanused=[1,22,3,4,55,6,17,8,9]

for i in range(len(vanused)):
    print("*"*vanused[i])




print(f"Kõige vanem on: {max(vanused)}")
print(f"Kõige noorem on: {min(vanused)}")
print(f"vanuste summa: {sum(vanused)}")
print(f"keskmine vanus: {sum(vanused)/len(vanused)}")




    




'''

#duplikaadid

opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
nimed=[]
for i in range(len(opilased)):
    if opilased[i] not in nimed:
        nimed.append(opilased[i])
       
for i in range(len(nimed)):
    print(nimed[i],end=", ")
    
               
           




#õpilased

opilased = ['juhan','kati','mati','maaria','mario']
print("mis nime sa tahad muuta?")
for a in range(len(opilased)):
    print(f"{a+1}. {opilased[a]}")
nr=int(input("sisesta nime number: "))
opilased[nr-1]
print(opilased)
nimi2=input("sisesta uus nimi: ")
del opilased[nr-1]
opilased.insert(nr-1,nimi2)
print("nime muudeti")
print(opilased)    
    



#nimede lisamine

nimed=[]

for a in range(5):
    nimi=input("Pane siia 5 nime!: ")
    nimed.append(nimi)
nimed.sort()
for a in range(len(nimed)):
    print (nimed[a])
   '''  
    
