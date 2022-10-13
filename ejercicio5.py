#5_Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

usuario=""
codigo=""

usuario=input("Diga el usuario: \n")
codigo=input("Diga la contraseña: \n")

'''
if(usuario!="pepe"):
    print("Error usuario o contraseña incorrectos")
elif(codigo!="asdasd"):
    print("Error usuario o contraseña incorrectos")
else:
    print("Has entrado al sistema")
'''

while(usuario!="pepe" or codigo!="asdasd"):
    print("Error usuario o contraseña incorrectos")
    usuario=input("Diga el usuario: \n")
    codigo=input("Diga la contraseña: \n")

print("Has entrado al sistema")