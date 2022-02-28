
# def counting_ones(p):
#     pass


# class TrapFunc:
#     def __init__(self, k, d):
#         self.k = k
#         self.d = d

#     def trap_tl(self, p):
#         pass

#     def trap_ntl(self, p):
#         pass


#p = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#b is the fitness

def counting_ones(p):
    return (sum(p))


def trap_tl(p):
    k = 4
    d = 1
    b = 0
    for i in range(len(p)//k):
       if sum(p[i*k:i*k+k]) == k:
           b=b+k
       else:
           x = k-d - (k-d)/(k-1)*sum(p[i*k:i*k+k])
           b = b+x
    return b



def trap_ntl(p):
    k = 4
    d = 2.5
    b = 0
    for i in range(len(p)//k):
       if sum(p[i*k:i*k+k]) == k:
           b=b+k
       else:
           x = k-d - (k-d)/(k-1)*sum(p[i*k:i*k+k])
           b = b+x
    return b


def nontight_trap_tl(p):
    k = 4
    d = 1
    b = 0
    for i in range(len(p)//k):
        subfunction = []
        for j in range(k):
            subfunction.append(p[j*10+i])
        if sum(subfunction) == k:
            b =b+k
        else:
            x = k - d - (k - d) / (k - 1) * sum(subfunction)
            b = b + x
    return b

def nontight_trap_ntl(p):
    k = 4
    d = 2.5
    b = 0
    for i in range(len(p)//k):
        subfunction = []
        for j in range(k):
            subfunction.append(p[j*10+i])
        if sum(subfunction) == k:
            b =b+k
        else:
            x = k - d - (k - d) / (k - 1) * sum(subfunction)
            b = b + x
    return b

print(nontight_trap_ntl(p))
