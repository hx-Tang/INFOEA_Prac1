import random


class GenAlg:
    def __init__(self, l, N, crossover, fitness):
        self.l = l
        self.N = N
        self.P = []
        self.crossover = crossover
        self.fitness = fitness

    def instances(self):
        self.P = []
        for i in range(self.N):
            current_ins =[]
            for j in range(self.l):
                current_ins.append(random.randint(0,1))
            self.append(current_ins)
        return self.P

    def evo(self):
        group = self.P.copy()
        random.shuffle(group)
        group = zip(*(iter(group),) * 2)
        family = [[[p, self.fitness(p)] for p in g + self.crossover(g)] for g in group]
        return family

    def run(self):
        while True:
            family = self.evo()
            counter = 0
            nextP = []
            for f in family:
                if f[0][1] >= f[2][1] and f[0][1] >= f[3][1] and f[1][1] >= f[2][1] and f[1][1] >= f[3][1]:
                    counter += 1
                if counter == 5:
                    return False
                sorted(f, key=lambda x: x[1])
                if f[0] == self.l:
                    return True
                f = [p[0] for p in f[:2]]
                nextP += f
            self.P = nextP


if __name__ == "__main__":
    a = (2, 3)
    b = (1, 3)
    # random.shuffle(P)
    # group = zip(*(iter(P),) * 2)
    print(a + b)
