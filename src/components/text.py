from core.component import Component
from core.context import WindowContext


class Text(Component):
    def __init__(self, text: str):
        self.text = text

    def render(self, cx: WindowContext):
        cx.font.draw(self.text, 0, 0)
