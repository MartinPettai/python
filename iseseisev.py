#iseseisev ülesanne
#Martin Pettai IT21

#prindib siit listist välja kõik numbrid mis on väiksemad kui 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i<5:
        print(i)

#väljund näitab nüüd numbreid listis

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numbrid=[]

for i in a:
    if i<5:
        numbrid.append(i)
print(numbrid)

#ühe reana

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numbrid=[]

[numbrid.append(i)for i in a if i<5]
print(numbrid)

#inimene valib ise numbri ja kood valib sellest numbrist väiksemad arvud

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numbrid=[]

valik=int(input("vali number: "))
[numbrid.append(i) for i in a if i<valik]

print(numbrid)
