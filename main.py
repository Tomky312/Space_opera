from __future__ import annotations

import pyglet
from pyglet.gl import glClearColor
from pyglet.window import key
from pyglet.window import mouse

import resources
import ship
import camera
import field
from game import Game
import asteroid

# Create a window
window = pyglet.window.Window(resizable= True, width=2000, height=1000, caption="Basic Pyglet Game Loop")
keys = key.KeyStateHandler()
mouse_state = {"left": False, "right": False, "middle": False}
mouse_pos = {"x": 0, "y": 0}

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

ship01 = ship.Ship(field01, [0, 0], resources.image_battleship)
ship01.sprite.batch = batch

ship02 = ship.Ship(field01, [5000, 5000], resources.image_frigate)
ship02.max_speed *= 10
ship02.acceleration *= 10
ship02.sprite.batch = batch

# camera.tracking_obj = ship01


### --------- MENUS ------------


# Update function (called every frame or interval)
def update(dt):
    global TICK
    TICK += 1
    if TICK > tick_max:
        TICK = 0

    mouse_pos["x"] = window._mouse_x
    mouse_pos["y"] = window._mouse_y
    game.update(TICK, batch, mouse_state, mouse_pos["x"], mouse_pos["y"])



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
    if button == mouse.LEFT:
        mouse_state["left"] = True

        game.selected = []

        for ship in game.current_field.ships:
            ship.select(x, y, game.camera)
    elif button == mouse.RIGHT:
        mouse_state["right"] = True

        for ship in game.selected:
            ship.start_waypoint(x, y)


@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        mouse_state["left"] = False
    elif button == mouse.RIGHT:
        mouse_state["right"] = False

        for ship in game.selected:
            ship.set_waypoint(x, y)

@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    game.camera.set_zoom(scroll_y, x, y)

# Schedule the update function to be called regularly
pyglet.clock.schedule_interval(update, 1/60.0)  # 60 FPS

pyglet.app.run()
