import datetime
import time
import sys
from time import strftime
run=input("press enter to start")
x=0
y=0
lista_realnog_vremena=[]
while True:

    datumvreme=datetime.datetime.now().time().strftime("%S")

    duzina_liste_real=len(lista_realnog_vremena)



    if duzina_liste_real==0:
        lista_realnog_vremena.append(int(datumvreme))
    else:
        lista_realnog_vremena.append(int(datumvreme))


        index_predzadnji_element=len(lista_realnog_vremena)-2
        index_zadnji_element=len(lista_realnog_vremena)-1
        predzadnji_element=lista_realnog_vremena[index_predzadnji_element]
        zadnji_element=lista_realnog_vremena[index_zadnji_element]
        if zadnji_element==predzadnji_element:
            lista_realnog_vremena.remove(lista_realnog_vremena[index_predzadnji_element])
        duzina_liste_nova=len(lista_realnog_vremena)
        if duzina_liste_real==duzina_liste_nova-1:
            #print(x)
            x=x+1


            if x==60:
                x=0
                y=y+1
            print(y+45,":",x)
            file = open("SecondHalfcorected.txt", "w")
            file.write(str(y+45)+":"+str(x))
            file.close()

    #lista_realnog_vremena=list(dict.fromkeys(lista_realnog_vremena[]))
    #print(lista_realnog_vremena)
