import math
import random
from core.application import Application
from core.component import Component, Render
from core.context import WindowContext
from components.div import Div
from enum import Enum


PLAYER_DIMENSIONS = (10, 100)
BALL_DIMENSIONS = (10, 10)
BORDER_WIDTH = 15
BALL_SPEED = 1
MAX_BOUNCE_ANGLE = 75


class Direction(Enum):
    Up = 0
    Down = 1


class Pong(Render):
    def __init__(self, cx: WindowContext):
        self.player = Player(cx, True)
        self.computer = Player(cx, False)
        self.ball = Ball(cx)
        cx.input.register(b'w', 0, lambda: self.player.move(Direction.Up))
        cx.input.register(b's', 0, lambda: self.player.move(Direction.Down))

    @staticmethod
    def new(cx: WindowContext):
        return Pong(cx)

    def render(self, cx):
        return Div().child(
            Div() \
                .set_width(cx.width) \
                .set_height(BORDER_WIDTH)
        ).child(
            Div() \
                .set_width(cx.width) \
                .set_height(BORDER_WIDTH) \
                .set_y(cx.height - BORDER_WIDTH)
        ).child(
            self.player
        ).child(
            self.ball
        ).child(
            self.computer
        )


class Ball(Component):
    def __init__(self, cx: WindowContext):
        super().__init__()
        self.x = cx.width // 2
        self.y = cx.height // 2
        self.direction = Direction.Up
        self.speed = BALL_SPEED
        self.velocity = [0., 0.]
        initial_angle = random.randint(-MAX_BOUNCE_ANGLE, MAX_BOUNCE_ANGLE)
        self.update_velocity(initial_angle)

    def move(self, cx: WindowContext):
        if 0 <= self.x <= cx.width:
            self.x += self.velocity[0]
        if not (BORDER_WIDTH <= self.y <= cx.height - BORDER_WIDTH):
            self.velocity = [self.velocity[0], -self.velocity[1]]
        self.y += self.velocity[1]

    def update_velocity(self, angle: float):
        self.velocity[0] = self.speed * math.sin(angle)
        self.velocity[1] = self.speed * math.cos(angle)

    def render(self, cx):
        self.move(cx)

        return Div().set_width(
            BALL_DIMENSIONS[0]
        ).set_height(
            BALL_DIMENSIONS[1]
        ).set_x(
            self.x - BALL_DIMENSIONS[0] // 2
        ).set_y(
            self.y - BALL_DIMENSIONS[1] // 2
        )


class Player(Component):
    def __init__(self, cx: WindowContext, is_player: bool = True):
        super().__init__()
        self.maximum_height = cx.height - BORDER_WIDTH - PLAYER_DIMENSIONS[1] - 10
        self.y = (cx.height - PLAYER_DIMENSIONS[1]) // 2
        self.x = cx.width - 10 * 2 - PLAYER_DIMENSIONS[0] // 2 if is_player else 10 + PLAYER_DIMENSIONS[0] // 2

    def move(self, direction: Direction):
        if direction == Direction.Up and self.y < self.maximum_height:
            self.y += 10
        elif direction == Direction.Down and self.y > BORDER_WIDTH + 10:
            self.y -= 10

    def render(self, cx):
        return Div().set_width(
            PLAYER_DIMENSIONS[0]
        ).set_height(
            PLAYER_DIMENSIONS[1]
        ).set_y(self.y).set_x(self.x)


if __name__ == '__main__':
    Application(None, [640, 480], "Pong Game").run(lambda cx: Pong.new(cx))
