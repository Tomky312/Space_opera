import pyglet

class Camera:
    def __init__(self, game, window):
        # chain setup
        self.game = game
        self.game.camera = self
        # ---
        self.window = window

        self.center = [window.width // 2, window.height // 2]
        self.pos = [0, 0]

        self.mov_speed = 5

        self.tracking_obj = None

    def update(self, TICK):
        self.track()
        self.draw_objects()
        self.set_move()

    def set_move(self):
        # Get mouse position
        mouse_x, mouse_y = self.window._mouse_x, self.window._mouse_y
        speed = self.mov_speed

        # Define edge threshold (px from edge where camera starts moving)
        edge_threshold = 20

        # Horizontal movement
        if mouse_x < edge_threshold:
            self.pos[0] += speed
        elif mouse_x > self.window.width - edge_threshold:
            self.pos[0] -= speed

        # Vertical movement
        if mouse_y < edge_threshold:
            self.pos[1] += speed
        elif mouse_y > self.window.height - edge_threshold:
            self.pos[1] -= speed

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