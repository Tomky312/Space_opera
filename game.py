import pyglet

class Game:
    def __init__(self):
        self.camera = None
        self.fields = []
        self.current_field = None
        self.menus = []

    def update(self, TICK):
        self.camera.update(TICK)

        for field in self.fields:
            field.update(TICK)
