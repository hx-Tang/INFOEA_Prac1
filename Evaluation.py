#
# [[0,1,0,1],[]] # len = N
#
# M1= [[0,0,0],[0,0,0]]     # len = 2, 1*parents, 1*winners
# M2= [[0,0,0],[0,1,0]]
# P= [[[0],34],[[0],45]] # len = N

def std(nums):
    avg = sum(nums)/len(nums)
    return (sum(map(lambda e: (e-avg)*(e-avg), nums))/len(nums))**0.5


def one_bit_proportion(P):
        propo = []
        for instance in P:
            propo.append(instance[1]/len(instance[0]))
        return sum(propo)/len(P)


def err_and_corr(M1,M2):
        p1 = M1[0]
        p2 = M1[1]
        w1 = M2[0]
        w2 = M2[1]
        xor = [i^j for i ,j in zip(p1,p2)]
        corr = sum([x*y*k for x, y, k in zip(xor,w1,w2)])
        w11 =[i*j for i, j in zip(xor,w1)]
        w22 =[i*j for i, j in zip(xor,w2)]
        xor_xor=[i^j for i, j in zip(w11,w22)]
        err = sum(xor)-sum(xor_xor)-corr
        return corr,err


