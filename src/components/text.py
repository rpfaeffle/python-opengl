from core.component import Component
from core.context import WindowContext
from enum import Enum

class Alignment(Enum):
    Left = 0
    Center = 1

class Text(Component):
    def __init__(self, text: str):
        self.text = text
        self.alignment = Alignment.Left

    def render(self, cx: WindowContext):
        x, y = 0, 0

        if self.alignment == Alignment.Center:
            x = -((cx.font.width * len(self.text)) / 2)

        cx.font.draw(self.text, x, y)

    def set_alignment(self, alignment: Alignment):
        self.alignment = alignment
        return self
