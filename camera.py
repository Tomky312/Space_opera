import pyglet

class Camera:
    def __init__(self, game, window):
        self.game = game
        self.game.camera = self
        self.window = window

        self.center = [window.width // 2, window.height // 2]

        self.speed = 5

        # --- zoom ---
        self.desired_zoom_level = 0.1
        self.current_zoom_level = 0.1
        self.min_zoom = 0.0025
        self.max_zoom = 0.25

        # --- position ---
        self.desired_pos = [0.0, 0.0]
        self.current_pos = [0.0, 0.0]

        self.tracking_obj = None

    def update(self, TICK, batch):
        self.adjust_zoom()
        self.adjust_position()
        self.track()
        self.draw_objects(batch)
        self.set_move()

    def set_move(self):
        mouse_x, mouse_y = self.window._mouse_x, self.window._mouse_y
        speed = self.speed / self.current_zoom_level
        edge_threshold = 40

        if mouse_x < edge_threshold:
            self.desired_pos[0] += speed
        elif mouse_x > self.window.width - edge_threshold:
            self.desired_pos[0] -= speed

        if mouse_y < edge_threshold:
            self.desired_pos[1] += speed
        elif mouse_y > self.window.height - edge_threshold:
            self.desired_pos[1] -= speed

    def set_zoom(self, scroll_y, x, y):
        zoom_speed = 0.1 * self.desired_zoom_level
        old_zoom = self.desired_zoom_level
        new_zoom = old_zoom + scroll_y * zoom_speed
        new_zoom = max(self.min_zoom, min(self.max_zoom, new_zoom))

        if new_zoom == old_zoom:
            return

        # World position under mouse BEFORE zoom
        world_x_before = (x - self.center[0]) / old_zoom - self.desired_pos[0]
        world_y_before = (y - self.center[1]) / old_zoom - self.desired_pos[1]

        # Recalculate pos so that world_x_before stays fixed under the cursor
        self.desired_pos[0] = (x - self.center[0]) / new_zoom - world_x_before
        self.desired_pos[1] = (y - self.center[1]) / new_zoom - world_y_before

        self.desired_zoom_level = new_zoom

    def adjust_zoom(self):
        smoothing = 0.1
        if self.current_zoom_level != self.desired_zoom_level:
            self.current_zoom_level += (self.desired_zoom_level - self.current_zoom_level) * smoothing
        else:
            self.current_zoom_level = self.desired_zoom_level

    def adjust_position(self):
        smoothing = 0.1
        dx = self.desired_pos[0] - self.current_pos[0]
        dy = self.desired_pos[1] - self.current_pos[1]

        if abs(dx) > 0.001 or abs(dy) > 0.001:
            self.current_pos[0] += dx * smoothing
            self.current_pos[1] += dy * smoothing
        else:
            self.current_pos[0] = self.desired_pos[0]
            self.current_pos[1] = self.desired_pos[1]

    def world_to_screen(self, pos: list[float]):
        screen_x =  (pos[0] + self.current_pos[0]) * self.current_zoom_level + self.center[0]
        screen_y = (pos[1] + self.current_pos[1]) * self.current_zoom_level + self.center[1]
        return [screen_x, screen_y]

    def screen_to_world(self, screen_pos: list[float]) -> list[float]:
        world_x = (screen_pos[0] - self.center[0]) / self.current_zoom_level - self.current_pos[0]
        world_y = (screen_pos[1] - self.center[1]) / self.current_zoom_level - self.current_pos[1]
        return [world_x, world_y]

    def draw_objects(self, batch):
        for station in self.game.current_field.stations:
            screen_pos = self.world_to_screen(station.world_pos)
            station.sprite.x = screen_pos[0]
            station.sprite.y = screen_pos[1]
        for ship in self.game.current_field.ships:
            screen_pos = self.world_to_screen(ship.world_pos)
            ship.sprite.x = screen_pos[0]
            ship.sprite.y = screen_pos[1]
            ship.selection_circle_sprite.x = screen_pos[0]
            ship.selection_circle_sprite.y = screen_pos[1]
            if ship.selected:
                ship.selection_circle_sprite.batch = batch
                line_start = self.world_to_screen(ship.world_pos)
                line_end = self.world_to_screen(ship.world_dest)
                ship.line = pyglet.shapes.Line(line_start[0], line_start[1], line_end[0], line_end[1], color=(76, 255, 0))
                ship.line.batch = batch
            else:
                ship.selection_circle_sprite.batch = None
                ship.line.batch = None

        for asteroid in self.game.current_field.asteroids:
            screen_pos = self.world_to_screen(asteroid.world_pos)
            asteroid.sprite.x = screen_pos[0]
            asteroid.sprite.y = screen_pos[1]

    def track(self):
        if self.tracking_obj:
            self.pos = [-self.tracking_obj.world_pos[0], -self.tracking_obj.world_pos[1]]
