#7_Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
# El exponente sea positivo, sólo tienes que imprimir la potencia.
# El exponente sea 0, el resultado es 1.
# El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base=0
exponente=0

base=int(input("Diga la base de la potencia: \n"))
exponente=int(input("Diga el exponente: \n"))

if(exponente>=1):
    print(base,"^",exponente,"=",base**exponente)

elif(exponente==0):
    print(base,"^",exponente,"=",1)
else:
    print(base,"^",exponente,"=","1 /",(base**(-1*exponente)))
