
class Camera:
    def __init__(self):
        self.objects = []

        self.center = [1000, 550]
        self.pos = [0, 0]

        self.mov_speed = 1

        self.tracking_obj = None

    def update(self):
        self.track()
        self.draw_objects()

    def set_move(self):
        pass

    def world_to_screen(self, pos: list[float]):
        screen_pos = [pos[0] + self.center[0] + self.pos[0], pos[1] + self.center[1] + self.pos[1]]
        return screen_pos

    def draw_objects(self):
        for object in self.objects:
            screen_pos = self.world_to_screen(object.world_pos)
            object.sprite.x = screen_pos[0]
            object.sprite.y = screen_pos[1]

    def track(self):
        if self.tracking_obj:
            self.pos = [-self.tracking_obj.world_pos[0], -self.tracking_obj.world_pos[1]]