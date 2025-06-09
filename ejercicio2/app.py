import funcion.operacion as op

n = int(input("Ingrese un número entero positivo para convertir a binario: "))

binario = op.decimal_binario(n)

print(f"\nEl decimal {n} en binario es {binario}")
