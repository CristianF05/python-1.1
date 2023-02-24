#suma del numero actual y su anterior

#cracion de las variables para el uso de un ciclo for
n = int(input("numero final:"))
#creacion del ciclo for
print("0 + 0 = 0")
for i in range(1,n+1):
    print(i,"+",i-1,"=",i+(i-1))   
