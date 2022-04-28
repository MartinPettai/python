#KT1
#Martin Pettai
#28.04
#IT21

fail='oda_uus.txt'
parimad_visked=[0]
parim_vise=[0]
def odavise(fail):
    with open(fail, 'r') as minu_fail:
        for rida in minu_fail:
            enimi,pnimi,vise1,vise2,vise3=rida.split(" ")   #splittisin read
            
            visked=vise1,vise2,vise3
            parim_vise=visked[0]
            for vise in visked:
                if vise>parim_vise:
                    parim_vise=vise
                    parimad_visked.insert(parim_vise, -1)
                    

            vastus=print(pnimi,enimi,parim_vise)
    return parimad_visked


odavise(fail)


print(max(parimad_visked))

