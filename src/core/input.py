import OpenGL.GLUT as glut


class Input:
    _instance = None

    # Singleton class
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.callbacks = {}

    def register(self, key, modifiers, callback):
        self.callbacks[(key, modifiers)] = callback

    def handle_keyboard_event(self, key, x, y):
        modifiers = glut.glutGetModifiers()
        if (key, modifiers) in self.callbacks:
            self.callbacks[(key, modifiers)]()

    def start(self):
        glut.glutKeyboardFunc(self.handle_keyboard_event)
