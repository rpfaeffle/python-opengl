class OpenGLUtils(object):

    @staticmethod
    def convert_to_normalized_coordinates(x: int, y: int, canvas_width: int, canvas_height: int):
        # Convert pixel coordinates to [-1, 1] range
        normalized_x: float = (x / canvas_width) * 2 - 1
        normalized_y: float = (y / canvas_height) * 2 - 1
        return normalized_x, normalized_y

    @staticmethod
    def convert_to_normalized_size(width: int, height: int, canvas_width: int, canvas_height: int):
        # Convert pixel size to [-1, 1] range
        normalized_width: float = (width / canvas_width) * 2
        normalized_height: float = (height / canvas_height) * 2
        return normalized_width, normalized_height
