import math

import math


def size(vector):
    """
    Calculate the magnitude (length) of a 2D vector.

    Args:
        vector: A 2D vector as [x, y] or (x, y)

    Returns:
        float: The magnitude of the vector using Euclidean distance formula

    Example:
        size([3, 4]) -> 5.0
        size([0, 0]) -> 0.0
    """
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)


def difference(pos1, pos2):
    """
    Calculate the vector difference from pos1 to pos2.

    Args:
        pos1: Starting position as [x, y] or (x, y)
        pos2: Ending position as [x, y] or (x, y)

    Returns:
        list: Vector from pos1 to pos2 as [dx, dy]

    Example:
        difference([1, 2], [4, 6]) -> [3, 4]
    """
    return [pos2[0] - pos1[0], pos2[1] - pos1[1]]


def distance(pos1, pos2):
    """
    Calculate the Euclidean distance between two points.

    Args:
        pos1: First point as [x, y] or (x, y)
        pos2: Second point as [x, y] or (x, y)

    Returns:
        float: Distance between the two points

    Example:
        distance([0, 0], [3, 4]) -> 5.0
    """
    diff = difference(pos1, pos2)
    return size(diff)


def direction(pos1, pos2):
    """
    Calculate the unit vector (normalized direction) from pos1 to pos2.

    Args:
        pos1: Starting position as [x, y] or (x, y)
        pos2: Ending position as [x, y] or (x, y)

    Returns:
        list: Unit vector pointing from pos1 to pos2 as [x, y]
               Returns [0, 0] if positions are identical

    Example:
        direction([0, 0], [3, 4]) -> [0.6, 0.8]
        direction([1, 1], [1, 1]) -> [0, 0]
    """
    dif = difference(pos1, pos2)
    dist = distance(pos1, pos2)
    if dist == 0:
        return [0, 0]
    return [dif[0] / dist, dif[1] / dist]


def normal(vector):
    """
    Calculate the perpendicular (normal) vector by rotating 90 degrees counterclockwise.

    Args:
        vector: Input vector as [x, y] or (x, y)

    Returns:
        list: Perpendicular vector as [x, y]

    Example:
        normal([1, 0]) -> [0, 1]
        normal([0, 1]) -> [-1, 0]
        normal([3, 4]) -> [-4, 3]
    """
    return [-vector[1], vector[0]]


def angle_between_points(pos1, pos2):
    """
    Calculate the angle in degrees from pos1 to pos2.

    Args:
        pos1: Starting position as [x, y] or (x, y)
        pos2: Ending position as [x, y] or (x, y)

    Returns:
        float: Angle in degrees (-180 to 180)
               0° points right (+X), 90° points up (+Y)

    Example:
        angle_between_points([0, 0], [1, 0]) -> 0.0
        angle_between_points([0, 0], [0, 1]) -> 90.0
        angle_between_points([0, 0], [-1, 0]) -> 180.0
    """
    dif = difference(pos1, pos2)
    angle_rad = math.atan2(dif[1], dif[0])
    angle_deg = math.degrees(angle_rad)
    return angle_deg


def angle_from_vector(vector):
    """
    Calculate the angle in degrees of a vector from the positive X-axis.

    Args:
        vector: Input vector as [x, y] or (x, y)

    Returns:
        float: Angle in degrees (-180 to 180)
               0° points right (+X), 90° points up (+Y)

    Example:
        angle_from_vector([1, 0]) -> 0.0
        angle_from_vector([0, 1]) -> 90.0
        angle_from_vector([-1, 0]) -> 180.0
        angle_from_vector([1, 1]) -> 45.0
    """
    angle_rad = math.atan2(vector[1], vector[0])
    angle_deg = math.degrees(angle_rad)
    return angle_deg


def scale(vector, scale):
    """
    Scale a vector by multiplying each component by a scalar value.

    Args:
        vector: Input vector as [x, y] or (x, y)
        scale: Scalar multiplier (float or int)

    Returns:
        list: Scaled vector as [x, y]

    Example:
        scale([3, 4], 2) -> [6, 8]
        scale([1, -2], 0.5) -> [0.5, -1.0]
        scale([5, 3], 0) -> [0, 0]
    """
    return [vector[0] * scale, vector[1] * scale]


def rotate_around_point(pos, center_pos, angle):
    """
    Rotate a point around another point by a given angle.

    Args:
        pos: Current position (x, y) - can be tuple or list
        center_pos: Center point to rotate around (x, y)
        angle: Rotation angle in radians

    Returns:
        new_pos: New position after rotation (x, y) as tuple
    """
    # Translate point to origin
    x = pos[0] - center_pos[0]
    y = pos[1] - center_pos[1]

    # Apply rotation
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)

    new_x = x * cos_angle - y * sin_angle
    new_y = x * sin_angle + y * cos_angle

    # Translate back
    new_x += center_pos[0]
    new_y += center_pos[1]

    return [new_x, new_y]