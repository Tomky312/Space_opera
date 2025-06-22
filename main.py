from __future__ import annotations

import pyglet
from pyglet.gl import glClearColor

import resources
import resources as res
import ship
import camera

# Create a window
window = pyglet.window.Window(width=2000, height=1100, caption="Basic Pyglet Game Loop")

#   set colour after clear call
glClearColor(100/255.0, 100/255.0, 230/255.0, 1.0)
batch = pyglet.graphics.Batch()
camera = camera.Camera()

# tick timer for delayed actions
tick = 0
tick_max = 60

ship01 = ship.Ship([0, 0], resources.image_ship, resources.sprite_icon)
ship01.sprite.batch = batch
camera.objects.append(ship01)

ship02 = ship.Ship([-100, -100], resources.image_ship, resources.sprite_icon)
ship02.sprite.batch = batch
ship02.debug_sprite.batch = batch
camera.objects.append(ship02)

ship02.maneuver_type = ["orbit", 5000]

# Update function (called every frame or interval)
def update(dt):
    global tick
    tick += 1
    if tick > tick_max:
        tick = 0

    ship02.maneuver_target = [ship01.world_pos[0], ship01.world_pos[1]]

    ship01.update(tick)
    ship02.update(tick)

    point = camera.world_to_screen(ship02.world_dest)
    ship02.debug_sprite.x = point[0]
    ship02.debug_sprite.y = point[1]

    camera.draw_objects()

@window.event
def on_draw():
    window.clear()
    batch.draw()
    # Drawing code goes here

@window.event
def on_key_press(symbol, modifiers):
    pass  # Handle key press events here

@window.event
def on_key_release(symbol, modifiers):
    pass  # Handle key release events here

@window.event
def on_mouse_press(x, y, button, modifiers):
    ship01.world_dest = [x - camera.center[0], y - camera.center[1]]

@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    pass


# Schedule the update function to be called regularly
pyglet.clock.schedule_interval(update, 1/60.0)  # 60 FPS

pyglet.app.run()
