import OpenGL.GL as gl
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
        self.color = (1, 1, 1, 1)

    def render(self, cx: WindowContext):
        x, y = 0, 0

        if self.alignment == Alignment.Center:
            x = -((cx.font.width * len(self.text)) / 2)

        gl.glColor4f(*self.color)
        cx.font.draw(self.text, x, y)

    def set_color(self, color: tuple[float, float, float, float]):
        self.color = color
        return self

    def set_alignment(self, alignment: Alignment):
        self.alignment = alignment
        return self
