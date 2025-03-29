"""
#Ejemplo:
texto_usuario = "Hola, me llamo Nate. ¿Tu como te llamas?"

# Output esperado
# espacios = 6
# puntos = 1
# comas = 1

"""
espacios = 0
puntos = 0
comas = 0

texto_usuario = input("Introduzca un texto: ")

for caracter in texto_usuario:
    if caracter == " ":
        espacios += 1
    elif caracter == ".":
        puntos += 1
    elif caracter == ",":
        comas += 1

print(f"Espacios {espacios}")
print(f"Puntos {puntos}")
print(f"Comas {comas}")
