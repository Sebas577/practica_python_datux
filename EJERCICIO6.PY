#Escribe un programa que pida tu edad y muestre si es mayor  de edad o no lo es.

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad>=18:
    print("Usted si es mayor de edad 😀 ")
elif edad<=17:
    print("Usted no es mayor de edad ☹️ ")