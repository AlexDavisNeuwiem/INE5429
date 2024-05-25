from random import randint

from RandomNumberGenerators.LaggedFibonacciGenerator import *
from RandomNumberGenerators.LinearCongruentialGenerator import *

def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    """
    Função para realizar a exponenciação modular.
    """
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:  # Se o expoente é ímpar, multiplique a base com o resultado
            result = (result * base) % modulus
        exponent //= 2 # Divida o expoente por 2
        base = (base * base) % modulus  # Eleve a base ao quadrado
    return result

def fermat_primality_test(n: int, k: int) -> bool:
    """
    Teste de primalidade de Fermat.
    
    n: Número a ser testado.
    k: Número de iterações do teste (maior valor aumenta a precisão).
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    for _ in range(k):
        a = randint(2, n - 1) # Único uso da classe random
        if modular_exponentiation(a, n - 1, n) != 1:
            return False
    
    return True
