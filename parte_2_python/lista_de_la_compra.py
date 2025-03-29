
lista_de_la_compra = []
element = ""
print(f"Bienvenido a su lista de compras. Estos son los elementos que tiene añadidos actualmentes en su lista {lista_de_la_compra}.")

while True:
    element = input("¿Qué quiere añádir en su lista de la compra? ([Q] para salir) ")
    if element == "Q":
        break
    elif element in lista_de_la_compra:
        print(f"{element} ya está en la lista, no hace falta añadirlo otra vez.")
    else:
        choice = input(f"¿Seguro qué quiere añádir {element}? [S/N] ")
        if choice == "S":
            lista_de_la_compra.append(element)
            print(f"{element} añadido exitosamente.")

print("La lista de la compra es:")
print(lista_de_la_compra)
