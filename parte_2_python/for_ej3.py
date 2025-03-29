"""
# Numero elegido por el usuario: 2, output esperado:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
"""

numero = int(input("Ingresa un numero a multiplicar: "))

for a in range(1, 11):
    if a % 2 == 0:
        print(f"{numero} x {a} = {numero * a}")