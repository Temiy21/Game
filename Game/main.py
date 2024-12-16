"""
Platformer Game
"""

import arcade

Window_Width = 640
Window_Height = 480
Window_Title = 'Game'


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(Window_Width, Window_Height, Window_Title)

        arcade.set_background_color((255, 255, 255, 100))

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        self.clear()
        # Code to draw the screen goes here


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()