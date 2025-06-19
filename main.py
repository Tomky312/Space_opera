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

ship01 = ship.Ship([0, 0], resources.sprite_ship)
ship01.sprite.batch = batch

# Update function (called every frame or interval)
def update(dt):
    ship01.update(camera)

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
    pass  # Handle mouse press events here

@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    pass


# Schedule the update function to be called regularly
pyglet.clock.schedule_interval(update, 1/60.0)  # 60 FPS

pyglet.app.run()
