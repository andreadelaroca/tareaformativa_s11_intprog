def decimal_binario(num):
    if num < 0:
        print("El número debe ser un entero positivo.")
        return None
    while num > 0:
        binario = num % 2
        num = num // 2
    print(f"\nEl número en binario es {binario}")
    return binario

