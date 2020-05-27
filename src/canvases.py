import os
import tkinter as tk

import config
import utils

from sprites import Sprite, Character


class GameCanvas(tk.Canvas):

    BLOCK = 25

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rock = Sprite(
            file='rock.jpeg',
            size=(self.BLOCK, self.BLOCK))

        self.water = Sprite(
            file='water.jpeg',
            size=(self.BLOCK, self.BLOCK))

        self.grass = Sprite(
            file='grass.png',
            size=(self.BLOCK, self.BLOCK))

        self.peasant = Character(
            name='peasant',
            size=(self.BLOCK, self.BLOCK),
            direction='south'
        )

        self.bind_all('<KeyPress>', self._handle_key_press)

    def _handle_key_press(self, event):
        if event.char in 'wasd':
            # Old coordinates.
            x, y = self.coords(self.peasant.id)

            # Change sprite direction. Calculate new coordinates.
            if event.char == 'w':
                self.peasant.direction = 'north'
                y -= self.BLOCK
            elif event.char == 'a':
                self.peasant.direction = 'west'
                x -= self.BLOCK
            elif event.char == 's':
                self.peasant.direction = 'south'
                y += self.BLOCK
            elif event.char == 'd':
                self.peasant.direction = 'east'
                x += self.BLOCK

            # Delete old image, Create new one.
            self.delete(self.peasant.id)
            self.peasant.id = self.create_image(
                x, y, image=self.peasant.image, anchor='nw')

    def generate_level(self, level_num):
        if level_num == 1:
            self._generate_level_one()

    def _generate_level_one(self):
        self._draw_level_one_background()
        self.peasant.id = self.create_image(
            0, 0, image=self.peasant.image, anchor='nw')

    def _draw_level_one_background(self):
        x, y = 0, 0

        # LINE OF ROCKS
        for i in range(self.winfo_reqwidth() // self.BLOCK):
            self.create_image(x, y, image=self.rock.image, anchor='nw')
            x += self.BLOCK
        y += self.BLOCK

        # MIDDLE GRASS
        for i in range(self.winfo_reqheight() // self.BLOCK - 2):

            # LEFT ROCK
            x = 0
            self.create_image(x, y, image=self.rock.image, anchor='nw')
            x += self.BLOCK

            # GRASS ROW
            for j in range(self.winfo_reqwidth() // self.BLOCK - 2):
                self.create_image(x, y, image=self.grass.image, anchor='nw')
                x += self.BLOCK

            # RIGHT ROCK
            self.create_image(x, y, image=self.rock.image, anchor='nw')

            y += self.BLOCK

        # LINE OF ROCKS
        x = 0
        for i in range(self.winfo_reqwidth() // self.BLOCK):
            self.create_image(x, y, image=self.rock.image, anchor='nw')
            x += self.BLOCK


class DialogueCanvas(tk.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.background_image = utils.create_photo_image(
            os.path.join(config.ASSETS_ROOT, 'witch.png'),
            (self.winfo_reqwidth(), self.winfo_reqheight()))
        self.create_image(0, 0, image=self.background_image, anchor='nw')


class MapCanvas(tk.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.background_image = utils.create_photo_image(
            os.path.join(config.ASSETS_ROOT, 'map.png'),
            (self.winfo_reqwidth(), self.winfo_reqheight()))
        self.create_image(0, 0, image=self.background_image, anchor='nw')
