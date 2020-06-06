import os
import tkinter as tk

import simpleaudio as sa

from config import (
    AssetsConfig,
)

from utils import create_photo_image


class Sprite:

    NO_CANVAS_ID = -1

    def __init__(self, name, canvas, position, size, direction = 'south', speed = 1):
        self.name = name
        self.canvas = canvas
        self.canvas.cache_sprite(self)
        self.size = size
        self.position = position
        self.direction = direction
        self.speed = speed
        self.canvas_id = self.NO_CANVAS_ID
        self.sleep_time = 10
        self.costume_num = 0
        self.image = None
        self.set_image(os.path.join(self.name, f'{self.direction}.png'))

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
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    @property
    def tags(self):
        return [self.name, self.__class__.__name__.lower()]

    def get_canvas_id(self):
        if self.canvas_id == self.NO_CANVAS_ID:
            raise AttributeError('canvas_id has not been initialized.')
        return self.canvas_id

    def set_canvas_id(self, canvas_id):
        self.canvas_id = canvas_id

    def set_image(self, image_file):
        self.image = create_photo_image(os.path.join(AssetsConfig.sprites, image_file), self.size)

    def set_position(self, new_position):
        self.position = new_position

    def set_direction(self, new_direction):
        if new_direction not in ('north', 'south', 'west', 'east'):
            raise ValueError(f"Invalid direction value '{new_direction}'")
        self.direction = new_direction
        self.set_image(os.path.join(self.name, f'{self.direction}.png'))

    def switch_costume(self):
        self.costume_num += 1
        if self.costume_num > 2:  # Why 2?
            self.costume_num = 1
        self.set_image(os.path.join(self.name, f'{self.direction}-{self.costume_num}.png'))

    def reset_costume(self):
        self.set_image(os.path.join(self.name, f'{self.direction}.png'))

    def draw_on_canvas(self):
        self.draw_on_canvas_at(self.x, self.y)

    def redraw_on_canvas(self):
        self.redraw_on_canvas_at(self.x, self.y)

    def draw_on_canvas_at(self, x, y):
        canvas_id = self.canvas.create_image(
            x, y, image=self.image, anchor='nw', tags=self.tags)
        self.set_canvas_id(canvas_id)

    def redraw_on_canvas_at(self, x, y):
        self.canvas.delete(self.get_canvas_id())
        self.draw_on_canvas_at(x, y)

    def move(self, direction):
        self.set_direction(direction)
        if direction == 'north':
            self.set_position((self.x, self.y - self.speed))
        elif direction == 'west':
            self.set_position((self.x - self.speed, self.y))
        elif direction == 'south':
            self.set_position((self.x, self.y + self.speed))
        elif direction == 'east':
            self.set_position((self.x + self.speed, self.y))
        self._animate_move(direction)
        self.reset_costume()
        self.redraw_on_canvas()

    def _animate_move(self, direction):
        print(self.x, self.y)
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
