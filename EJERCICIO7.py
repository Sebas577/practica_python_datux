#Escribe un programa que pida un numero entero si es par o impar.
numero=int(input("Escribe un numero: "))
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")