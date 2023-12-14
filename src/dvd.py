from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *
from datetime import datetime
import random


def get_random_direction():
    return random.randint(0, 5) + 1


class DVD(Base):
    def __init__(self, screen_size=[520, 520]):
        super().__init__(screen_size)
        self.x_direction = 1
        self.y_direction = 1
        self.start_time = None

    def initialize(self):
        print("Initializing program...")
        self.start_time = datetime.now()
        self.item_size = 10

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

        glPointSize(self.item_size)
        self.UNIFROM_LOCATION_TIME = glGetUniformLocation(self.program_ref, "u_time")
        self.UNIFORM_POSITION = glGetUniformLocation(self.program_ref, "u_position")
        self.x = 50
        self.y = 30

    def update(self):
        glUseProgram(self.program_ref)

        time = (datetime.now() - self.start_time).total_seconds()
        glUniform1f(self.UNIFROM_LOCATION_TIME, time)

        # Check if the ball is at the edge of the screen and change direction
        if self.x > self.screen.get_width() - (self.item_size + self.x_direction):
            self.x_direction = -1 * get_random_direction()
        elif self.x < (self.item_size - self.x_direction):
            self.x_direction = get_random_direction()

        if self.y > self.screen.get_width() - (self.item_size + self.y_direction):
            self.y_direction = -1 * get_random_direction()
        elif self.y < (self.item_size - self.y_direction):
            self.y_direction = get_random_direction()

        # Move the ball
        self.x += self.x_direction
        self.y += self.y_direction

        # Set the position of the ball
        glUniform3f(
            self.UNIFORM_POSITION,
            (self.x / (520 / 2)) - 1.0,
            1.0 - (self.y / (520 / 2)),
            0.0
        )

        # Draw a point
        glDrawArrays(GL_POINTS, 0, 1)


DVD().run()
