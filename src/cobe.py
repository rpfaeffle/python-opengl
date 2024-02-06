from OpenGL.GLUT import glutReshapeFunc, glutSolidSphere
from core.application import Application
from core.component import Component, Render
import OpenGL.GL as gl
import OpenGL.GLU as glu

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
    gl.glLoadIdentity()

    cx.rotate_y += 0.5
    # cx.rotate_x += 0.5

    gl.glTranslatef(0.0, 0.0, -8.0)
    gl.glColor3f(0.5, 0.5, 1.0)

    # Rotate when user changes rotate_x and rotate_y
    gl.glRotatef(cx.rotate_x, 1.0, 0.0, 0.0)
    gl.glRotatef(cx.rotate_y, 0.0, 1.0, 0.0)
    gl.glRotatef(90.0, 0.0, 0.0, 1.0)

    gl.glScalef(1.0, 1.0, 1.0)

    glutSolidSphere(1.0, 20, 20)

if __name__ == '__main__':
  def reshape_func(x: int, y: int):
    # Nothing is visible so return
    if y == 0 or x == 0:
      return

    # Setup the new projection matrix
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()

    # Angle of view: 40 degrees
    # Near clipping plane distance: 0.5
    # Far clipping plane distance: 20.0
    glu.gluPerspective(40.0, x / y, 0.5, 20.0)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glViewport(0, 0, x, y) # Use the whole window for rendering


  def setup(cx):
    gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
    glutReshapeFunc(reshape_func)

  Application(setup,None,None).run(lambda cx: CobeWindow.new(cx))
