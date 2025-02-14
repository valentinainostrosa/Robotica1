import math

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

# Ejemplo de uso
radio = float(input("Introduce el radio del círculo: "))
perimetro = calcular_perimetro_circulo(radio)
print(f"El perímetro del círculo es: {perimetro}")