import pyglet

class OverviewMenu:
    def __init__(self, window, image, game):
        # chain setup
        self.game = game
        self.game.menus.append(self)
        # ---
        self.window = window
        self.sprite = pyglet.sprite.Sprite(image)
        self.sprite.x =  window.width
        self.sprite.y = window.height

    def update(self, TICK):
        pass

