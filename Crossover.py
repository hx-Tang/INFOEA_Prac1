import random


def uni_x(p):
    end = len(p[0]) - 1
    x = random.randint(0, end)
    p1 = p[0]
    p2 = p[1]
    c1 = p1[0:x]
    c1.extend(p2[x:len(p[0])])
    c2 = p2[0:x]
    c2.extend(p1[x:len(p[0])])

    return c1, c2


def two_x(p):
    end = len(p[0]) - 1
    x = random.randint(0, end)
    y = random.randint(0, end - x) + x
    p1 = p[0]
    p2 = p[1]
    c1 = p1[0:x]
    c1.extend(p2[x:y])
    c1.extend(p1[y:end + 1])
    c2 = p2[0:x]
    c2.extend(p1[x:y])
    c2.extend(p2[y:end + 1])
    return c1, c2


if __name__ == "__main__":
    p = [[1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 1],
         [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 1, 0]]
    random.seed(123)
    print(two_x(p))
