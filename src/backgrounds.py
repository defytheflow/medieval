import abc
import tkinter as tk

from config import BLOCK_SIZE
from sprites import Sprite


class Background(abc.ABC):

    @abc.abstractmethod
    def draw(self, canvas: tk.Canvas):
        pass


class GrassBackground(Background):

    def __init__(self):
        self._block_size: int = BLOCK_SIZE
        self._grass = Sprite(image_file='grass.png',
                             size=(self._block_size, self._block_size))
        self._stone = Sprite(image_file='stone.jpeg',
                             size=(self._block_size, self._block_size))

    def draw(self, canvas: tk.Canvas):
        x, y = 0, 0

        # LINE OF STONES
        for i in range(canvas.winfo_reqwidth() // self._block_size):
            canvas.create_image(x, y, image=self._stone.image, anchor='nw')
            x += self._block_size
        y += self._block_size

        # MIDDLE GRASS
        for i in range(canvas.winfo_reqheight() // self._block_size - 2):

            # LEFT STONE
            x = 0
            canvas.create_image(x, y, image=self._stone.image, anchor='nw')
            x += self._block_size

            # GRASS ROW
            for j in range(canvas.winfo_reqwidth() // self._block_size - 2):
                canvas.create_image(x, y, image=self._grass.image, anchor='nw')
                x += self._block_size

            # RIGHT STONE
            canvas.create_image(x, y, image=self._stone.image, anchor='nw')

            y += self._block_size

        # LINE OF STONES
        x = 0
        for i in range(canvas.winfo_reqwidth() // self._block_size):
            canvas.create_image(x, y, image=self._stone.image, anchor='nw')
            x += self._block_size
