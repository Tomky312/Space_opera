from __future__ import annotations

import pyglet
from pyglet.gl import glClearColor

import resources
import resources as res
import ship
import camera

# Create a window
WIDTH = 2000
HEIGHT = 1100
window = pyglet.window.Window(width=WIDTH, height=HEIGHT, caption="Basic Pyglet Game Loop")

batch = pyglet.graphics.Batch()

# background sprite
background_sprite = pyglet.sprite.Sprite(resources.image_background)
background_sprite.batch = batch

#   set colour after clear call
glClearColor(50/255.0, 70/255.0, 150/255.0, 1.0)
camera = camera.Camera()

# tick timer for delayed actions
TICK = 0
tick_max = 60

ship01 = ship.Ship([0, 0], resources.image_ship, resources.sprite_icon)
ship01.sprite.batch = batch
camera.objects.append(ship01)
camera.tracking_obj = ship01

ship01.maneuver_type = "orbit"
ship01.maneuver_target = [100, 100]
ship01.maneuver_dist = 500

# Update function (called every frame or interval)
def update(dt):
    global TICK
    TICK += 1
    if TICK > tick_max:
        TICK = 0

    ship01.update(TICK)

    camera.update()

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
    pass

@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    pass


# Schedule the update function to be called regularly
pyglet.clock.schedule_interval(update, 1/60.0)  # 60 FPS

pyglet.app.run()
