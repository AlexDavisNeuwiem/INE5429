import random

from RandomNumberGenerators.LaggedFibonacciGenerator import *
from RandomNumberGenerators.LinearCongruentialGenerator import *

def exp_modular(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

def teste_fermat(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    for _ in range(k):
        a = random.randint(2, n - 1) # Substituir
        if exp_modular(a, n - 1, n) != 1:
            return False
    
    return True
