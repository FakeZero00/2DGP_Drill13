from pico2d import *

class Ball:
    def __init__(self, x, y):
        self.image = None
        self.x = x
        self.y = y
        if self.image is None:
            self.image = load_image('ball21x21.png')

    def update(self):
        pass

    def draw(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self):
        pass