from pico2d import *
import common

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
        if self.x >= common.court.window_left and self.x <= common.court.window_left + common.court.cw and self.y >= common.court.window_bottom and self.y <= common.court.window_bottom + common.court.ch:
            sx = self.x - common.court.window_left
            sy = self.y - common.court.window_bottom
            self.image.clip_draw(0, 0, 23, 23, sx, sy, 20, 20)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self):
        pass