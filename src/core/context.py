from core.input import Input


class ViewContext(object):
    def __init__(self):
        self.bg_color = (1.0, 1.0, 1.0, 1.0)

    def bg(self, color: tuple[float, float, float, float]):
        self.bg_color = color
        return self


class WindowContext(object):
    def __init__(self):
        self.width = 720
        self.height = 540
        self.title = "Main Application Window"
        self.input = Input()

    def set_width(self, width: int):
        self.width = width
        return self

    def set_height(self, height: int):
        self.height = height
        return self

    def set_title(self, title: str):
        self.title = title
        return self
