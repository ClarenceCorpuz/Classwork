import arcade


WIDTH = 640
HEIGHT = 480

x1 = 100
y1 = 250
x2 = 200
y2 = 450
x3 = 300
y3 = 250

a = 150
b = 150
c = 100
d = 150

def update(delta_time):
    pass

def on_draw():
    arcade.start_render()
    arcade.draw_xywh_rectangle_filled(a, b, c, d, arcade.color.DARK_BROWN)
    arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, arcade.color.DARK_GREEN)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()