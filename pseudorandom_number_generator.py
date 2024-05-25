from random import randint
from time import time

from RandomNumberGenerators.LaggedFibonacciGenerator import *
from RandomNumberGenerators.LinearCongruentialGenerator import *

def generate_pseudorandom_number(generator) -> int:
    start_time = time()
    generated_number = generator.next()
    end_time = time()

    print("Número pseudo-aleatório gerado =", generated_number)
    print("Tamanho do número gerado:", generated_number.bit_length(), "bits.")
    print("Tempo de execução: {:.8f} segundos.\n".format(end_time - start_time))

    return generated_number


if __name__ == "__main__":

    print("=" * 100)

    print("\nLAGGED FIBONACCI GENERATOR\n")

    # Definindo o tamanho dos números primos gerados
    bit_lengths =  [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

    for size in bit_lengths:
        # Parâmetros
        j = 5
        k = 17
        m = 2**size

        # Gerando sementes iniciais com random
        seed = [randint(1, m-1) for _ in range(k)]

        # Criando uma instância de LFG
        lfg = LaggedFibonacciGenerator(seed, j, k, m)

        # Testando a primalidade dos números aleatórios gerados
        generate_pseudorandom_number(lfg)

    print("=" * 100)

    print("\nLINEAR CONGRUENTIAL GENERATOR\n")

    for size in bit_lengths:
        # Parâmetros
        a = 1664525
        c = 1013904223
        m = 2**size

        # Gerando a semente inicial com random
        seed = randint(1, m-1)

        # Criando uma instância do LCG
        lcg = LinearCongruentialGenerator(seed, a, c, m)

        # Testando a primalidade dos números aleatórios gerados
        generate_pseudorandom_number(lcg)
    
    print("=" * 100)
