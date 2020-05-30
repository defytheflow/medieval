import os
import tkinter as tk

from typing import Tuple

from config import SPRITES_ROOT
from utils import create_photo_image


class Sprite:

    def __init__(self, image_file: str, size: Tuple[int, int]):
        self._size = size
        self._image = create_photo_image(os.path.join(SPRITES_ROOT, image_file), self._size)

    @property
    def size(self) -> Tuple[int, int]:
        return self._size

    @property
    def image(self) -> tk.PhotoImage:
        return self._image

    @image.setter
    def image(self, image_file: str) -> None:
        self._image = create_photo_image(os.path.join(SPRITES_ROOT, image_file), self._size)

    def width(self) -> int:
        return self._size[0]

    def height(self) -> int:
        return self._size[1]


class Character(Sprite):

    def __init__(self,
                 tag: str,
                 size: Tuple[int, int],
                 direction: str,
                 speed: int = 1):

        self._tag = tag
        self._direction = direction
        self._speed = speed
        self._costume_num = 0

        super().__init__(size=size, image_file=os.path.join(self._tag, f'{self._direction}.png'))

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def direction(self) -> str:
        return self._direction

    @direction.setter
    def direction(self, direction) -> None:
        if not direction in ('north', 'south', 'west', 'east'):
            raise ValueError(f'Invalid direction value {direction}')
        self._direction = direction
        self.image = os.path.join(self._tag, f'{self._direction}.png')

    @property
    def speed(self) -> int:
        return self._speed

    def switch_costume(self) -> None:
        self._costume_num += 1
        if self._costume_num > 2:  # Why 2?
            self._costume_num = 1
        self.image = os.path.join(self._tag, f'{self._direction}-{self._costume_num}.png')

    def reset_costume(self) -> None:
        self.image = os.path.join(self._tag, f'{self._direction}.png')

    def draw(self, canvas: tk.Canvas, x: int, y: int) -> None:
        self.id = canvas.create_image(x, y, image=self._image, anchor='nw', tags='character')

    def redraw(self, canvas: tk.Canvas, x: int, y: int) -> None:
        canvas.delete(self.id)
        self.id = canvas.create_image(x, y, image=self._image, anchor='nw', tags='character')
