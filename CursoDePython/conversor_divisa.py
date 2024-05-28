
welcome = "Bienvenido al conversor de divisas"

print("\n" + welcome + "\n" + len(welcome) * "-" + "\n")

conversor_type = input("¿Cómo quieres hacer la conversión? (Seleccione una opción [A, B, C, D])\n"
                       "A: Dolar a euro\n"
                       "B: Euro a dolar\n"
                       "C: Libra a Euro\n"
                       "D: Euro a libra\n")

user_money = float(input("Ingrese la cantidad: "))

money_type = ""
new_money_type = ""
dollar_euro = 0.92
libra_euro = 1.18
text = "La cantidad ingresada en {} es {:.2f}. En {} es {:.2f}."

if conversor_type == "A":
    money_type = "dólares"
    new_money_type = "euros"
    result = user_money * dollar_euro
elif conversor_type == "B":
    money_type = "euros"
    new_money_type = "dólares"
    result = user_money / dollar_euro
elif conversor_type == "C":
    money_type = "libras"
    new_money_type = "euros"
    result = user_money * libra_euro
elif conversor_type == "D":
    money_type = "euros"
    new_money_type = "libras"
    result = user_money / libra_euro
else:
    print("Opción no es valida. Las opciones son: A, B, C y D.")
    exit()

print(text.format(money_type, user_money, new_money_type, result))
