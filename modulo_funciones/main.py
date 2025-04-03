

def potencia(num, pot=2):
    return num ** pot



def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    for _ in range(n - 1):
        c = a + b
        a = b
        b = c
    return b

def fibonacci_recursivo_nate(n):
    if n <= 1:
        return 1
    return fibonacci_recursivo_nate(n-1) + fibonacci_recursivo_nate(n-2)

def fibonacci_recursivo(n):
    if n < 2:
        return n
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def main():
    # for f in range(8):
    #     print(fibonacci(f))
    #     print(fibonacci_recursivo(f))
    print(potencia(4, 5))


if __name__ == "__main__":
    main()