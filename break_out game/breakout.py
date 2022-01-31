"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Breakout Game!!
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


# Global variables


def main():
    graphics = BreakoutGraphics()
    game_on(graphics)


def game_on(graphics):
    lives = NUM_LIVES
    vx = 0
    vy = 0
    scores = 0
    while True:
        upper_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        lower_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        upper_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
        lower_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                    graphics.ball.y + graphics.ball.height)
        # Give the ball speed and make it move
        if graphics.ball_dx != 0 and graphics.ball_dy != 0:
            if graphics.ball.x == graphics.window.width / 2 - graphics.ball_radius and graphics.ball.y == graphics.window.height / 2 - graphics.ball_radius:
                vx = graphics.ball_dx
                vy = graphics.ball_dy
        graphics.ball.move(vx, vy)
        # Make the ball bounce when it hit on the wall
        if graphics.ball.x + graphics.ball.width >= graphics.window.width or graphics.ball.x <= 0:
            vx = -vx
        if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
            vy = -vy
        # Detect the collision
        # Upper left
        if upper_left is not None and upper_left is not graphics.paddle:
            graphics.crack_the_brisk(upper_left)
            scores += 1
            vy = -vy
        # Lower left
        elif lower_left is not None and lower_left is not graphics.paddle:
            graphics.crack_the_brisk(lower_left)
            scores += 1
            vy = -vy
        # Upper right
        elif upper_right is not None and upper_right is not graphics.paddle:
            graphics.crack_the_brisk(upper_right)
            scores += 1
            vy = -vy
        # Lower right
        elif lower_right is not None and lower_right is not graphics.paddle:
            graphics.crack_the_brisk(lower_right)
            scores += 1
            vy = -vy
        # If it hit the paddle
        lower_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        lower_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                    graphics.ball.y + graphics.ball.height)
        if lower_left is graphics.paddle or lower_right is graphics.paddle:
            vy = -vy
            if graphics.ball.y + graphics.ball.height > graphics.paddle.y:
                a = graphics.ball.x
                graphics.window.remove(graphics.ball)
                graphics.window.add(graphics.ball, x=a, y=graphics.paddle.y - graphics.ball.height)
        # Lose one live and play again
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            graphics.window.remove(graphics.ball)
            graphics.respawn()
            vx = 0
            vy = 0
        # Run out of lives
        if lives == 0:
            break
        if scores == graphics.rows * graphics.cols:
            break
        pause(FRAME_RATE)

    # Add the animation loop here!


if __name__ == '__main__':
    main()
