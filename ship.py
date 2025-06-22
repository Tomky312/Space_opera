import pyglet
import my_math

class Ship:
    def __init__(self, world_pos, image, debug_sprite):
        self.world_pos = world_pos
        self.sprite = pyglet.sprite.Sprite(image)
        self.debug_sprite = debug_sprite

        self.max_speed = 20
        self.acceleration = 0.1
        self.velocity = [0, 0]

        self.world_dest = [world_pos[0], world_pos[1]]

        self.maneuver_type = ["none", 0]
        self.maneuver_target = [0, 0]

    def update(self, tick):
        self.move()
        self.rotate()
        self.maneuver(tick)

    def move(self):

        self.velocity[0] *= 1 - self.acceleration / self.max_speed
        self.velocity[1] *= 1 - self.acceleration / self.max_speed

        self.world_pos[0] += self.velocity[0]
        self.world_pos[1] += self.velocity[1]

        if self.world_dest[0] == self.world_pos[0] and self.world_dest[1] == self.world_pos[1]:
            return

        if my_math.distance(self.world_pos, self.world_dest) < 10:
            self.world_dest[0] = self.world_pos[0]
            self.world_dest[1] = self.world_pos[1]

        breaking_time = (my_math.size(self.velocity) / self.acceleration) * 1.05 # coefficient to slightly extend breakpoint
        brake_point = [0, 0]
        brake_point[0] = self.world_pos[0] + self.velocity[0] * breaking_time
        brake_point[1] = self.world_pos[1] + self.velocity[1] * breaking_time

        if my_math.distance(self.world_pos, self.world_dest) < 1:
            self.world_dest[0] = self.world_pos[0]
            self.world_dest[1] = self.world_pos[1]
            return
        elif my_math.size(self.velocity) > self.max_speed:
            return
        else:
            dir = my_math.direction(brake_point, self.world_dest)
            self.velocity[0] += dir[0] * self.acceleration
            self.velocity[1] += dir[1] * self.acceleration

    def rotate(self):
        if self.world_dest[0] == self.world_pos[0] and self.world_dest[1] == self.world_pos[1]:
            return

        if self.sprite.rotation > 360:
            self.sprite.rotation -= 360
        if self.sprite.rotation < -360:
            self.sprite.rotation += 360

        desired_angle = - my_math.angle_from_vector(self.velocity)
        dif_angle = desired_angle - self.sprite.rotation

        if abs(dif_angle) <= 0.1:
            self.sprite.rotation = desired_angle
            return

        if dif_angle > 180:
            dif_angle -= 360
        elif dif_angle < -180:
            dif_angle += 360

        if dif_angle > 0:
            self.sprite.rotation += min(self.acceleration * abs(dif_angle), self.acceleration * 10)
        elif dif_angle < 0:
            self.sprite.rotation -= min(self.acceleration * abs(dif_angle), self.acceleration * 10)

    def maneuver(self, tick):
        if tick == 0:
            pass
        else:
            return
        if self.maneuver_type[0] == "none":
            return

        if self.maneuver_type[0] == "orbit":
            dir_to_self = my_math.direction(self.maneuver_target, self.world_pos)
            point_at_distance = my_math.scale(dir_to_self, self.maneuver_type[1])
            point_at_distance[0] += self.maneuver_target[0]
            point_at_distance[1] += self.maneuver_target[1]
            normal = my_math.normal(dir_to_self)

            point_at_distance[0] = point_at_distance[0] + normal[0] * self.maneuver_type[1]
            point_at_distance[1] = point_at_distance[1] + normal[1] * self.maneuver_type[1]

            dir_to_center = my_math.direction(point_at_distance, self.maneuver_target)

            point_at_distance[0] += dir_to_center[0] * self.maneuver_type[1]/3
            point_at_distance[1] += dir_to_center[1] * self.maneuver_type[1]/3

            self.world_dest[0] = point_at_distance[0]
            self.world_dest[1] = point_at_distance[1]


        elif self.maneuver_type[0] == "keep_at_range":
            dir_to_self = my_math.direction(self.maneuver_target, self.world_pos)
            point_at_distance = my_math.scale(dir_to_self, self.maneuver_type[1])
            point_at_distance[0] += self.maneuver_target[0]
            point_at_distance[1] += self.maneuver_target[1]

            self.world_dest[0] = point_at_distance[0]
            self.world_dest[1] = point_at_distance[1]





