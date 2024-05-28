title = "Bienvenido al test sobre el queso"
print("\n" + title + "\n" + len(title) * "-")
score = 0

option = input("Pregunta 1: Que hacer cuando ves una tabla de quesos?\n"
               "A - Salgo corriendo\n"
               "B - Pruebo uno de los quesos o incluso varios\n"
               "C - No puedo evitar devorarla\n")
if option == "A":
    score += 0
elif option == "B":
    score += 5
elif option == "C":
    score += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

option = input("Pregunta 2: ¿Como te gusta la hamburguesa?\n"
               "A - Sin queso\n"
               "B - Con queso\n"
               "C - Pan y queso\n")
if option == "A":
    score += 0
elif option == "B":
    score += 5
elif option == "C":
    score += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

option = input("Pregunta 3: ¿Eres intolerante a la lactosa?\n"
               "A - Si\n"
               "B - A veces\n"
               "C - No\n")
if option == "A":
    score += 0
elif option == "B":
    score += 5
elif option == "C":
    score += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

if score >= 25:
    print("Resultado: Felicidades, eres fánatico de los quesos.")
elif score >= 15:
    print("Resultado: Felicidades, eres una persona que le gusta el queso.")
else:
    print("Resultado: Felicidades no te gusta el quesos.")
print(score)