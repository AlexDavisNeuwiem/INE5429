from random import randint
from time import time

from RandomNumberGenerators.LaggedFibonacciGenerator import *
from RandomNumberGenerators.LinearCongruentialGenerator import *

from PrimeNumberValidators.FermatPrimalityTest import *
from PrimeNumberValidators.MillerRabin import *

def generate_prime_number(generator, test_method) -> int:
    random_number = 0
    number_of_loops = 5

    is_prime = False

    start_time = 0
    end_time = 0

    while not is_prime :
        start_time = time()

        random_number = generator.next()
        if test_method(random_number, number_of_loops):
            is_prime = True

        end_time = time()

    print("Número primo gerado =", random_number)
    print("Tamanho do número gerado:", random_number.bit_length(), "bits.")
    print("Tempo de execução: {:.8f} segundos.\n".format(end_time - start_time))

    return random_number


if __name__ == "__main__":

    print("=" * 100)

    print("\nFERMAT PRIMALITY TEST\n")

    # Definindo o tamanho dos números primos gerados
    bit_lengths =  [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048] # 4096

    for size in bit_lengths:
        # Parâmetros escolhidos conforme o site: https://en.wikipedia.org/wiki/Linear_congruential_generator
        a = 1664525
        c = 1013904223
        m = 2**size

        # Gerando a semente inicial com random
        seed = randint(1, m-1)

        # Criando uma instância do LCG
        lcg = LinearCongruentialGenerator(seed, a, c, m)

        # Testando a primalidade dos números aleatórios gerados
        generate_prime_number(lcg, fermat_primality_test)

    print("=" * 100)

    print("\nMILLER-RABIN PRIMALITY TEST\n")

    for size in bit_lengths:
        # Parâmetros escolhidos conforme o site: https://en.wikipedia.org/wiki/Linear_congruential_generator
        a = 1664525
        c = 1013904223
        m = 2**size

        # Gerando a semente inicial com random
        seed = randint(1, m-1)

        # Criando uma instância do LCG
        lcg = LinearCongruentialGenerator(seed, a, c, m)

        # Testando a primalidade dos números aleatórios gerados
        generate_prime_number(lcg, miller_rabin)
    
    print("=" * 100)
