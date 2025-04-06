
lista = []
for c in range(1,7) :
    valor = float(input("valor {}: ".format(c)))
    lista.append(valor) 
for valor in lista :
    print(valor**2)