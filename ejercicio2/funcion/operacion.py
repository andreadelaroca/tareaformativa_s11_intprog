def decimal_binario(num):
    binario = "" #str vacío para almacenar binario
    if num < 0:
        print("El número debe ser un entero positivo.")
        return None
    while num // 2 > 0:
        binario = str(num % 2) + binario
        num = num // 2
    return str(num) + binario
    