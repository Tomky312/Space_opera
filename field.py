import pyglet

class Field:
    def __init__(self, game):
        # chain setup
        self.game = game
        self.game.fields.append(self)
        # ---

        self.stations = []
        self.ships = []
        self.asteroids = []

    def update(self, TICK):
        for station in self.stations:
            station.update(TICK)

        for ship in self.ships:
            ship.update(TICK)

        for asteroid in self.asteroids:
            asteroid.update(TICK)