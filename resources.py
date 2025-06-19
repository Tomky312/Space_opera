import pyglet

def load_centered_sprite(image_path):
    image = pyglet.image.load(image_path)
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

    return pyglet.sprite.Sprite(image)

sprite_ship = load_centered_sprite("ship.png")
