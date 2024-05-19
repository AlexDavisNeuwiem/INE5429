import random

from RandomNumberGenerators.LaggedFibonacciGenerator import *
from RandomNumberGenerators.LinearCongruentialGenerator import *

from PrimeNumberValidators.FermatPrimalityTest import *
from PrimeNumberValidators.MillerRabin import *

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


    '''
    ===== TESTE DO FPT =====
    '''

    numero = 547349664017
    print(f"\nTamanho de {numero} em bits:", numero.bit_length())
    if fermat_primality_test(numero):
        print("Esse número é provavelmente primo pelo teste de Fermat.")
    else:
        print("Esse número é composto.")


    '''
    ===== TESTE DO MR =====
    '''

    numero = 29
    k = 5  # número de iterações
    print(f"\nTamanho de {numero} em bits:", numero.bit_length())
    if miller_rabin(numero, k):
        print("Esse número é provavelmente primo pelo algoritmo de Miller-Rabin.")
    else:
        print("Esse número é composto.")
