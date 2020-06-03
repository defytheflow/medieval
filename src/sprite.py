import os
import tkinter as tk
from typing import Tuple, List

import simpleaudio as sa

import config
from utils import create_photo_image


class Sprite:

    NO_CANVAS_ID = -1

    def __init__(self,
                 name: str,
                 canvas: 'GameCanvas',
                 position: Tuple[int, int],
                 size: Tuple[int, int],
                 direction: str = 'south',
                 speed: int = 1):

        self.name = name
        self._canvas = canvas
        self._canvas.cache_sprite(self)
        self._size = size
        self._position = position
        self._direction = direction
        self._speed = speed
        self._canvas_id = self.NO_CANVAS_ID
        self._sleep_time = 10
        self._costume_num = 0
        self._image = None
        self.set_image(os.path.join(self.name, f'{self._direction}.png'))

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"name='{self.name}', "
                f"direction='{self._direction}', "
                f"position={self._position}, "
                f"size={self._size}, "
                f"canvas_id={self._canvas_id}, "
                f"tags={self.get_tags()})")

    def get_name(self) -> str:
        return self.name

    def get_direction(self) -> str:
        return self._direction

    def get_x(self) -> int:
        return self._position[0]

    def get_y(self) -> int:
        return self._position[1]

    def get_width(self) -> int:
        return self._size[0]

    def get_height(self) -> int:
        return self._size[1]

    def get_speed(self) -> int:
        return self._speed

    def get_image(self) -> tk.PhotoImage:
        return self._image

    def get_tags(self) -> List[str]:
        return [self.name, self.__class__.__name__.lower()]

    def get_size(self) -> Tuple[int, int]:
        return self._size

    def get_position(self) -> Tuple[int, int]:
        return self._position

    def get_canvas_id(self) -> int:
        if self._canvas_id == self.NO_CANVAS_ID:
            raise AttributeError('canvas_id has not been initialized.')
        return self._canvas_id

    def set_canvas_id(self, canvas_id: int) -> None:
        self._canvas_id = canvas_id

    def set_image(self, image_file: str) -> None:
        self._image = create_photo_image(os.path.join(config.SPRITES_ROOT, image_file), self._size)

    def set_position(self, new_position: Tuple[int, int]) -> None:
        self._position = new_position

    def set_direction(self, new_direction: str) -> None:
        if new_direction not in ('north', 'south', 'west', 'east'):
            raise ValueError(f"Invalid direction value '{new_direction}'")
        self._direction = new_direction
        self.set_image(os.path.join(self.name, f'{self._direction}.png'))

    def switch_costume(self) -> None:
        self._costume_num += 1
        if self._costume_num > 2:  # Why 2?
            self._costume_num = 1
        self.set_image(os.path.join(self.name, f'{self._direction}-{self._costume_num}.png'))

    def reset_costume(self) -> None:
        self.set_image(os.path.join(self.name, f'{self._direction}.png'))

    def draw_on_canvas(self) -> None:
        self.draw_on_canvas_at(self.get_x(), self.get_y())

    def redraw_on_canvas(self) -> None:
        self.redraw_on_canvas_at(self.get_x(), self.get_y())

    def draw_on_canvas_at(self, x: int, y: int) -> None:
        canvas_id = self._canvas.create_image(
            x, y, image=self._image, anchor='nw', tags=self.get_tags())
        self.set_canvas_id(canvas_id)

    def redraw_on_canvas_at(self, x: int, y: int) -> None:
        self._canvas.delete(self.get_canvas_id())
        self.draw_on_canvas_at(x, y)

    def move(self, direction: str) -> None:
        self.set_direction(direction)
        if direction == 'north':
            self.set_position((self.get_x(), self.get_y() - self.get_width()))
        elif direction == 'west':
            self.set_position((self.get_x() - self.get_width(), self.get_y()))
        elif direction == 'south':
            self.set_position((self.get_x(), self.get_y() + self.get_width()))
        elif direction == 'east':
            self.set_position((self.get_x() + self.get_width(), self.get_y()))
        self._animate_move(direction)
        self.reset_costume()
        self.redraw_on_canvas()

    def _animate_move(self, direction: str) -> None:
        wave_obj = sa.WaveObject.from_wave_file(os.path.join(config.SOUNDS_ROOT, 'grass-move.wav'))
        play_obj = wave_obj.play()

        for i in range(1, self.get_width() + 1, self.get_speed()):
            self.switch_costume()
            if direction == 'north':
                self.redraw_on_canvas_at(self.get_x(), self.get_y() + self.get_width() - i)
            elif direction == 'west':
                self.redraw_on_canvas_at(self.get_x() + self.get_width() - i, self.get_y())
            elif direction == 'south':
                self.redraw_on_canvas_at(self.get_x(), self.get_y() - self.get_width() + i)
            elif direction == 'east':
                self.redraw_on_canvas_at(self.get_x() - self.get_width() + i, self.get_y())
            self._canvas.after(self._sleep_time)
            self._canvas.update()

        play_obj.stop()
