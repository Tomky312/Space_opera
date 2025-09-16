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

        self.speed = 5
        self.zoom_level = 1.0  # <-- new zoom variable
        self.min_zoom = 0.05  # prevent zooming out too much
        self.max_zoom = 1.0  # prevent zooming in too much

        self.tracking_obj = None

    def update(self, TICK):
        self.track()
        self.draw_objects()
        self.set_move()

    def set_move(self):
        # Get mouse position
        mouse_x, mouse_y = self.window._mouse_x, self.window._mouse_y
        speed = self.speed / self.zoom_level

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

    def set_zoom(self, scroll_y, x, y):
        # scroll_y is +1 (up) or -1 (down)
        zoom_speed = 0.1 * self.zoom_level
        old_zoom = self.zoom_level
        new_zoom = old_zoom + scroll_y * zoom_speed
        new_zoom = max(self.min_zoom, min(self.max_zoom, new_zoom))

        if new_zoom == old_zoom:
            return

        world_x_before = (x - self.center[0]) / old_zoom - self.pos[0]
        world_y_before = (y - self.center[1]) / old_zoom - self.pos[1]

        # Recalculate pos so that world_x_before stays fixed under the cursor
        self.pos[0] = (x - self.center[0]) / new_zoom - world_x_before
        self.pos[1] = (y - self.center[1]) / new_zoom - world_y_before

        self.zoom_level = new_zoom

    def world_to_screen(self, pos: list[float]):
        # Apply zoom around the camera center
        screen_pos = [
            (pos[0] + self.pos[0]) * self.zoom_level + self.center[0],
            (pos[1] + self.pos[1]) * self.zoom_level + self.center[1]
        ]
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