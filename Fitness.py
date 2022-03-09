
def counting_ones(p):
    return sum(p)


class TrapFunc:
    def __init__(self, k, d):
        self.k = k
        self.d = d

    def trap_tl(self, p):
        b = 0
        for i in range(len(p) // self.k):
            if sum(p[i * self.k:i * self.k + self.k]) == self.k:
                b += self.k
            else:
                x = self.k - self.d - (self.k - self.d) / (self.k - 1) * sum(p[i * self.k:i * self.k + self.k])
                b += x
        return b

    def trap_ntl(self, p):
        b = 0
        for i in range(len(p) // self.k):
            subfunction = []
            for j in range(self.k):
                subfunction.append(p[j * 10 + i])
            if sum(subfunction) == self.k:
                b += self.k
            else:
                x = self.k - self.d - (self.k - self.d) / (self.k - 1) * sum(subfunction)
                b += x
        return b


if __name__ == "__main__":
    p = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # fitness = counting_ones
    # fitness = TrapFunc(4, 1).trap_tl
    # fitness = TrapFunc(4, 1).trap_ntl
    # fitness = TrapFunc(4, 2.5).trap_tl
    fitness = TrapFunc(4, 2.5).trap_ntl
    print(fitness(p))
