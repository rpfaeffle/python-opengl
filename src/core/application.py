from OpenGL.GL import *
from OpenGL.GLUT import *
from core.component import Component


class Application(object):
    def __init__(self, screen_size=None, title=None):
        # Set default variables
        if screen_size is None:
            screen_size = [520, 520]
        if title is None:
            title = b"Python OpenGL application"
        self.screen_size = screen_size

        # Set important variables
        self.is_running = True

        # Initialize the OpenGL window
        glutInit()
        # Set the size of the window
        glutInitWindowSize(screen_size[0], screen_size[1])
        # Set the title of the window
        glutCreateWindow(title)

    # implement by initializing the class
    def initialize(self):
        pass

    # implement by initializing the class
    def render(self) -> Component:
        pass

    def _run(self):
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)
        root = self.render()
        root.render(None)
        glFlush()

    def run(self):
        # Startup
        self.initialize()

        # Set the display function, this is the applications run function
        glutDisplayFunc(self._run)
        # Start the main OpenGL loop
        glutMainLoop()
