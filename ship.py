import pyglet
import my_math

class Ship:
    def __init__(self, world_pos, sprite):
        self.world_pos = world_pos
        self.sprite = sprite

        self.max_speed = 10
        self.acceleration = 0.1
        self.velocity = [0, 0]

        self.world_dest = [0, 0]

    def update(self, camera):
        screen_pos = camera.world_to_screen(self.world_pos)
        self.sprite.x = screen_pos[0]
        self.sprite.y = screen_pos[1]

        self.move()

    def move(self):
        self.velocity[0] *= 1 - self.acceleration / self.max_speed
        self.velocity[1] *= 1 - self.acceleration / self.max_speed

        self.world_pos[0] += self.velocity[0]
        self.world_pos[1] += self.velocity[1]
        if self.world_pos == self.world_dest:
            return

        breaking_time = (my_math.size(self.velocity) / self.acceleration) * 1.05 # coefficient to slightly extend breakpoint
        brake_point = [0, 0]
        brake_point[0] = self.world_pos[0] + self.velocity[0] * breaking_time
        brake_point[1] = self.world_pos[1] + self.velocity[1] * breaking_time

        if my_math.distance(self.world_pos, self.world_dest) < 1:
            self.world_dest = self.world_pos
            return
        #elif my_math.size(self.velocity) > self.max_speed:
        #    return
        else:
            dir = my_math.direction(brake_point, self.world_dest)
            self.velocity[0] += dir[0] * self.acceleration
            self.velocity[1] += dir[1] * self.acceleration

