class LinearCongruentialGenerator:
    def __init__(self, seed: int, a: int, c: int, m: int):
        """
        seed: Valor inicial.
        a: Múltiplicador.
        c: Incremento.
        m: Módulo.
        """
        self.a = a
        self.c = c
        self.m = m
        self.x = seed

    def next(self) -> int:
        """
        Abaixo, vamos aplicar a fórmula   Xn = (aX[n-1] + c) mod m   para gerar um elemento aleatório
        Implementação baseada nos sites:
            - https://en.wikipedia.org/wiki/Linear_congruential_generator
            - https://learn.microsoft.com/en-us/archive/msdn-magazine/2016/august/test-run-lightweight-random-number-generation
        """
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def generate_sequence(self, n: int) -> list[int]:
        # Aplica o método next() n vezes e armazena os resultados em uma lista
        sequence = []
        for _ in range(n):
            sequence.append(self.next())
        return sequence

