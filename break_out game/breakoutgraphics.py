"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Breakout graphics design
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constants
BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # variables
        self.ball_radius = ball_radius
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.pf = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width) / 2,
                            y=window_height - paddle_offset
                              - paddle_height)
        self.window.add(self.paddle)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle.color = 'black'
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=window_width / 2 - ball_radius,
                          y=window_height / 2 - ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.ball.__dy = 0
        self.ball.__dx = 0
        # Draw bricks
        self.rows = brick_rows
        self.cols = brick_cols
        for i in range(self.rows):
            for j in range(self.cols):
                self.brick = GRect(brick_width, brick_height, x=0 + j * (brick_width + brick_spacing),
                                   y=brick_offset + i * (brick_height + brick_spacing))
                self.window.add(self.brick)
                self.brick.filled = True
                if i < 2:
                    self.brick.fill_color = 'red'
                elif i < 4:
                    self.brick.fill_color = 'orange'
                elif i < 6:
                    self.brick.fill_color = 'yellow'
                elif i < 8:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
        onmousemoved(self.follow_paddle)
        onmouseclicked(self.move_the_ball)

    # Paddle follows the mouse
    def follow_paddle(self, mouse):
        self.window.add(self.paddle, x=mouse.x - self.paddle.width / 2, y=self.window.height - self.pf)
        if mouse.x - self.paddle.width / 2 <= 0:
            self.window.add(self.paddle, x=0, y=self.window.height - self.pf)
        if mouse.x + self.paddle.width / 2 >= self.window.width:
            self.window.add(self.paddle, x=self.window.width - self.paddle.width, y=self.window.height - self.pf)

    def move_the_ball(self, mouse):
        if self.ball.x == self.window.width / 2 - BALL_RADIUS and self.ball.y == self.window.height / 2 - BALL_RADIUS:
            self.ball_dx = MAX_X_SPEED
            self.ball_dy = INITIAL_Y_SPEED

    def respawn(self):
        self.window.add(self.ball, x=self.window.width / 2 - self.ball_radius,
                        y=self.window.height / 2 - self.ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'
        self.ball.__dx = 0
        self.ball.__dy = 0

    def crack_the_brisk(self, brick):
        self.window.remove(brick)

    @property
    def ball_dx(self):
        return self.ball.__dx

    @property
    def ball_dy(self):
        return self.ball.__dy

    @ball_dx.setter
    def ball_dx(self, new_speed):
        new_speed = random.randint(1, new_speed)
        if random.random() > 0.5:
            new_speed = -new_speed
        self.ball.__dx = new_speed

    @ball_dy.setter
    def ball_dy(self, new_speed):
        self.ball.__dy = new_speed

    # self.ball.__dy = INITIAL_Y_SPEED
    # self.ball.__dx = random.randint(1, MAX_X_SPEED)
    # if random.random() > 0.5:
    #     self.ball.__dx = -self.ball.__dx
    # Initialize our mouse listeners
