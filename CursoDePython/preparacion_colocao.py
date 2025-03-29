print("Me voy a la cocina")
print("Miro la nevera")

hay_leche = input("¿Hay Leche? (S/N)\n")
hay_colocao = input("¿Hay Colocao? (S/N)\n")

if hay_leche != "S" or hay_colocao != "S":
    print("Voy a comprar al super.")
    if hay_leche != "S":
        print("Compro leche")
    if hay_colocao != "S":
        print("Compro colacao")

print("Ponemos la leche en el vaso")
print("Ponemos el colocao en el vaso")
print("Mezclamos")