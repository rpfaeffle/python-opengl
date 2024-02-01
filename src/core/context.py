from core.input import Input


class WindowContext(object):
    _instance = None

    # Singleton
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.width = 720
        self.height = 540
        self.title = "Main Application Window"
        self.elapsed_time = 0
        self.input = Input()
        self.font = None

    def set_width(self, width: int):
        self.width = width
        return self

    def set_height(self, height: int):
        self.height = height
        return self

    def set_title(self, title: str):
        self.title = title
        return self
