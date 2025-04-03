
SALIDA = "SALIR"
ARCHIVO_LISTA = "lista_compra.txt"
# LISTA = "LISTA"
# PRODUCTS = ["Pan", "Pollo", "Pipas"]

# def preguntar_producto_usuario():
#     info = "Introduce un producto [{} para lista los productos disponibles] [{} para salir] ".format(LISTA, SALIDA)
#     user_input = input(info)
#     while user_input not in PRODUCTS and user_input != SALIDA and user_input != LISTA:
#         print("Lo siento. Debes elegir un producto de la lista.")
#         user_input = input(info)
#     return user_input
#
#
# def save_shopping_list(archivo, lista_de_la_compra):
#     with open(archivo, "w") as mi_archivo:
#         mi_archivo.write("\n".join(lista_de_la_compra))

def preguntar_producto_usuario():
    info = "Introduce un producto [{} para salir] ".format(SALIDA)
    return input(info)
    # user_input = input(info)
    # while user_input not in PRODUCTS and user_input != SALIDA and user_input != LISTA:
    #     print("Lo siento. Debes elegir un producto de la lista.")
    #     user_input = input(info)
    # return user_input

def guardar_lista_a_disco(lista_compra):
    with open(ARCHIVO_LISTA, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))

def guardar_item_en_lista(lista_compra, item_a_guardar):
    if item_a_guardar.lower() in [a.lower() for a in lista_compra]:
        print("El producto ya existe")
    else:
        lista_compra.append(item_a_guardar)

def cargar_o_crear_lista():
    lista_compra = []
    if input("¿Quieres cargar la última lista de la compra? [S/N] ") == "S":
        try:
            with open(ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("¡Archivo de la compra no encontrado! ")
    return lista_compra

def mostrar_lista(lista_compra):
    print("\n".join(lista_compra))

def main():
    lista_compra = cargar_o_crear_lista()
    mostrar_lista(lista_compra)
    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIDA:
        guardar_item_en_lista(lista_compra, input_usuario)
        mostrar_lista(lista_compra)
        input_usuario = preguntar_producto_usuario()
        # input_usuario = preguntar_producto_usuario()
        # if input_usuario == LISTA:
        #     print(f"Estos son los productos que puedes añadir a tu lista {PRODUCTS}")
        # elif input_usuario == SALIDA:
        #     continue
        # else:
        #     lista_de_la_compra.append(input_usuario)
        #     print("\n".join(lista_de_la_compra))

    guardar_lista_a_disco(lista_compra)



if __name__ == "__main__":
    main()