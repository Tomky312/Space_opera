import pyglet
import my_math

class Ship:
    def __init__(self, world_pos, image, debug_sprite):
        self.world_pos = world_pos
        self.sprite = pyglet.sprite.Sprite(image)

        self.max_speed = 20
        self.acceleration = 0.1
        self.velocity = [0, 0]

        self.world_dest = [world_pos[0], world_pos[1]]

        self.maneuver_type = "none"
        self.maneuver_target = [0, 0]
        self.maneuver_dist = 10

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
        # Don't rotate if already at destination
        if self.world_dest[0] == self.world_pos[0] and self.world_dest[1] == self.world_pos[1]:
            return

        # reset rotation to keep -360 < r < 360
        if self.sprite.rotation > 360:
            self.sprite.rotation -= 360
        if self.sprite.rotation < -360:
            self.sprite.rotation += 360

        # Calculate desired rotation based on velocity direction
        desired_angle = -my_math.angle_from_vector(self.velocity)
        angle_difference = desired_angle - self.sprite.rotation

        # Snap to target if close enough
        if abs(angle_difference) <= 0.1:
            self.sprite.rotation = desired_angle
            return

        # Normalize angle difference to shortest path (-180 to 180)
        if angle_difference > 180:
            angle_difference -= 360
        elif angle_difference < -180:
            angle_difference += 360

        # Apply rotation with acceleration-based speed
        max_rotation_speed = self.acceleration * 10
        rotation_speed = min(self.acceleration * abs(angle_difference), max_rotation_speed)

        if angle_difference > 0:
            self.sprite.rotation += rotation_speed
        elif angle_difference < 0:
            self.sprite.rotation -= rotation_speed

    def maneuver(self, tick):
        if tick == 0:
            pass
        else:
            return
        if self.maneuver_type == "none":
            return

        if self.maneuver_type == "orbit":
            orbit_radius = self.maneuver_dist

            # Get direction from target to current position
            dir_to_self = my_math.direction(self.maneuver_target, self.world_pos)

            # Start with a point at orbit distance from target
            orbit_point = my_math.scale(dir_to_self, orbit_radius)
            orbit_point[0] += self.maneuver_target[0]
            orbit_point[1] += self.maneuver_target[1]

            # Move perpendicular to create orbital offset
            perpendicular = my_math.normal(dir_to_self)
            orbit_point[0] += perpendicular[0] * orbit_radius
            orbit_point[1] += perpendicular[1] * orbit_radius

            # Pull slightly back toward center for spiral effect
            dir_to_center = my_math.direction(orbit_point, self.maneuver_target)
            inward_pull = my_math.scale(dir_to_center, orbit_radius / 3)
            orbit_point[0] += inward_pull[0]
            orbit_point[1] += inward_pull[1]

            # Set as destination
            self.world_dest[0] = orbit_point[0]
            self.world_dest[1] = orbit_point[1]



        elif self.maneuver_type[0] == "keep_at_range":
            desired_range = self.maneuver_dist

            # Get direction from target to current position
            dir_to_self = my_math.direction(self.maneuver_target, self.world_pos)

            # Calculate position at desired range from target
            range_position = my_math.scale(dir_to_self, desired_range)
            range_position[0] += self.maneuver_target[0]
            range_position[1] += self.maneuver_target[1]

            # Set as destination
            self.world_dest[0] = range_position[0]
            self.world_dest[1] = range_position[1]





