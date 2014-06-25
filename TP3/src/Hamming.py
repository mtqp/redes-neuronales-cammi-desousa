
def distance(aVector, anotherVector):
    if not  len(aVector)==len(anotherVector):
        raise Exception("Cannot calculate hammingDistance with vectors of diferrent sizes: " + str(len(aVector)) + ' - ' + str(len(anotherVector)))

    distance = 0
    for i in range(0, len(aVector)):
        if not aVector[i] == anotherVector[i]:
            distance += 1

    return distance