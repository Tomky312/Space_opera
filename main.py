from __future__ import annotations

import pyglet
from pyglet.gl import *

import resources
import ship
import camera
import field
from game import Game
import asteroid

# Create a window
window = pyglet.window.Window(resizable = True, width=1600, height=800, caption="Basic Pyglet Game Loop")

batch = pyglet.graphics.Batch()

# background sprite
background_sprite = pyglet.sprite.Sprite(resources.image_background)
background_sprite.batch = batch

#   set colour after clear call
glClearColor(50/255.0, 70/255.0, 150/255.0, 1.0)

# tick timer for delayed actions
TICK = 0
tick_max = 60

### ---------------------ACTIVE--------------------------
game = Game()
camera = camera.Camera(game, window)
field01 = field.Field(game)
game.current_field = field01

ship01 = ship.Ship(field01, [200, 200], resources.image_destroyer)
ship01.sprite.batch = batch

asteroid01 = asteroid.Asteroid(field01, [500, 500], resources.image_asteroid)
asteroid01.sprite.batch = batch

# camera.tracking_obj = ship01

ship01.maneuver_target = asteroid01
ship01.maneuver_dist = 6000
ship01.maneuver_type = "orbit"

### --------- MENUS ------------


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
    for ship in game.current_field.ships:
        ship.select(x, y, game.camera)

@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    game.camera.set_zoom(scroll_y, x, y)


# Schedule the update function to be called regularly
pyglet.clock.schedule_interval(update, 1/60.0)  # 60 FPS

pyglet.app.run()
