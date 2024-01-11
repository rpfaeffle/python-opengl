from core.application import Application
from core.component import Component, Render
from core.context import WindowContext
from components.div import Div
from enum import Enum

PLAYER_DIMENSIONS = (10, 100)
BORDER_WIDTH = 15

class Direction(Enum):
  Up = 0
  Down = 1


class Pong(Render):
    def __init__(self, cx: WindowContext):
        self.player = Player(cx)
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
        ).child(self.player)


class Player(Component):
    def __init__(self, cx: WindowContext):
        super().__init__()
        self.maximum_height = cx.height - BORDER_WIDTH - PLAYER_DIMENSIONS[1] - 10
        self.y = (cx.height - PLAYER_DIMENSIONS[1]) // 2

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
        ).set_y(self.y).set_x(cx.width - 10 - 15)


if __name__ == '__main__':
    Application(None, [640, 480], "Pong Game").run(lambda cx: Pong.new(cx))
