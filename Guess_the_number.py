"""
Guess the number
"""
import random


print("""
Bienvenido al juego de adivina el número.
Adivina un número de 1 a 5.
""")

numero_usuario = int(input("Elije el número (de 1 a 5): "))
numero_maquina = random.randint(1, 5)
print(numero_maquina)

if numero_usuario == numero_maquina:
    print("¡Muy bien, adivinaste el número!")
else:
    print("No adivinaste el número :(")
