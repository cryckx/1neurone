from random import randint


def random_assignment(vehicles, rides):
    percar = rides/vehicles
    print 'percar :', percar
    toassign = [i for i in range(0, rides+1)]
    triplet = []
    trajets = []
    lastcut = -1

    print('toto')
    while len(toassign) > 0:
        print('tata')
        for i in range(percar):
            if len(toassign) == 0:
                lastcut = i
                break
            rd = randint(0, len(toassign) - 1)
            triplet.append(toassign[rd])
            toassign = toassign[0:rd] + toassign[rd+1:]
        trajets.append([len(triplet)]+ triplet)
        triplet = []

    if lastcut:
        trajets[-1] = trajets[-1][0:trajets[-1][0]]

    return trajets
