import random

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

def miller_rabin(n: int, k=5) -> bool:
    """
    Teste de primalidade de Miller-Rabin.
    
    n: Número a ser testado.
    k: Número de iterações do teste (maior valor aumenta a precisão).
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # Escreva n-1 como 2^s * d
    s = 0
    d = n - 1
    while (d % 2) == 0:
        d //= 2
        s += 1
    
    # Realize k testes
    for _ in range(k):
        a = random.randint(2, n - 2) # Único uso da classe random
        x = modular_exponentiation(a, d, n)
        
        if x == 1 or x == (n - 1):
            continue
        
        for _ in range(s - 1):
            x = modular_exponentiation(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True