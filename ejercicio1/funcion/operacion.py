def calcular_factorial(num):
    if num < 0:
        print("El número debe ser un entero positivo.")
        return None
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial

