import random


class GenAlg:
    def __init__(self, l, N, crossover, fitness):
        self.l = l
        self.N = N
        self.P = self.instances()
        self.crossover = crossover
        self.fitness = fitness

        self.generation = 0
        self.avgfitness = 0

        self.prop = []
        self.error = []
        self.correct = []

    def instances(self):
        ins = []
        for i in range(self.N):
            current_ins = []
            for j in range(self.l):
                current_ins.append(random.randint(0,1))
            ins.append(current_ins)
        return ins

    def evo(self):
        group = self.P.copy()
        random.shuffle(group)
        group = zip(*(iter(group),) * 2)
        family = [[[p, self.fitness(p)] for p in (g + self.crossover(g))] for g in group]
        return family

    def run(self):
        counter = 0
        maxf = 0
        while True:
            counter += 1
            family = self.evo()
            nextP = []
            for f in family:
                f = sorted(f, key=lambda x: x[1], reverse=True)
                if f[0][1] > maxf:
                    counter = 0
                    maxf = f[0][1]
                f = [p[0] for p in f[:2]]
                nextP += f
            print(maxf)
            if maxf == self.l:
                return True
            if counter == 5:
                return False
            self.P = nextP


if __name__ == "__main__":
    a = (1,2,3)
    b = (3,4,5)
    print(list(zip(a,b)))

    xor = [i*j for i, j in zip(a,b)]
    print(xor)
    # c = [a,b]
    # random.shuffle(P)
    # group = zip(*(iter(P),) * 2)
    # sorted(c, key=lambda x: x[1], reverse=True)
    # print(sum(a))
