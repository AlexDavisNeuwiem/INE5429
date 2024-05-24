from time import time

from RandomNumberGenerators.LaggedFibonacciGenerator import *
from RandomNumberGenerators.LinearCongruentialGenerator import *

from PrimeNumberValidators.FermatPrimalityTest import *
from PrimeNumberValidators.MillerRabin import *

def generate_prime_number(generator) -> int:
    generated_prime = 0
    number_of_loops = 5

    fermat_test_prime = False
    miller_rabin_prime = False

    start_time = 0
    end_time = 0

    while (not fermat_test_prime) or (not miller_rabin_prime):
        start_time = time()
        random_number = generator.next()
        
        # Teste de Primalidade de Fermat
        if fermat_primality_test(random_number, number_of_loops):
            fermat_test_prime = True
            generated_prime = random_number

        # Miller-Rabin
        if miller_rabin(random_number, number_of_loops):
            miller_rabin_prime = True
            generated_prime = random_number
        end_time = time()

    print("Número primo gerado =", generated_prime)
    print("Tamanho do número gerado:", random_number.bit_length(), "bits.")
    print("Tempo de execução: {:.6f} segundos.".format(end_time - start_time))
    if fermat_test_prime:
        print("Esse número é PROVAVELMENTE PRIMO pelo teste de Fermat.")
    else:
        print("Esse número é COMPOSTO pelo teste de Fermat.")
    if miller_rabin_prime:
        print("Esse número é PROVAVELMENTE PRIMO pelo teste de Miller-Rabin.")
    else:
        print("Esse número é COMPOSTO pelo teste de Miller-Rabin.")
    print("")

    return generated_prime


if __name__ == "__main__":

    print("=" * 100)

    print("\nLAGGED FIBONACCI GENERATOR\n")

    # Definindo o tamanho dos números primos gerados
    bit_lengths =  [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048] # 4096

    for size in bit_lengths:
        # Parâmetros
        j = 5
        k = 17
        m = 2**size

        # Gerando sementes iniciais com random
        seed = [random.randint(1, m-1) for _ in range(k)]

        # Criando uma instância de LFG
        lfg = LaggedFibonacciGenerator(seed, j, k, m)

        # Testando a primalidade dos números aleatórios gerados
        generate_prime_number(lfg)

    print("=" * 100)

    print("\nLINEAR CONGRUENTIAL GENERATOR\n")

    for size in bit_lengths:
        # Parâmetros
        a = 1664525
        c = 1013904223
        m = 2**size

        # Gerando a semente inicial com random
        seed = random.randint(1, m-1)

        # Criando uma instância do LCG
        lcg = LinearCongruentialGenerator(seed, a, c, m)

        # Testando a primalidade dos números aleatórios gerados
        generate_prime_number(lcg)
    
    print("=" * 100)
