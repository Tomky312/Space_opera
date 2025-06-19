
class Camera:
    def __init__(self):

        self.center = [800, 450]
        self.pos = [0, 0]

        self.mov_speed = 1

    def set_move(self):
        pass

    def world_to_screen(self, pos: list[float]):
        screen_pos = [pos[0] + self.center[0] + self.pos[0], pos[1] + self.center[1] + self.pos[1]]
        return screen_pos