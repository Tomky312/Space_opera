import pyglet

class GameSprite:
    def __init__(self, image_path, batch, camera):
        self.batch = batch
        self.camera = camera

        self.image = pyglet.image.load(image_path)
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image)

        self.world_pos = [500, 500]
        self.sprite.x = 500
        self.sprite.y = 500
