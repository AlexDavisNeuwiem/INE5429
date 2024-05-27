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
        if (exponent % 2) == 1:  # Se o expoente é ímpar, vamos multiplicar a base com o resultado
            result = (result * base) % modulus
        exponent //= 2 # Dividindo o expoente por 2
        base = (base * base) % modulus  # Elevando a base ao quadrado
    return result

def fermat_primality_test(n: int, k: int) -> bool:
    """
    Teste de primalidade de Fermat.
    
    n: Número a ser testado.
    k: Número de iterações do teste (maior valor aumenta a precisão).
    """
    # Se n for negativo ou 1
    if n <= 1:
        return False
    # Se n for 2 ou 3
    if n <= 3:
        return True
    # Se n for par
    if n % 2 == 0:
        return False
    
    """
    Implementação baseada nos sites:
        - https://en.wikipedia.org/wiki/Fermat_primality_test
        - https://www.geeksforgeeks.org/fermat-method-of-primality-test/
    """
    
    # Realizando k testes
    for _ in range(k):
        a = randint(2, n - 1) # Único uso da classe random
        if modular_exponentiation(a, n - 1, n) != 1:
            return False
    
    return True
