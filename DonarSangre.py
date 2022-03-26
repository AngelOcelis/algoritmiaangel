edad=int(input("digite su edad: "))
peso=float(input("digite su peso: "))
pulso=int(input("digite su pulso: "))
plaquetas=int(input("digite la cantidad de plaquetas: "))

if (edad>=18 and edad<60) and (peso>50 and peso<100) and (pulso>50) and (plaquetas>150000):
    print("Apto para donar")
else:
    print("No es apto para donar")