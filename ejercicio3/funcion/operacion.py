import math

def potencia_numero_exponente (num, exp):
    if num < 0 or exp < 0:
        print("Los valores deben ser enteros positivos.")
        return None
    potencia = math.pow(num, exp)
    print(f"\n{num}^{exp} = {potencia}")
    suma = sum(int(digit) for digit in str(int(potencia)))
    print(f"La suma de los dígitos de {int(potencia)} es {suma}")
    return suma