class LinearCongruentialGenerator:
    def __init__(self, seed: int, a=1664525, c=1013904223, m=2**32):
        """
        seed: Valor inicial
        a: Múltiplicador
        c: Incremento
        m: Módulo
        """
        self.a = a
        self.c = c
        self.m = m
        self.x = seed

    def next(self) -> int:
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def generate_sequence(self, n=5) -> list[int]:
        sequence = []
        for _ in range(n):
            sequence.append(self.next())
        return sequence

