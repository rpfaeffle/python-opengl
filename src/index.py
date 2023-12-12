from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *
from datetime import datetime
import math

class Test(Base):
    def __init__(self, screen_size=[520, 520]):
        super().__init__(screen_size)
        self.start_time = None

    def initialize(self):
        print("Initializing program...")
        self.start_time = datetime.now()

        vs_code = """
        uniform vec3 u_position;
        void main() {
          gl_Position = vec4(u_position, 1.0);
        }
        """

        fs_code = """
        out vec4 fragColor;
        uniform float u_time;
        void main()
        {
          fragColor = vec4(abs(sin(u_time)), abs(cos(u_time)), abs(sin(u_time + 0.5)), 1.0);
        }
        """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code);
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)

        glPointSize(100)
        self.UNIFROM_RESOLUTION = glGetUniformLocation(self.program_ref, "u_resolution")
        self.UNIFROM_LOCATION_TIME = glGetUniformLocation(self.program_ref, "u_time")
        self.UNIFORM_POSITION = glGetUniformLocation(self.program_ref, "u_position")

    def update(self):
        glUseProgram(self.program_ref)

        time = (datetime.now() - self.start_time).total_seconds()
        glUniform1f(self.UNIFROM_LOCATION_TIME, time)
        glUniform2f(self.UNIFROM_RESOLUTION, 100, 100)
        # Get position on circle for time
        x = math.cos(time) * 0.5
        y = math.sin(time) * 0.5
        glUniform3f(self.UNIFORM_POSITION, x, y, 0.0)

        # Draw a point
        glDrawArrays(GL_POINTS, 0, 1)

Test().run()
