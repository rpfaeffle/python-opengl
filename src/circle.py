from core.application import Application
from core.component import Component, Render
from core.context import WindowContext
import OpenGL.GL as gl
import math

def rgb(r: int, g: int, b: int):
  return (r / 255, g / 255, b / 255)


class CircleWindow(Render):
    @staticmethod
    def new(cx: WindowContext):
        return CircleWindow()

    def render(self, cx: WindowContext):
        return [
          Circle().set_radius(0.25).set_v_count(2048).set_color(rgb(253, 184, 19)),
          Circle().set_radius(0.03).set_v_count(2048).set_rotation(0.5, .5).set_color(rgb(0, 0, 255))
        ]



class CircleContext(object):
    def __init__(self):
        super().__init__()

        self.radius = 0.5
        self.v_count = 128
        self.rotation_speed = 0.0
        self.rotation_radius = 0.0
        self.color = (1.0, 1.0, 1.0)

    def set_v_count(self, v_count: int):
        self.v_count = v_count
        return self

    def set_radius(self, radius: float):
        self.radius = radius
        return self

    def set_rotation(self, speed: float, radius: float):
        self.rotation_speed = speed
        self.rotation_radius = radius
        return self

    def set_color(self, color: tuple[float, float, float]):
        self.color = color
        return self


class Circle(Component, CircleContext):
    def __init__(self):
        super().__init__()
        self.vertices = []

    @staticmethod
    def build_circle(radius: float, v_count: int):
        angle: float = 360.0 / v_count
        triangle_count: int = v_count - 2
        temp = []
        vertices = []

        for i in range(0, v_count):
            current_angle: float = angle * i
            x: float = radius * math.cos(math.radians(current_angle))
            y: float = radius * math.sin(math.radians(current_angle))
            temp.append((x, y))

        for i in range(0, triangle_count):
            vertices.append((0, 0))
            vertices.append(temp[i + 1])
            vertices.append(temp[i + 2])

        vertices.append((0, 0))
        vertices.append(temp[0])
        vertices.append(temp[1])

        vertices.append((0, 0))
        vertices.append(temp[triangle_count + 1])
        vertices.append(temp[0])

        return vertices

    def render(self, cx: WindowContext):
        if len(self.vertices) == 0:
            # Only generate vertices once
            self.vertices = Circle.build_circle(self.radius, self.v_count)

        gl.glPushMatrix()
        gl.glTranslatef(math.sin(cx.elapsed_time * self.rotation_speed) * self.rotation_radius, math.cos(cx.elapsed_time * self.rotation_speed) * self.rotation_radius, 1.0)
        gl.glColor4f(*self.color, 1.0)
        gl.glBegin(gl.GL_TRIANGLES)
        for vertex in self.vertices:
            gl.glVertex2f(*vertex)
        gl.glEnd()
        gl.glPopMatrix()


if __name__ == '__main__':
    Application().run(lambda cx: CircleWindow.new(cx))
