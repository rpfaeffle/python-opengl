from OpenGL.GL import *
from core.component import Component
from core.context import WindowContext
from core.openGLUtils import OpenGLUtils


class Div(Component):
    def __init__(self):
        super().__init__()
        self.children = []
        self.x = 0
        self.y = 0
        self.height = 0
        self.width = 0

    def set_height(self, height: int):
        self.height = height
        return self

    def set_width(self, width: int):
        self.width = width
        return self

    def set_position(self, x: int, y: int):
        return self.set_x(x).set_y(y)

    def set_x(self, x: int):
        self.x = x
        return self

    def set_y(self, y: int):
        self.y = y
        return self

    def render(self, cx: WindowContext):
        x, y = OpenGLUtils.convert_to_normalized_coordinates(self.x, self.y, cx.width, cx.height)
        width, height = OpenGLUtils.convert_to_normalized_size(self.width, self.height, cx.width, cx.height)

        glPushMatrix()
        glTranslatef(x, y, 0)  # Position the rectangle
        color = (1.0, 1.0, 1.0, 0.5)
        glColor4f(color[0], color[1], color[2], color[3])  # Set the rectangle color
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(0, height)
        glVertex2f(width, height)
        glVertex2f(width, 0)
        glEnd()
        glPopMatrix()

        return self.children

    def child(self, child):
        self.children.append(child)
        return self
