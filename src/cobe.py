from OpenGL.GLUT import glutReshapeFunc, glutSolidSphere
from core.application import Application
from core.component import Component, Render
from OpenGL.GL import *
from OpenGL.GLU import *

class CobeWindow(Render):
  @staticmethod
  def new(cx):
    cx.rotate_x = 0
    cx.rotate_y = 0
    return CobeWindow()

  def render(self, cx):
    return Cobe(cx)

class Cobe(Component):
  def __init__(self, cx):
    super().__init__()

  def render(self, cx):
    glLoadIdentity()

    cx.rotate_y += 0.5
    # cx.rotate_x += 0.5

    glTranslatef(0.0, 0.0, -8.0)
    glColor3f(0.5, 0.5, 1.0)

    # Rotate when user changes rotate_x and rotate_y
    glRotatef(cx.rotate_x, 1.0, 0.0, 0.0)
    glRotatef(cx.rotate_y, 0.0, 1.0, 0.0)
    glRotatef(90.0, 0.0, 0.0, 1.0)

    glScalef(1.0, 1.0, 1.0)

    glutSolidSphere(1.0, 20, 20)

if __name__ == '__main__':
  def reshape_func(x: int, y: int):
    # Nothing is visible so return
    if y == 0 or x == 0:
      return

    # Setup the new projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Angle of view: 40 degrees
    # Near clipping plane distance: 0.5
    # Far clipping plane distance: 20.0
    gluPerspective(40.0, x / y, 0.5, 20.0)

    glMatrixMode(GL_MODELVIEW)
    glViewport(0, 0, x, y) # Use the whole window for rendering


  def setup(cx):
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glutReshapeFunc(reshape_func)

  Application(setup,None,None).run(lambda cx: CobeWindow.new(cx))
