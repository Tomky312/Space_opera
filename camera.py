
class Camera:
    def __init__(self, game):
        # chain setup
        self.game = game
        self.game.camera = self
        # ---

        self.center = [800, 400]
        self.pos = [0, 0]

        self.mov_speed = 1

        self.tracking_obj = None

    def update(self, TICK):
        self.track()
        self.draw_objects()

    def set_move(self):
        pass

    def world_to_screen(self, pos: list[float]):
        screen_pos = [pos[0] + self.center[0] + self.pos[0], pos[1] + self.center[1] + self.pos[1]]
        return screen_pos

    def draw_objects(self):
        for station in self.game.current_field.stations:
            screen_pos = self.world_to_screen(station.world_pos)
            station.sprite.x = screen_pos[0]
            station.sprite.y = screen_pos[1]
        for ship in self.game.current_field.ships:
            screen_pos = self.world_to_screen(ship.world_pos)
            ship.sprite.x = screen_pos[0]
            ship.sprite.y = screen_pos[1]
        for asteroid in self.game.current_field.asteroids:
            screen_pos = self.world_to_screen(asteroid.world_pos)
            asteroid.sprite.x = screen_pos[0]
            asteroid.sprite.y = screen_pos[1]

    def track(self):
        if self.tracking_obj:
            self.pos = [-self.tracking_obj.world_pos[0], -self.tracking_obj.world_pos[1]]