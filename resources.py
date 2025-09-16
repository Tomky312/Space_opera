import pyglet


def load_centered_image(image_path):
    """
    Load an image and set its anchor point to the center.

    This function loads an image file and sets the anchor point to the center
    of the image, which is useful for rotating sprites around their center
    or positioning them by their center point rather than top-left corner.

    Args:
        image_path (str): Path to the image file to load

    Returns:
        pyglet.image.AbstractImage: Loaded image with anchor set to center

    Example:
        ship_image = load_centered_image("assets/ship.png")
        # Now when creating a sprite, it will rotate around its center
        ship_sprite = pyglet.sprite.Sprite(ship_image, x=100, y=100)
    """
    image = pyglet.image.load(image_path)
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

    return image

image_ship = load_centered_image("assets/ships/test.png")

image_asteroid = load_centered_image("assets/asteroids/asteroid.png")


image_background = load_centered_image("assets/background/01.jpg")

image_icon = load_centered_image("green_icon.png")
sprite_icon = pyglet.sprite.Sprite(image_icon)