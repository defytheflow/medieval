import os
import tkinter as tk

from typing import Tuple

import config
from utils import create_photo_image


class Sprite:

    def __init__(self,
                 name: str,
                 image_file: str,
                 size: Tuple[int, int]):

        self._name = name
        self._size = size
        self._image = create_photo_image(os.path.join(config.SPRITES_ROOT, image_file), self._size)

    @property
    def name(self) -> str:
        return self._name

    @property
    def size(self) -> Tuple[int, int]:
        return self._size

    @property
    def image(self) -> tk.PhotoImage:
        return self._image

    @property
    def width(self) -> int:
        return self._size[0]

    @property
    def height(self) -> int:
        return self._size[1]

    @image.setter
    def image(self, image_file: str) -> None:
        self._image = create_photo_image(os.path.join(config.SPRITES_ROOT, image_file), self._size)



class Character(Sprite):

    def __init__(self,
                 name: str,
                 size: Tuple[int, int],
                 direction: str,
                 speed: int = 1):

        self._name = name
        self._direction = direction
        self._speed = speed
        self._costume_num = 0

        super().__init__(name=name,
                         size=size,
                         image_file=os.path.join(self._name, f'{self._direction}.png'))

    @property
    def direction(self) -> str:
        return self._direction

    @property
    def speed(self) -> int:
        return self._speed

    @direction.setter
    def direction(self, direction: str) -> None:
        if not direction in ('north', 'south', 'west', 'east'):
            raise ValueError(f'Invalid direction value {direction}')
        self._direction = direction
        self.image = os.path.join(self._name, f'{self._direction}.png')

    def switch_costume(self) -> None:
        self._costume_num += 1
        if self._costume_num > 2:  # Why 2?
            self._costume_num = 1
        self.image = os.path.join(self._name, f'{self._direction}-{self._costume_num}.png')

    def reset_costume(self) -> None:
        self.image = os.path.join(self._name, f'{self._direction}.png')

    def draw(self, canvas: tk.Canvas, x: int, y: int) -> None:
        self.id = canvas.create_image(x, y, image=self._image, anchor='nw', tags='character')

    def redraw(self, canvas: tk.Canvas, x: int, y: int) -> None:
        canvas.delete(self.id)
        self.id = canvas.create_image(x, y, image=self._image, anchor='nw', tags='character')
