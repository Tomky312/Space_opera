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
    if dist == 0:
        return [0, 0]
    return [dif[0]/dist, dif[1]/dist]

def normal(vector):
    return [-vector[1], vector[0]]

def angle_between_points(pos1, pos2):
    dif = difference(pos1, pos2)
    angle_rad = math.atan2(dif[1], dif[0])
    angle_deg = math.degrees(angle_rad)
    return angle_deg

def angle_from_vector(vector):
    angle_rad = math.atan2(vector[1], vector[0])
    angle_deg = math.degrees(angle_rad)
    return angle_deg

def scale(vector, scale):
    return [vector[0] * scale, vector[1] * scale]