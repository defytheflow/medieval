import os
import tkinter as tk

import utils


class GameCanvas(tk.Canvas):

    SQUARE = 25

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ROCK_IMAGE = utils.create_photo_image(
            os.path.join('assets', 'rock.jpeg'), (self.SQUARE, self.SQUARE))
        self.WATER_IMAGE = utils.create_photo_image(
            os.path.join('assets', 'water.jpeg'), (self.SQUARE, self.SQUARE))
        self.GRASS_IMAGE = utils.create_photo_image(
            os.path.join('assets', 'grass.png'), (self.SQUARE, self.SQUARE))

    # Public
    def generate_level(self, level_num):
        if level_num == 1:
            self._generate_level_one()

    # Private
    def _generate_level_one(self):
        x, y = 0, 0

        # LINE OF ROCKS
        for i in range(int(self['width']) // self.SQUARE):
            self.create_image(x, y, image=self.ROCK_IMAGE, anchor='nw')
            x += self.SQUARE
        y += self.SQUARE

        # MIDDLE GRASS
        for i in range(int(self['height']) // self.SQUARE - 2):  # two lines of rocks.

            # LEFT ROCK
            x = 0
            self.create_image(x, y, image=self.ROCK_IMAGE, anchor='nw')
            x += self.SQUARE

            # GRASS ROW
            for j in range(int(self['width']) // self.SQUARE - 2): # two rocks.
                self.create_image(x, y, image=self.GRASS_IMAGE, anchor='nw')
                x += self.SQUARE

            # RIGHT ROCK
            self.create_image(x, y, image=self.ROCK_IMAGE, anchor='nw')

            y += self.SQUARE

        # LINE OF ROCKS
        x = 0
        for i in range(int(self['width']) // self.SQUARE):
            self.create_image(x, y, image=self.ROCK_IMAGE, anchor='nw')
            x += self.SQUARE


class DialogueCanvas(tk.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.background_image = utils.create_photo_image(
            os.path.join('assets', 'witch.png'),
            (200, 200))
        self.create_image(0, 0, image=self.background_image, anchor=tk.NW)
