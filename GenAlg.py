import random
from Evaluation import *


class GenAlg:
    """Genetic algorithm"""
    def __init__(self, l, N, crossover, fitness):
        self.l = l
        self.N = N
        self.P = []
        self.crossover = crossover
        self.fitness = fitness

        self.Pwf = []

        self.generation = 0
        self.avgfitness = 0

        self.prop = []
        self.error = []
        self.correct = []
        self.schematadata = []

    def initP(self, P):
        return [[p, self.fitness(p)]for p in P]

    def reinit(self):
        """initialize the population"""
        self.P = self.instances()

        self.Pwf = self.initP(self.P)

        self.generation = 0
        self.avgfitness = 0

        self.prop = []
        self.error = []
        self.correct = []
        self.schematadata = []

    def instances(self):
        ins = []
        for i in range(self.N):
            current_ins = []
            for j in range(self.l):
                current_ins.append(random.randint(0,1))
            ins.append(current_ins)
        return ins

    def evo(self):
        """generate family"""
        group = self.P.copy()
        random.shuffle(group)
        group = zip(*(iter(group),) * 2)
        family = [[[p, self.fitness(p)] for p in (g + self.crossover(g))] for g in group]
        return family

    def run(self):
        """run the evo"""
        self.reinit()
        counter = 0
        maxf = 0
        while True:
            counter += 1
            family = self.evo()
            nextP = []

            nextPwf = []
            err = 0
            corr = 0

            self.prop.append(one_bit_proportion(self.Pwf))
            self.schematadata.append(average_and_std(self.Pwf))
            self.avgfitness += average_fi(self.Pwf)

            # do family competition
            for f in family:
                sortedf = sorted(f, key=lambda x: x[1], reverse=True)
                if sortedf[0][1] > maxf:
                    counter = 0
                    maxf = sortedf[0][1]
                winner = [p[0] for p in sortedf[:2]]
                nextP += winner

                # err and corr
                parents = [p[0] for p in f[:2]]
                winnerwf = [p for p in sortedf[:2]]
                nextPwf += winnerwf
                er, cor = err_and_corr(parents, winner)
                err += er
                corr += cor

            self.error.append(err)
            self.correct.append(corr)

            if maxf == self.l:
                self.avgfitness = self.avgfitness / self.generation
                return True
            if counter == 5:
                self.avgfitness = self.avgfitness / self.generation
                return False

            self.generation += 1

            self.P = nextP
            self.Pwf = nextPwf


if __name__ == "__main__":
    pass
    # a = (1,2,3)
    # b = (3,4,5)
    # print(list(zip(a,b)))
    #
    # xor = [i*j for i, j in zip(a,b)]
    # print(xor)
    # c = [a,b]
    # random.shuffle(P)
    # group = zip(*(iter(P),) * 2)
    # sorted(c, key=lambda x: x[1], reverse=True)
    # print(sum(a))
