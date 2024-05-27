class LaggedFibonacciGenerator:
    def __init__(self, seed: list[int], j: int, k: int, m: int):
        """
        seed: Sequência inicial de números inteiros.
        j: Índice de um valor anterior à k na sequência.
        k: Índice de um valor anterior à n na sequência.
        m: Módulo.
        """
        self.j = j
        self.k = k
        self.m = m
        self.x = seed.copy()
        self.index = 0

    def next(self) -> int:
        """
        Abaixo, vamos aplicar a fórmula   Xn = (X[n-j] + X[n-k]) mod m   para um elemento da sequência
        Implementação baseada nos sites:
            - https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator
            - https://learn.microsoft.com/en-us/archive/msdn-magazine/2016/august/test-run-lightweight-random-number-generation

        """
        new_value = (self.x[self.index - self.j] + self.x[self.index - self.k]) % self.m
        self.x[self.index] = new_value
        self.index = (self.index + 1) % len(self.x)
        return new_value

    def generate_sequence(self, n: int) -> list[int]:
        # Aplica o método next() n vezes e armazena os resultados em uma lista
        sequence = []
        for _ in range(n):
            sequence.append(self.next())
        return sequence
