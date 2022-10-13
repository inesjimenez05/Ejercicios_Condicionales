#1_Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

num1=0
num2=0

num1=int(input("Di un número: \n"))
num2=int(input("Di otro número: \n"))

if(num1>num2):
    print(num1, "es mayor que ", num2)
else:
    print(num1, "no es mayor que ", num2)