from RandomNumberGenerators.LaggedFibonacciGenerator import *
from RandomNumberGenerators.LinearCongruentialGenerator import *

from PrimeNumberValidators.FermatPrimalityTest import *
from PrimeNumberValidators.MillerRabin import *

def test_number_primality(sequence: list[int]) -> bool:
    for numero in sequence:
        print(f"\nTamanho do número {numero} em bits:", numero.bit_length())

        # Teste de Primalidade de Fermat
        if fermat_primality_test(numero):
            print("TESTE DE FERMAT: Esse número é provavelmente primo.")
        else:
            print("TESTE DE FERMAT: Esse número é composto.")

        # Miller-Rabin
        if miller_rabin(numero):
            print("MILLER-RABIN: Esse número é provavelmente primo.")
        else:
            print("MILLER-RABIN: Esse número é composto.")
    
    print("=" * 85)


if __name__ == "__main__":

    print("=" * 85)

    """
    Lagged Fibonacci Generator
    """

    # Parâmetros
    j = 5
    k = 17
    m = 2**32

    # Gerando sementes iniciais com random
    seed = [random.randint(1, m-1) for _ in range(k)]

    # Criando uma instância de LFG
    lfg = LaggedFibonacciGenerator(seed, j, k, m)

    # Gerando uma sequência de 5 números pseudoaleatórios
    sequence = lfg.generate_sequence(5)
    print("Valores gerados pelo LFG:", str(sequence).replace("[", "").replace("]", ""))

    # Testando a primalidade dos números aleatórios gerados
    test_number_primality(sequence)

    """
    Linear Congruential Generator
    """

    # Parâmetros
    a = 1664525
    c = 1013904223
    m = 2**32

    # Gerando a semente inicial com random
    seed = random.randint(1, m-1)

    # Criando uma instância do LCG
    lcg = LinearCongruentialGenerator(seed, a, c, m)

    # Gerando uma sequência de 5 números pseudoaleatórios
    sequence = lcg.generate_sequence(5)
    print("Valores gerados pelo LCG:", str(sequence).replace("[", "").replace("]", ""))

    # Testando a primalidade dos números aleatórios gerados
    test_number_primality(sequence)
