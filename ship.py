import pyglet

class Ship:
    def __init__(self, world_pos, sprite):
        self.world_pos = world_pos
        self.sprite = sprite

    def update(self, camera):
        screen_pos = camera.world_to_screen(self.world_pos)
        self.sprite.x = screen_pos[0]
        self.sprite.y = screen_pos[1]
