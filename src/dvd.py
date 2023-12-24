from core.application import Application
from core.component import Render
from components.div import Div
import random


def get_random_direction():
    return random.randint(0, 5) + 1


class BounceAnimation(Render):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_direction = 1
        self.y_direction = 1
        self.item_size = 30

    @staticmethod
    def new(cx):
        return BounceAnimation()

    def render(self, cx):
        # Check if the ball is at the edge of the screen and change direction
        if self.x > cx.width - (self.item_size + self.x_direction):
            self.x_direction = -1 * get_random_direction()
        elif self.x < 0:
            self.x_direction = get_random_direction()

        if self.y > cx.height - (self.item_size + self.y_direction):
            self.y_direction = -1 * get_random_direction()
        elif self.y < 0:
            self.y_direction = get_random_direction()

        # Move the ball
        self.x += self.x_direction
        self.y += self.y_direction

        return Div().set_width(self.item_size).set_height(self.item_size).set_x(self.x).set_y(self.y)


if __name__ == '__main__':
    Application([640, 480], "Bounce Animation").run(lambda cx: BounceAnimation.new(cx))
