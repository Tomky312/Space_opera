import pyglet

class Asteroid:
    def __init__(self, field, world_pos, image):
        # chain setup
        self.field = field
        self.field.asteroids.append(self)
        # ---
        self.sprite = pyglet.sprite.Sprite(image)

        self.world_pos = world_pos
        self.image = image

    def update(self, TICK):
        pass