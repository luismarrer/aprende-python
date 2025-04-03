# Ejercicio 1: La string más larga
def string_mas_larga(*args):
    larger_word = ""
    for word in args:
        if len(word) > len(larger_word):
            larger_word = word
    return larger_word
print(string_mas_larga("hola", "como", "estas"))

# Ejercicio 2: Sumando la lista
def suma(num_list):
    result = 0
    for number in num_list:
        result += number
    return result
print(suma([1, 2, 3, 4, 5]))

# Ejercicio 3: Par o impar
def es_impar(num):
    return num % 2 != 0
print(es_impar(3))
print(es_impar(24))

# Ejercicio 4: Pregunta algo
def sure():
    return input("¿Estás seguro? [S]í o [N]o ").capitalize() == "S"
print(sure())

# Ejercicio 5: A mayus
def all_capitalize(string):
    new_string = ""
    for letter in string:
        if "a" <= letter <= "z":
            new_string += chr(ord(letter) - 32)
        else:
            new_string += letter
    return new_string
print(all_capitalize("hola me llamo luiS E. M"))

# Ejercicio 6: Adivina el número
def guess_number(num):
    while int(input("Adivina el número del 1 al 100: ")) != num:
        print("Prueba otra vez.")
    print("¡Muy bien! Adivinaste.")
guess_number(56)

# Ejercicio 7: Lista de la compra
def shopping_list(my_list):
    print(my_list)
    new_item = input("Añade un nuevo elemento a lista: ")
    if new_item not in my_list:
        my_list.append(new_item)
    else:
        print("El elemento ya se encuentra en la lista.")
    print(my_list)

shopping_list(['huevo', 'pan', 'leche', 'jamon'])
