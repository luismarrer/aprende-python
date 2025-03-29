

lista_de_la_compra = ["leche", "arroz", "jamon"]

for item in lista_de_la_compra:
    print(f"Hoy voy a comprar {item}")


vocales = ["a", "e", "i", "o", "u"]
count_vocales = 0
frase = "hola, hoy estoy aprendiendo Python"


for letra in frase:
    if letra in vocales:
        print(f"{letra} es una vocal en la frase")
        count_vocales += 1

print(f"Vocales encontradas: {count_vocales}")