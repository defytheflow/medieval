import os
import tkinter as tk

from typing import Tuple, List

import config
from utils import create_photo_image


class Sprite:

    NO_CANVAS_ID = -1

    def __init__(self,
                 name: str,
                 canvas,
                 size: Tuple[int, int],
                 direction: str = 'south',
                 speed: int = 1):

        image_file=os.path.join(config.SPRITES_ROOT, name, f'{direction}.png')

        self._name = name
        self._canvas = canvas
        self._canvas.add_sprite(self)
        self._canvas_id = self.NO_CANVAS_ID   # type: int
        self._size = size
        self._image = create_photo_image(image_file, size)
        self._direction = direction
        self._speed = speed
        self._costume_num = 0

    def __repr__(self):
        return (f"{self.__class__.__name__}(name='{self._name}', size={self._size}, "
                f"canvas_id={self._canvas_id}, tags={self.get_tags()})")

    def get_name(self) -> str:
        return self._name

    def get_tags(self) -> List[str]:
        return [self._name, self.__class__.__name__.lower()]

    def get_canvas_id(self) -> int:
        if self._canvas_id == self.NO_CANVAS_ID:
            raise AttributeError('canvas_id has not been initialized.')
        return self._canvas_id

    def get_size(self) -> Tuple[int, int]:
        return self._size

    def get_image(self) -> tk.PhotoImage:
        return self._image

    def get_width(self) -> int:
        return self._size[0]

    def get_height(self) -> int:
        return self._size[1]

    def get_direction(self) -> str:
        return self._direction

    def get_speed(self) -> int:
        return self._speed

    def set_canvas_id(self, canvas_id: int) -> None:
        self._canvas_id = canvas_id

    def set_image(self, image_file: str) -> None:
        self._image = create_photo_image(os.path.join(config.SPRITES_ROOT, image_file), self._size)

    def set_direction(self, new_direction: str) -> None:
        if not new_direction in ('north', 'south', 'west', 'east'):
            raise ValueError(f'Invalid direction value {new_direction}')
        self._direction = new_direction
        self.set_image(os.path.join(self._name, f'{self._direction}.png'))

    def draw_on_canvas(self, x: int, y: int) -> None:
        canvas_id = self._canvas.create_image(x, y, image=self._image, anchor='nw', tags=self.get_tags())
        self.set_canvas_id(canvas_id)

    def redraw_on_canvas(self, x: int, y: int) -> None:
        self._canvas.delete(self.get_canvas_id())
        self.draw_on_canvas(x, y)

    def switch_costume(self) -> None:
        self._costume_num += 1
        if self._costume_num > 2:  # Why 2?
            self._costume_num = 1
        self.set_image(os.path.join(self._name, f'{self._direction}-{self._costume_num}.png'))

    def reset_costume(self) -> None:
        self.set_image(os.path.join(self._name, f'{self._direction}.png'))
