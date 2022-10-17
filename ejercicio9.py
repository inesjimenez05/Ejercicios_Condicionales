#9_Algoritmo que pida tres números y los muestre ordenados (de mayor a menor).

num1=0
num2=0
num3=0
vNumeros=[]

num1=int(input("Di un número: \n"))
num2=int(input("Di otro número: \n"))
num3=int(input("Di un númera: \n"))

vNumeros.append(num1)
vNumeros.append(num2)
vNumeros.append(num3)

vNumeros.sort(reverse=True)
print("El mayor es", vNumeros[0])
print("El menor es", vNumeros[2])
ultimo= len(vNumeros)
print("El ultimo numero es", vNumeros[ultimo-1])


print(vNumeros)