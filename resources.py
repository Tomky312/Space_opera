import pyglet

def load_centered_image(image_path):
    image = pyglet.image.load(image_path)
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

    return image

image_ship = load_centered_image("ship.png")
image_icon = load_centered_image("green_icon.png")
sprite_icon = pyglet.sprite.Sprite(image_icon)