"""
# Números usuario
numeros = [1, 2, 3, 4, 5, 6]

# Output
numero_mas_pequenio: 1
numero_mas_grande: 6
"""

# Mi solución
# numeros = list(input("Añade una lista de numeros: "))
#
# print(numeros)
#
# print("Número más pequeño es {}".format(min(numeros)))
# print("Número más grande es {}".format(max(numeros)))

# Programa con while loop

# numeros_de_usuario = []
#
# numero_introducido = int(input("Introduzca un número en la lista: "))
# numeros_de_usuario.append(numero_introducido)
#
# while input("¿Desea introducir más números? [S/N]") == "S":
#     numero_introducido = int(input("Introduzca un número en la lista: "))
#     numeros_de_usuario.append(numero_introducido)
#
# print(numeros_de_usuario)


numeros_introducidos = input("Introduzca los números separados por coma: ")
numeros_de_usuario = [int(numero) for numero in numeros_introducidos.split(",")] # list comprehension

numero_mas_pequenio = numeros_de_usuario[0]
numero_mas_grande = numeros_de_usuario[0]

for numero in numeros_de_usuario[1:]: # Slicing, filtrado de listas
    if numero > numero_mas_grande:
        numero_mas_grande = numero

    if numero < numero_mas_pequenio:
        numero_mas_pequenio = numero

print(numeros_de_usuario)
print(f"El número más pequeño es {numero_mas_pequenio}. El número más grande es {numero_mas_grande}")
