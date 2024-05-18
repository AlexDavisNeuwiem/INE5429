class LaggedFibonacciGenerator:
    def __init__(self, seed, j=5, k=17, m=2**32):
        self.j = j
        self.k = k
        self.m = m
        self.state = seed.copy()
        self.index = 0

    def next(self):
        new_value = (self.state[self.index - self.j] + self.state[self.index - self.k]) % self.m
        self.state[self.index] = new_value
        self.index = (self.index + 1) % len(self.state)
        return new_value

    def generate_sequence(self, n):
        sequence = []
        for _ in range(n):
            sequence.append(self.next())
        return sequence
