import os
import tkinter as tk

import simpleaudio as sa

from config import AssetsConfig
from geometry import Position
from utils import create_photo_image


class Sprite:

    NO_CANVAS_ID = -1

    def __init__(self, name, canvas, size, position, direction='south', speed=1):
        self.name = name
        self.canvas = canvas
        self.canvas.cache_sprite(self)
        self.size = size
        self._position = position
        self._direction = direction
        self._speed = speed
        self.image = os.path.join(self.name, f'{self.direction}.png')
        self.sleep_time = 10
        self.costume_num = 0
        self._canvas_id = self.NO_CANVAS_ID

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"name='{self.name}', "
                f"direction='{self.direction}', "
                f"position={self.position}, "
                f"size={self.size}, "
                f"canvas_id={self.canvas_id}, "
                f"tags={self.get_tags()})")

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    @property
    def width(self):
        return self.size.width

    @property
    def height(self):
        return self.size.height

    @property
    def tags(self):
        return [self.name, self.__class__.__name__.lower()]

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        self._speed = new_speed

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image_file):
        self._image = create_photo_image(os.path.join(AssetsConfig.sprites, image_file), self.size)

    @property
    def canvas_id(self):
        if self._canvas_id == self.NO_CANVAS_ID:
            raise AttributeError('canvas_id has not been initialized.')
        return self._canvas_id

    @canvas_id.setter
    def canvas_id(self, canvas_id):
        self._canvas_id = canvas_id

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        if not isinstance(new_position, Position):
            raise TypeError(f'Argument must be of type {Position}.')
        if new_position.x > self.canvas.width - self.width or \
           new_position.y > self.canvas.height - self.height:
            raise ValueError(f'Position of the canvas.')
        self._position = new_position

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, new_direction):
        if new_direction not in ('north', 'south', 'west', 'east'):
            raise ValueError(f"Invalid direction '{new_direction}'")
        self._direction = new_direction
        self.image = os.path.join(self.name, f'{self.direction}.png')

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
            self.position = Position(self.x, self.y - self.speed)
        elif direction == 'west':
            self.position = Position(self.x - self.speed, self.y)
        elif direction == 'south':
            self.position = Position(self.x, self.y + self.speed)
        elif direction == 'east':
            self.position = Position(self.x + self.speed, self.y)
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
