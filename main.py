from __future__ import annotations

import pyglet
from pyglet.gl import glClearColor

import resources
import ship
import camera
import field
from game import Game

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

# tick timer for delayed actions
TICK = 0
tick_max = 60

### -----------------------------------------------
game = Game()
camera = camera.Camera(game)
field01 = field.Field(game)
game.current_field = field01

ship01 = ship.Ship(field01, [10, 10], resources.image_ship)
ship01.sprite.batch = batch


# Update function (called every frame or interval)
def update(dt):
    global TICK
    TICK += 1
    if TICK > tick_max:
        TICK = 0

    game.update(TICK)

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
