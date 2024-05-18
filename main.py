import random

from NumerosAleatorios.LaggedFibonacciGenerator import *
from NumerosAleatorios.LinearCongruentialGenerator import *

from NumerosPrimos.FermatPrimalityTest import *
from NumerosPrimos.MillerRabin import *

if __name__ == "__main__":

    '''
    ===== TESTE DO LFG =====
    '''

    # Parâmetros
    j = 5
    k = 17
    m = 2**32

    # Gerando sementes iniciais
    seed = [random.randint(1, m-1) for _ in range(k)]

    lfg = LaggedFibonacciGenerator(seed, j, k, m)

    # Gerar uma sequência de 10 números pseudoaleatórios
    sequence = lfg.generate_sequence(10)
    print("TESTE DO LFG =>", sequence)

    '''
    ===== TESTE DO LCG =====
    '''

    # Parâmetros
    a = 1664525
    c = 1013904223
    m = 2**32

    # Gerando a semente inicial
    seed = random.randint(1, m-1)

    # Criar uma instância do LCG
    lcg = LinearCongruentialGenerator(seed, a, c, m)

    # Gerar uma sequência de 10 números pseudoaleatórios
    sequence = lcg.generate_sequence(10)
    print("\nTESTE DO LCG =>", sequence)
