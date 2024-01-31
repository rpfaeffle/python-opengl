import OpenGL.GL as gl
import freetype

SUPPORTED_CHARACTERS = 128

class Font:
    def __init__(self, font_name: str, size: int, cx):
        self.font_name = font_name
        self.size = size
        self.width = 0

        self.list_base = gl.glGenLists(SUPPORTED_CHARACTERS)

        self.face = freetype.Face(font_name)
        self.face.set_char_size(size * 64 * 4)

        self.load(cx)


    def load(self, cx):
        gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 1)
        for i in range(SUPPORTED_CHARACTERS):
            self.face.load_char(chr(i), freetype.FT_LOAD_RENDER | freetype.FT_LOAD_FORCE_AUTOHINT)
            bitmap = self.face.glyph.bitmap

            self.width = max(self.width, (bitmap.width * 1.25) / cx.width)

            # Generate a texture for the character
            texture = gl.glGenTextures(1)
            gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
            gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
            gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)

            gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_ALPHA, bitmap.width, bitmap.rows, 0, gl.GL_ALPHA, gl.GL_UNSIGNED_BYTE, bitmap.buffer)

            width = self.face.glyph.metrics.width / 64 / cx.width
            height = self.face.glyph.metrics.height / 64 / cx.height
            bearing_x = self.face.glyph.metrics.horiBearingX / 64 / cx.width
            bearing_y = (self.face.glyph.metrics.horiBearingY - self.face.glyph.metrics.height) / 64 / cx.height
            advance = self.face.glyph.metrics.horiAdvance / 64 / cx.width

            # Calculate the texture coordinates
            tex_coord_x = bitmap.width / cx.width
            tex_coord_y = bitmap.rows / cx.height

            # Create a display list for the character
            gl.glNewList(self.list_base + i, gl.GL_COMPILE)
            gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
            gl.glBegin(gl.GL_QUADS)
            gl.glTexCoord2f(0, 1); gl.glVertex2f(bearing_x, bearing_y)
            gl.glTexCoord2f(1, 1); gl.glVertex2f(bearing_x + width, bearing_y)
            gl.glTexCoord2f(1, 0); gl.glVertex2f(bearing_x + width, bearing_y + height)
            gl.glTexCoord2f(0, 0); gl.glVertex2f(bearing_x, bearing_y + height)
            gl.glEnd()
            gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
            gl.glEndList()

            # Unbind the texture
            gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

    def draw(self, text: str, x: float, y: float):
        gl.glPushMatrix()
        gl.glTranslatef(x, y, 0)
        for c in text:
            gl.glCallList(self.list_base + ord(c))
            gl.glTranslatef(self.width, 0, 0)
        gl.glPopMatrix()
