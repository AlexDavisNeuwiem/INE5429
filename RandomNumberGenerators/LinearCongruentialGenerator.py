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
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def generate_sequence(self, n: int) -> list[int]:
        sequence = []
        for _ in range(n):
            sequence.append(self.next())
        return sequence

