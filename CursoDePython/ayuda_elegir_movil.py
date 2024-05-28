welcome = "Bienvenido a nuestro quiz para seleccionar tu próximo teléfono"
print("\n" + welcome + "\n" + len(welcome) * "-" + "\n")

text = "Tu telefono nuevo debería ser "
text2 = "Opción invalida"
phone = ""

choice = input("iOS o Android [I / A]: ")

if choice == "A":  # Ha contestado Android
    choice = input("Tienes dinero [S / N]: ")
    if choice == "N":  # final_1 No tiene dinero
        phone = "Android chino"
    elif choice == "S":  # Tiene dinero
        choice = input("¿Te importa la cámara? [S / N]: ")
        if choice == "S":  # final_2 Le importa la camara
            phone = "Google Pixel Supercamara"
        elif choice == "N":  # final_3 No le importa la camara
            phone = "Android calidad-precio"
        else:
            phone = text2
    else:
        phone = text2

elif choice == "I":  # Ha contestado iOS
    choice = input("Tienes dinero [S / N]: ")
    if choice == "S":  # final_4 Tiene dinero
        phone = "iPhone Ultra Pro Max"
    elif choice == "N":  # final_5 No tiene dinero
        phone = "iPhone de segunda mano"
    else:
        phone = text2
else:
    phone = text2

print(text + phone)