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


def average_and_std(P):
    fit_all_1=[]
    fit_all_0=[]
    num_0=0
    num_1=0
    for instance in P:
        fi =instance[1]
        body =instance[0]
        if body[0] == 1:
            num_1 =num_1 + 1
            fit_all_1.append(fi)
        else:
            num_0 = num_0 + 1
            fit_all_0.append(fi)
    if len(fit_all_1) == 0:
        aver_1, std_1 =0,0
    else:
        aver_1 = sum(fit_all_1)/len(fit_all_1)
        std_1 = std(fit_all_1)
    if len(fit_all_0)==0:
        aver_0, std_0=0,0
    else:
        aver_0 =sum(fit_all_0)/len(fit_all_0)
        std_0 = std(fit_all_0)
    return num_1, num_0, aver_1,std_1,aver_0,std_0

def average_fi(P):
    fi=[]
    for instance in P:
        fi.append(instance[1])
    return sum(fi)/len(fi)

