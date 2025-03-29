

"""
# Ejemplo:
texto_usuario = "Hola, me llamo Nate. ¿Tu como te llamas?

# Output esperado
mayusculas = 3
"""

import string

print("Bienvenido al contado de mayusculas.")
texto_del_usario = input("Ingresa un texto: ")
mayusculas = 0

for caracter in texto_del_usario:
    if caracter in string.ascii_uppercase:
        mayusculas += 1

print(f"Total de mayusculas: {mayusculas}")