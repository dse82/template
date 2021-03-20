"""
Starting Template

"""
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def draw_background(self):
        """
        This function draws the background. Specifically, the sky and ground.
        """
        # Draw the sky in the top two-thirds
        arcade.draw_lrtb_rectangle_filled(
            0,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            SCREEN_HEIGHT * (1 / 3),
            arcade.color.SKY_BLUE,
        )

        # Draw the ground in the bottom third
        arcade.draw_lrtb_rectangle_filled(
            0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.DARK_SPRING_GREEN
        )

    def draw_bird(self, x, y):
        """
        Draw a bird using a couple arcs.
        """
        arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
        arcade.draw_arc_outline(x + 20, y, 20, 20, arcade.color.BLACK, 90, 180)

    def draw_pine_tree(self, x, y):
        """
        This function draws a pine tree at the specified location.
        """
        # Draw the triangle on top of the trunk
        arcade.draw_triangle_filled(
            x + 40, y, x, y - 100, x + 80, y - 100, arcade.color.DARK_GREEN
        )

        # Draw the trunk
        arcade.draw_lrtb_rectangle_filled(
            x + 30, x + 50, y - 100, y - 140, arcade.color.DARK_BROWN
        )

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.draw_background()
        self.draw_pine_tree(50, 250)
        self.draw_pine_tree(350, 320)
        self.draw_bird(70, 500)
        self.draw_bird(470, 550)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
