from GenAlg import GenAlg
from Fitness import *
from Crossover import *

l = 40
N = 10


fitness = counting_ones
# fitness = TrapFunc(4, 1).trap_tl
# fitness = TrapFunc(4, 1).trap_ntl
# fitness = TrapFunc(4, 2.5).trap_tl
# fitness = TrapFunc(4, 2.5).trap_ntl


def search(N):
    GA = GenAlg(l, N, fitness)
    if GA.run():
        N = binary_search(N // 2, N)
        return N
    else:
        search(2 * N)


def binary_search(left, right):
    while True:
        mid = (right + left)//2
        if mid % 10 != 0:
            return right
        GA = GenAlg(l, mid, fitness)
        if GA.run():
            right = mid
        else:
            left = mid
