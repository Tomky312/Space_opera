import pyglet
import random

class SpaceGunk:
    def __init__(self,world_pos, image):
        self.world_pos = world_pos
        self.sprite = pyglet.sprite.Sprite(image)
