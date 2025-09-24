import pyglet
import resources

class Asteroid:
    def __init__(self, asteroid_cluster, world_pos, mass):
        # chain setup
        self.asteroid_cluster = asteroid_cluster
        self.asteroid_cluster.asteroids.append(self)
        # ---
        self.world_pos = world_pos
        self.mass = mass

        if self.mass >= 3000:
            self.sprite = pyglet.sprite.Sprite(resources.image_asteroid_medium)
        if self.mass >= 8000:
            self.sprite = pyglet.sprite.Sprite(resources.image_asteroid_large)
        else:
            self.sprite = pyglet.sprite.Sprite(resources.image_asteroid_small)


    def update(self, TICK):
        pass