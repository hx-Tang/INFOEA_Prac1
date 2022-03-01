import random

class GenAlg:
    def __init__(self, l, N, crossover, fitness):
        self.N = N
        self.l = l
        self.P = []
        self.crossover = crossover
        self.fitness = fitness
        self.count = 0

    def evo(self):
        ch = []
        random.shuffle(self.P)
        group = zip(*(iter(self.P), *2))

        return ch

    def run(self):
        return True
