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

          # Generate a texture for the character
          texture = glGenTextures(1)
          glBindTexture(GL_TEXTURE_2D, texture)
          glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
          glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

          glTexImage2D(GL_TEXTURE_2D, 0, GL_ALPHA, bitmap.width, bitmap.rows, 0, GL_ALPHA, GL_UNSIGNED_BYTE, bitmap.buffer)

          width, height = bitmap.width / 640, bitmap.rows / 480

          # Create a display list for the character
          glNewList(self.list_base+i, GL_COMPILE)
          glBindTexture(GL_TEXTURE_2D, texture)
          glBegin(GL_QUADS)
          glTexCoord2f(0, 1); glVertex2f(0, 0)
          glTexCoord2f(1, 1); glVertex2f(width, 0)
          glTexCoord2f(1, 0); glVertex2f(width, height)
          glTexCoord2f(0, 0); glVertex2f(0, height)
          glEnd()
          glBindTexture(GL_TEXTURE_2D, 0)
          glEndList()

          # Unbind the texture
          glBindTexture(GL_TEXTURE_2D, 0)


    def render_text(self, text, x, y):
      glPushMatrix()
      glTranslatef(x, y, 0)
      glListBase(self.list_base)
      for c in text:
        if 32 <= ord(c) < 127:
          glCallList(self.list_base + ord(c))
          glTranslatef(.03, 0, 0)
      glPopMatrix()

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
