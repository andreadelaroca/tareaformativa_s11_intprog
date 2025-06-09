def decimal_binario(num):
    binario = "" #str vacío para almacenar binario
    if num < 0:
        print("El número debe ser un entero positivo.")
        return None
    while num > 0:
        binario = str(num % 2) + binario
        n //= 2
    print(f"\nEl número en binario es {binario}")
    return binario
