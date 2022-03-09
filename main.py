from GenAlg import GenAlg
from Fitness import *
from Crossover import *
from Evaluation import *

import time

l = 40
N = 10


# fitness = counting_ones
# fitness = TrapFunc(4, 1).trap_tl
# fitness = TrapFunc(4, 1).trap_ntl
# fitness = TrapFunc(4, 2.5).trap_tl
fitness = TrapFunc(4, 2.5).trap_ntl

crossover = uni_x
# crossover = two_x


def run20(GA):
    suc = 0
    gens = []
    avgfit = []
    cpus = []

    for i in range(20):
        start = time.process_time()
        re = GA.run()
        end = time.process_time()
        if re:
            suc += 1
            gens.append(GA.generation)
            avgfit.append(GA.avgfitness)
            cpus.append(end-start)

    if suc >= 19:
        print('success:', GA.N)
        print('generation:', sum(gens)/len(gens), std(gens))
        print('average fitness', sum(avgfit)/len(avgfit), std(avgfit))
        print('average cpu', sum(cpus)/len(cpus), std(cpus))
        return True

    return False


def search(N):
    print('searching: ' + str(N))
    GA = GenAlg(l, N, crossover, fitness)
    if run20(GA):
        N = binary_search(N // 2, N)
        print('final N:'+str(N))
        return N
    elif N == 1280:
        return 'FAIL'
    else:
        search(2 * N)


def binary_search(left, right):
    while True:
        mid = (right + left)//2
        if mid % 10 != 0:
            return right
        print('searching: ' + str(mid))
        GA = GenAlg(l, mid, crossover, fitness)
        if run20(GA):
            right = mid
        else:
            left = mid


if __name__ == "__main__":
    search(N)
