numeros = []
for i in range(3):
    numero = float(input("Introduce el número #{}: ".format(i + 1)))
    numeros.append(numero)
menor = numeros[0]
for numero in numeros:
    if numero < menor:
        menor = numero
print("Menor:", menor)