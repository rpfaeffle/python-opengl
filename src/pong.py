from core.application import Application
from core.component import Component, Render
from core.context import WindowContext
from components.div import Div


class Pong(Render):
    def __init__(self, cx: WindowContext):
        self.border_width = 15
        cx.input.register(b'w', 0, lambda: Pong.on_move_up(cx))
        cx.input.register(b's', 0, lambda: Pong.on_move_down(cx))
        setattr(cx, 'player', {})

    @staticmethod
    def on_move_up(cx: WindowContext):
        current_y = getattr(cx, 'player').get('y', 240 - 50)
        getattr(cx, 'player')['y'] = current_y + 10

    @staticmethod
    def on_move_down(cx: WindowContext):
        current_y = getattr(cx, 'player').get('y', 240 - 50)
        getattr(cx, 'player')['y'] = current_y - 10

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
        ).child(Player())


class Player(Component):
    def __init__(self):
        super().__init__()
        self.y = 240 - 50

    def render(self, cx):
        y_position = getattr(cx, 'player').get('y', 240 - 50)
        return Div().set_width(10).set_height(100).set_y(y_position).set_x(cx.width - 10 - 15)


if __name__ == '__main__':
    Application([640, 480], "Pong Game").run(lambda cx: Pong.new(cx))
