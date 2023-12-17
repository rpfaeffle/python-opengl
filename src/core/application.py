from OpenGL.GL import *
from OpenGL.GLUT import *


class Application(object):
    def __init__(self, screen_size=None, title=None):
        # Set default variables
        if screen_size is None:
            screen_size = [520, 520]
        if title is None:
            title = b"Python OpenGL application"
        self.screen_size = screen_size

        # Set important variables
        self.target_fps = 60

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
    def render(self, context):
        pass

    def context(self):
        pass

    def _run(self):
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)
        self.render(self.context())
        glFlush()

    def update(self, _):
        glutPostRedisplay()  # Trigger a redraw
        glutTimerFunc(int(1000 / self.target_fps), self.update, 0)  # Restart the timer

    def run(self):
        # Startup
        self.initialize()
        # Set the display function, this is the applications run function
        glutDisplayFunc(self._run)
        # Set a timer to trigger a redraw of the screen
        glutTimerFunc(int(1000 / self.target_fps), self.update, 0)
        # Start the main OpenGL loop
        glutMainLoop()
