from random import randint
from os import system


VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 95

TAMANO_BARRA_VIDA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
    # Se desenvuelven los turnos del combate

    # Turno de Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ataca con Bola Voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
        vida_squirtle -= 11

    if vida_squirtle < 0:
        vida_squirtle = 0
    barra_de_vida_pikachu = int(vida_pikachu * TAMANO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu: [{}{}] ({}/{})".format("*" * barra_de_vida_pikachu, " " * (TAMANO_BARRA_VIDA - barra_de_vida_pikachu),
                                           vida_pikachu, VIDA_INICIAL_PIKACHU))

    barra_de_vida_squirtle = int(vida_squirtle * TAMANO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle: [{}{}] ({}/{})".format("*" * barra_de_vida_squirtle, " " * (TAMANO_BARRA_VIDA - barra_de_vida_squirtle),
                                            vida_squirtle, VIDA_INICIAL_SQUIRTLE))
    input("Enter para continuar...\n\n")
    system("clear")

    # Turno Squirtle
    print("Turno Squirtle")

    ataque_squirtle = None
    while ataque_squirtle not in ["P", "A", "B", "N"]:
        ataque_squirtle = input("¿Qué ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ")
    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "C":
        print("Squirtle no hace nada...")
    if vida_pikachu < 0:
        vida_pikachu = 0
    barra_de_vida_pikachu = int(vida_pikachu * TAMANO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu: [{}{}] ({}/{})".format("*" * barra_de_vida_pikachu, " " * (TAMANO_BARRA_VIDA - barra_de_vida_pikachu),
                                           vida_pikachu, VIDA_INICIAL_PIKACHU))

    barra_de_vida_squirtle = int(vida_squirtle * TAMANO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle: [{}{}] ({}/{})".format("*" * barra_de_vida_squirtle, " " * (TAMANO_BARRA_VIDA - barra_de_vida_squirtle),
                                            vida_squirtle, VIDA_INICIAL_SQUIRTLE))
    input("Enter para continuar...\n\n")
    system("clear")
if vida_pikachu > vida_squirtle:
    print("Pikachu gana!")
else:
    print("Squirtle gana!")
