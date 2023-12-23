from OpenGL.GL import *
from OpenGL.GLUT import *
from core.context import WindowContext
from core.component import Render
from datetime import datetime
from typing import Callable
import time


class Application(object):
    def __init__(self, screen_size=None, title=None):
        # Set default variables
        if screen_size is None:
            screen_size = [520, 520]
        if title is None:
            title = format(b"Python OpenGL application")
        self.screen_size = screen_size

        # Set important variables
        self.start_time = None
        self.target_fps = 60

        # Set base context
        self.cx = WindowContext().set_width(screen_size[0]).set_height(screen_size[1]).set_title(title)

        # Initialize the OpenGL window
        glutInit()
        # Set the size of the window
        glutInitWindowSize(screen_size[0], screen_size[1])
        # Set the title of the window
        glutCreateWindow(title)

    def initialize(self):
        self.start_time = datetime.now()
        self.previous_time = time.time()
        self.current_frame = 0

    # implement by initializing the class
    def render(self):
        pass

    # There is a type conflict between Render and Component
    # and due to the fact that this is an internal method
    # typing is not provided for this method
    def _run(self, component):
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)
        # Render the scene
        while component is not None:
            component = component.render(self.cx)
        # Flush the buffer
        glFlush()

    def update(self, frame):
        self.current_frame += 1

        if frame % 60 == 0:
            current_time = time.time()
            elapsed_time = datetime.now() - self.start_time
            frame_rate = frame / elapsed_time.total_seconds()
            print(f"FPS: {frame_rate:.2f}")
            self.previous_time = current_time

        glutPostRedisplay()  # Trigger a redraw
        glutTimerFunc(int(1000 / self.target_fps), self.update, self.current_frame)  # Restart the timer

    def run(self, callback: Callable[[WindowContext], Render]):
        # Startup
        self.initialize()
        # Get the base component
        base_component = callback(self.cx)
        # Set the display function, this is the applications run function
        glutDisplayFunc(lambda: self._run(base_component))
        # Set a timer to trigger a redraw of the screen
        glutTimerFunc(int(1000 / self.target_fps), self.update, 0)
        # Start the main OpenGL loop
        glutMainLoop()
