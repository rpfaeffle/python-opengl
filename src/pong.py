from core.application import Application
from core.component import Render
from core.context import WindowContext
from components.div import Div


class Pong(Render):
    def __init__(self):
        self.border_width = 15

    @staticmethod
    def new(cx: WindowContext):
        return Pong()

    def render(self, cx):
        return Div().child(
            Div().set_width(cx.width).set_height(self.border_width)
        ).child(
            Div().set_width(cx.width).set_height(self.border_width).set_y(cx.height - self.border_width)
        )


if __name__ == '__main__':
    Application([640, 480], "Pong Game").run(lambda cx: Pong.new(cx))
