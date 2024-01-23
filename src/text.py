from core.component import Render
from core.application import Application
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import freetype

class TextRenderer:
    def __init__(self, font_name, size):
        self.face = freetype.Face(font_name)
        self.face.set_char_size(size*64)
        self.list_base = glGenLists(128)
        self.load_chars()

    def load_chars(self):
        for i in range(128):
          self.face.load_char(chr(i), freetype.FT_LOAD_RENDER | freetype.FT_LOAD_FORCE_AUTOHINT)
          bitmap = self.face.glyph.bitmap
          glNewList(self.list_base+i, GL_COMPILE)
          glBitmap(bitmap.width, bitmap.rows, 0, 0, self.face.glyph.advance.x >> 6, 0, bitmap.buffer)
          glEndList()
          error = glGetError()
          if error != GL_NO_ERROR:
              print("Error", error)

    def render_text(self, text, x, y):
        glRasterPos2f(x, y)
        glListBase(self.list_base)
        glCallLists([ord(c) for c in text])

class Text(Render):
  def __init__(self) -> None:
    super().__init__()
    self.text = TextRenderer("./src/Arial.ttf", 16)

  def render(self, cx) -> None:
    glColor3f(1.0, 1.0, 1.0)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    self.text.render_text(f"Hello World", 0, 0)

  @staticmethod
  def new(cx):
    return Text()

if __name__ == '__main__':
    Application(None, [640, 480], "Text").run(lambda cx: Text.new(cx))
