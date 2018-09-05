# -*- coding: utf-8 -*-
"""
Antonio Reyes 17273
Mate Discreta 1
4/9/2018
Exponenciacion modular
"""

def main():
    terminar = input("Presione 1 para utilizar el programa o 0 para salir: ")
    if (terminar == 1):
        solicitud()

    if (terminar == 0):
        print "Gracias por utilizar el programa"

    if (terminar !=0 and terminar != 1):
        print "Esta opcion no es valida :/"
        terminar = input("Presione 1 para utilizar el programa o 0 para salir: ")
        print " "


#Ingreso de valores
def solicitud():
    print("Calcule b^e mod m")
    print "----------------------"
    b= input("Ingrese el valor de b: ")
    e= input("Ingrese el valor de e: ")
    m= input("Ingrese el valor de m: ")
    print(" ")
    print "Se va a calcular " , b , "^", e, "mod ", m
    calcular(b, e, m)

    

def calcular(b,e,m):
#convertir e en binario
    binario = bin(e)
    binario = binario[2:]
    print e, "en binario: ", binario
    aumento = 0

    #limite, hasta que b^limite se puede llegar
    limite = len(binario)

    opciones = []
    
    multiplicar = 1

    contador = 0

    for i in binario:
        if (aumento == 0):
            aumento = b
            if(aumento>m):
                while (aumento>m):
                    aumento = aumento-m
            opciones.append(aumento)

        else:
            aumento = aumento*aumento
            if(aumento>m):
                while (aumento>m):
                    aumento = aumento-m
            opciones.append(aumento)

    print opciones

    opciones.reverse()


    while (contador<limite):
        if (binario[contador] == "1"):
            multiplicar = multiplicar * opciones[contador]
        contador = contador +1
    

    if(multiplicar>m):
        while (multiplicar>m):
            multiplicar = multiplicar-m
         
    print "Respuesta: ",multiplicar
    print "**************************"
    print "**************************"
    main()

main()
    







