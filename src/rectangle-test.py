from core.base import Application
from core.component import Component
from OpenGL.GL import *

class Test(Application):
    def __init__(self, screen_size=[520, 520]):
        super().__init__(screen_size)

    def render(self) -> Component:
        return Rectangle()


class Rectangle(Component):
    def __init__(self):
        super().__init__()

    def render(self, context):
        glColor3f(1.0, 1.0, 0.0)  # Set the rectangle color

        # Define the vertices of the rectangle
        size_x = 100
        size_y = 50
        vertices = [
            (0, 0),
            (0, -1 * size_y / 300),
            (size_x / 400, -1 * size_y / 300),
            (size_x / 400, 0)
        ]

        glBegin(GL_QUADS)
        for vertex in vertices:
            glVertex2f(*vertex)
        glEnd()

Test().run()
