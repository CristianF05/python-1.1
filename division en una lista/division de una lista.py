#Desarrolle un algoritmo y que muestre los numeros
#divisibles entre 5 de una lista de números.
#creaccion de la lista
num = [20,12,23,25,40]
#creacion del bucle for
for n in num:
    #creacion de if para hallar los divisores de 5
    if (n%5 == 0):
        #imprimir los divisibles por 5
        print(n)
