import re
import socket
#Martin Pettai
#IT21
#ÜL10

ip=[]
list=[]
valjad=open('tekst.txt')
for line in valjad:
    ipa="None"
    pw="None"
    if line.find(".")>2: 
        ipa=line[:len(line)-1]
        try:
            socket.inet_aton(ipa) 
            ip.append(ipa)
        except socket.error:
            continue
    else:
        if line.find(".")>0:
            continue
        else:
            pw=line[:len(line)-1]
            if re.search('[a-z]',line):
                if re.search('[A-Z]',line):
                    if re.search('[0-9]',line):
                       list.append(pw)
            else:
                if re.search('[A-Z]',line):
                    if re.search('[0-9]',line): 
                       list.append(pw)
            
             
print("IP-adressid")
print(ip)
print()
print("paroolid")
print(list)