from core.application import Application, GlobalContext
from core.component import Component
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *


class Pong(Application):
    def __init__(self, screen_size=[858, 525]):
        super().__init__(screen_size, "Pong Game")
        self.border_width = 15
        self.player = None

    def initialize(self):
        super().initialize()
        self.borders = [
            Rectangle(0, 0, self.screen_size[0], self.border_width, self.global_context),
            Rectangle(0, self.screen_size[1] - self.border_width, self.screen_size[0], self.border_width,
                      self.global_context),
        ]

    def render_border(self, context):
        for border in self.borders:
            border.render(context)

    def render(self, context):
        self.render_border(context)


class Rectangle(Component):
    def __init__(self, x: int, y: int, width: int, height: int, context: GlobalContext, color=(1.0, 1.0, 1.0, 0.5)):
        super().__init__()
        screen_width, screen_height = context.get_width(), context.get_height()
        self.x, self.y = OpenGLUtils.convert_to_normalized_coordinates(
            x,
            y,
            screen_width,
            screen_height
        )
        self.width, self.height = OpenGLUtils.convert_to_normalized_size(
            width,
            height,
            screen_width,
            screen_height
        )
        self.color = color

    def render(self, context):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)  # Position the rectangle
        glColor4f(self.color[0], self.color[1], self.color[2], self.color[3])  # Set the rectangle color
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(0, self.height)
        glVertex2f(self.width, self.height)
        glVertex2f(self.width, 0)
        glEnd()
        glPopMatrix()


Pong().run()
