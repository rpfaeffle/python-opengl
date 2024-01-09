from core.application import Application
from core.component import Component, Render
from core.context import WindowContext
from components.div import Div
from enum import Enum

class Direction(Enum):
  Up = 0
  Down = 1


class Pong(Render):
    def __init__(self, cx: WindowContext):
        self.border_width = 15
        self.player = Player()
        cx.input.register(b'w', 0, lambda: self.player.move(Direction.Up))
        cx.input.register(b's', 0, lambda: self.player.move(Direction.Down))
        setattr(cx, 'player', {})

    @staticmethod
    def new(cx: WindowContext):
        return Pong(cx)

    def render(self, cx):
        return Div().child(
            Div() \
                .set_width(cx.width) \
                .set_height(self.border_width)
        ).child(
            Div() \
                .set_width(cx.width) \
                .set_height(self.border_width) \
                .set_y(cx.height - self.border_width)
        ).child(self.player)


class Player(Component):
    def __init__(self):
        super().__init__()
        self.y = 240 - 50

    def move(self, direction: Direction):
        if direction == Direction.Up:
            self.y += 10
        elif direction == Direction.Down:
            self.y -= 10

    def render(self, cx):
        return Div().set_width(10).set_height(100).set_y(self.y).set_x(cx.width - 10 - 15)


if __name__ == '__main__':
    Application(None, [640, 480], "Pong Game").run(lambda cx: Pong.new(cx))
