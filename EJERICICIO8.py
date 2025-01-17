#Escribe un programa que pida un numero entero y calcule la suma 1 hasta el numero ingresado.

numeros=int(input("Escribe un numero: "))

suma=sum(range(1, numeros + 1))        #range genera los números uno por uno cuando se necesitan, lo que lo hace más eficiente para cálculos grandes.

print (f"La suma de 1 hasta {numeros} es: {suma}")