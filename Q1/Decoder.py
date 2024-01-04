def add(a, b):
    if a in c1:
        if b in c1:
            return (c1.index(a) + c1.index(b) + 2) % 26
        else:
            return (c1.index(a) + c2.index(b) + 2) % 26
    else:
        if b in c1:
            return (c2.index(a) + c1.index(b) + 2) % 26
        else:
            return (c2.index(a) + c2.index(b) + 2) % 26


def diff(a, b):
    if a in c1:
        if b in c1:
            return (c1.index(a) - c1.index(b)) % 26
        else:
            return (c1.index(a) - c2.index(b)) % 26
    else:
        if b in c1:
            return (c2.index(a) - c1.index(b)) % 26
        else:
            return (c2.index(a) - c2.index(b)) % 26


def evaluator(tp, shift):
    if tp in c1:
        return c1[(shift - 1) % 26]
    else:
        return c2[(shift - 1) % 26]


flag = "cRyPtOgRaPhYisAmAzInG"
q = "c" #Flag[0]

c1 = "abcdefghijklmnopqrstuvwxyz"
c2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(flag) - 2):
    q += evaluator(flag[i + 1], diff(flag[i + 1], flag[i]))

q+=flag[-1]
print(q)


finder = q[0]

for i in range(len(q) - 2):
    finder += evaluator(q[i + 1], add(q[i + 1], finder[i]))

finder+=q[-1]
print(finder)
