import math

def size(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2)

def difference(pos1, pos2):
    return [pos2[0] - pos1[0], pos2[1] - pos1[1]]

def distance(pos1, pos2):
    diff = difference(pos1, pos2)
    return size(diff)

def direction(pos1, pos2):
    dif = difference(pos1, pos2)
    dist = distance(pos1, pos2)
    return [dif[0]/dist, dif[1]/dist]
