def fact(n):
    for el in range(1, n + 1):
        for elem in range(1, el):
            el *= elem
        yield el

factorials = [el for el in fact(4)]
print(factorials)

