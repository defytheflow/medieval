import os
import time
import tkinter as tk

import config
import utils

from sprites import Sprite, Character


class GameCanvas(tk.Canvas):

    BLOCK_SIZE = 25  # pixels

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rock = Sprite(
            file='rock.jpeg',
            size=(self.BLOCK_SIZE, self.BLOCK_SIZE))

        self.grass = Sprite(
            file='grass.png',
            size=(self.BLOCK_SIZE, self.BLOCK_SIZE))

        self.peasant = Character(
            name='peasant',
            size=(self.BLOCK_SIZE, self.BLOCK_SIZE),
            direction='south',
            speed=1,
        )

        self._pressed = False
        self._wait = 10  # milliseconds

        self.focus_set()
        self.bind('<KeyPress>', lambda e: self._key_press_decorator(self._handle_key_press, e))

    def _key_press_decorator(self, callback_func, event):
        if not self._pressed:
            self._pressed = True
            callback_func(event)
            self._pressed = False

    def _handle_key_press(self, event):
        # If peasant does not exist, do nothing
        if not self.gettags(self.peasant.name):
            return

        if event.char in 'wasd':
            old_x, old_y = self.coords(self.peasant.id)

            # Change sprite direction. Calculate new coordinates.
            if event.char == 'w':
                self.peasant.direction = 'north'
                new_x = old_x
                new_y = old_y - self.BLOCK_SIZE
            elif event.char == 'a':
                self.peasant.direction = 'west'
                new_x = old_x - self.BLOCK_SIZE
                new_y = old_y
            elif event.char == 's':
                self.peasant.direction = 'south'
                new_x = old_x
                new_y = old_y + self.BLOCK_SIZE
            else:
                self.peasant.direction = 'east'
                new_x = old_x + self.BLOCK_SIZE
                new_y = old_y

            if old_x != new_x:
                if old_x < new_x:
                    for i in range(1, self.BLOCK_SIZE + 1, self.peasant.speed):
                        self.peasant.switch_costume()
                        self._redraw_character(self.peasant, old_x + i, old_y)
                        self.after(self._wait)
                        self.update()
                else:
                    for i in range(1, self.BLOCK_SIZE + 1, self.peasant.speed):
                        self.peasant.switch_costume()
                        self._redraw_character(self.peasant, old_x - i, old_y)
                        self.after(self._wait)
                        self.update()
            else:
                if old_y < new_y:
                    for i in range(1, self.BLOCK_SIZE + 1, self.peasant.speed):
                        self.peasant.switch_costume()
                        self._redraw_character(self.peasant, old_x, old_y + i)
                        self.after(self._wait)
                        self.update()
                else:
                    for i in range(1, self.BLOCK_SIZE + 1, self.peasant.speed):
                        self.peasant.switch_costume()
                        self._redraw_character(self.peasant, old_x, old_y - i)
                        self.after(self._wait)
                        self.update()

            self.peasant.reset_costume()
            self._redraw_character(self.peasant, new_x, new_y)

    def _draw_character(self, character, x, y):
        character.id = self.create_image(
            x, y, image=character.image, anchor='nw', tags=character.name)

    def _redraw_character(self, character, x, y):
        self.delete(character)
        self._draw_character(character, x, y)

    def _generate_level_one(self):
        self._draw_level_one_background()
        self._draw_character(self.peasant, 0, 0)

    def generate_level(self, level_num):
        if level_num == 1:
            self._generate_level_one()

    def _draw_level_one_background(self):
        x, y = 0, 0

        # LINE OF ROCKS
        for i in range(self.winfo_reqwidth() // self.BLOCK_SIZE):
            self.create_image(x, y, image=self.rock.image, anchor='nw')
            x += self.BLOCK_SIZE
        y += self.BLOCK_SIZE

        # MIDDLE GRASS
        for i in range(self.winfo_reqheight() // self.BLOCK_SIZE - 2):

            # LEFT ROCK
            x = 0
            self.create_image(x, y, image=self.rock.image, anchor='nw')
            x += self.BLOCK_SIZE

            # GRASS ROW
            for j in range(self.winfo_reqwidth() // self.BLOCK_SIZE - 2):
                self.create_image(x, y, image=self.grass.image, anchor='nw')
                x += self.BLOCK_SIZE

            # RIGHT ROCK
            self.create_image(x, y, image=self.rock.image, anchor='nw')

            y += self.BLOCK_SIZE

        # LINE OF ROCKS
        x = 0
        for i in range(self.winfo_reqwidth() // self.BLOCK_SIZE):
            self.create_image(x, y, image=self.rock.image, anchor='nw')
            x += self.BLOCK_SIZE


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
