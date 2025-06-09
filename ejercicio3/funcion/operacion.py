import math

def suma_numero_exponente (num, exp):
    if num < 0 or exp < 0:
        print("Los valores deben ser enteros positivos.")
        return None
    resultado = math.pow(num, exp)