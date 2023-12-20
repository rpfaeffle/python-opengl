from OpenGL.GL import *
from OpenGL.GLUT import *
from datetime import datetime
from typing import Dict, Any


class GlobalContext(object):
    def __init__(self, screen_size):
        self.screen_size = screen_size

    def get_width(self):
        return self.screen_size[0]

    def get_height(self):
        return self.screen_size[1]


class Application(object):
    def __init__(self, screen_size=None, title=None):
        # Set default variables
        if screen_size is None:
            screen_size = [520, 520]
        if title is None:
            title = b"Python OpenGL application"
        self.screen_size = screen_size

        # Set important variables
        self.start_time = None
        self.target_fps = 60

        # Set base context
        self.global_context = GlobalContext(screen_size)

        # Initialize the OpenGL window
        glutInit()
        # Set the size of the window
        glutInitWindowSize(screen_size[0], screen_size[1])
        # Set the title of the window
        glutCreateWindow(title)

    def initialize(self):
        self.start_time = datetime.now()

    # implement by initializing the class
    def render(self, context):
        pass

    def context(self) -> Dict[str, Any]:
        return {}

    def _run(self):
        context = {
          "time": (datetime.now() - self.start_time).total_seconds(),
          "global": self.global_context
        } | self.context()

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)
        # Render the scene
        self.render(self.context() | context)
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
