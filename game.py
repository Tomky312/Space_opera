import pyglet

class Game:
    def __init__(self):
        self.camera = None
        self.fields = []
        self.current_field = None
        self.menus = []

        self.selected = []

    def update(self, TICK, batch, mouse_state, x, y):
        self.camera.update(TICK, batch)

        for field in self.fields:
            field.update(TICK)

        if mouse_state["right"]:
            for ship in self.selected:
                ship.update_waypoint(x, y)
