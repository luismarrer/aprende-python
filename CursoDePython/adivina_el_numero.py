import random

print("Bienvenido a mi juego")
user_num = int(input("Estoy pensando un número del 1 al 10. ¿Puedes adivinar cuál es?\n"))
win_num = random.randint(1, 10)
if user_num == win_num:
    print("¡Ehnorabuena haz ganado!")

if user_num > 10:
    print("Te has pasado un poco.")
if user_num < 1:
    print("Te has quedado corto")
print(f"El número ganador era {win_num}")