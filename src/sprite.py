import os
import tkinter as tk

import simpleaudio as sa

from config import AssetsConfig
from geometry import Position
from geometry import Oriented, Movable, Positionable, Rectangular
from utils import create_photo_image


class Sprite(Movable, Oriented, Positionable, Rectangular):

    NO_CANVAS_ID = -1

    def __init__(self, name, canvas, dimension, position, direction='south', speed=1):
        Oriented.__init__(self, direction)
        Movable.__init__(self, speed)
        Positionable.__init__(self, position)
        Rectangular.__init__(self, dimension)

        self.name = name
        self._image = create_photo_image(os.path.join(AssetsConfig.sprites, self.name, f'{self.direction}.png'),
                                         self.dimension)

        self.canvas = canvas
        self.canvas.save_sprite(self)
        self._canvas_id = self.NO_CANVAS_ID

        self.sleep_time = 10
        self.costume_num = 0

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"name='{self.name}', "
                f"{self.direction}, "
                f"{self.position}, "
                f"{self.dimension}, "
                f"canvas_id={self.canvas_id}, "
                f"tags={self.get_tags()})")

    @property
    def tags(self):
        return [self.name, self.__class__.__name__.lower()]

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image_file):
        self._image = create_photo_image(os.path.join(AssetsConfig.sprites, image_file), self.dimension)

    @property
    def canvas_id(self):
        if self._canvas_id == self.NO_CANVAS_ID:
            raise AttributeError('canvas_id has not been initialized.')
        return self._canvas_id

    @canvas_id.setter
    def canvas_id(self, canvas_id):
        self._canvas_id = canvas_id

    def switch_costume(self):
        self.costume_num += 1
        if self.costume_num > 2:  # Why 2?
            self.costume_num = 1
        self.image = os.path.join(self.name, f'{self.direction}-{self.costume_num}.png')

    def reset_costume(self):
        self.image = os.path.join(self.name, f'{self.direction}.png')

    def draw_on_canvas(self):
        self.draw_on_canvas_at(self.x, self.y)

    def redraw_on_canvas(self):
        self.redraw_on_canvas_at(self.x, self.y)

    def draw_on_canvas_at(self, x, y):
        self.canvas_id = self.canvas.create_image(x, y, image=self.image, anchor='nw', tags=self.tags)

    def redraw_on_canvas_at(self, x, y):
        self.canvas.delete(self.canvas_id)
        self.draw_on_canvas_at(x, y)

    def move(self, direction):
        self.direction = direction
        if direction == 'north':
            self.position = (self.x, self.y - self.speed)
        elif direction == 'west':
            self.position = (self.x - self.speed, self.y)
        elif direction == 'south':
            self.position = (self.x, self.y + self.speed)
        elif direction == 'east':
            self.position = (self.x + self.speed, self.y)
        self._animate_move(direction)
        self.reset_costume()
        self.redraw_on_canvas()

    def _animate_move(self, direction):
        wave_obj = sa.WaveObject.from_wave_file(os.path.join(AssetsConfig.sounds, 'grass-move.wav'))
        play_obj = wave_obj.play()

        for i in range(1, self.speed + 1, self.speed):
            self.switch_costume()
            if direction == 'north':
                self.redraw_on_canvas_at(self.x, self.y + self.speed - i)
            elif direction == 'west':
                self.redraw_on_canvas_at(self.x + self.speed - i, self.y)
            elif direction == 'south':
                self.redraw_on_canvas_at(self.x, self.y - self.speed + i)
            elif direction == 'east':
                self.redraw_on_canvas_at(self.x - self.speed + i, self.y)
            self.canvas.after(self.sleep_time)
            self.canvas.update()

        play_obj.stop()

        # if new_position.x > self.canvas.width - self.width or \
        #    new_position.y > self.canvas.height - self.height:
        #     raise ValueError(f'Position of the canvas.')
