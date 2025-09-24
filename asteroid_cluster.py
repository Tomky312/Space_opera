import pyglet
import math
import random
import asteroid as ast

class AsteroidCluster:
    def __init__(self, field, count, diameter):
        # chain setup
        self.field = field
        self.field.asteroid_clusters.append(self)

        self.positions = []
        self.masses = []

        self.asteroids = []

        self.generate_positions(count, diameter)
        self.generate_masses(count)

        for i in range(count):
            asteroid = ast.Asteroid(self, self.positions[i], self.masses[i])
            self.asteroids.append(asteroid)

    def update(self, TICK):
        for asteroid in self.asteroids:
            asteroid.update(TICK)

    def generate_positions(self, count, diameter):
        """Return list of (x, y) positions inside given diameter."""
        positions = []
        radius = diameter / 2
        for _ in range(count):
            # random polar coordinates inside circle
            r = radius * math.sqrt(random.random())
            theta = random.uniform(0, 2*math.pi)
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            positions.append((x, y))
        self.positions = positions

    def generate_masses(self, count, base=100, decay=0.85, floor=25):
        """Return descending masses. First is largest, then taper down."""
        masses = []
        value = random.randint(base-10, base+10)
        for i in range(count):
            masses.append(int(round(value)))
            # drop steeply at first, then level off
            if i < 1:
                value *= 0.5  # first → second big drop
            else:
                value = max(value * decay, floor)
        self.masses = masses
        for i in range(count):
            self.masses[i] = self.masses[i] * self.masses[i]
            print(self.masses[i])
