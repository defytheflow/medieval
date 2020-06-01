import abc
import tkinter as tk

from sprites import Sprite
from canvases import GameCanvas


class Background(abc.ABC):

    @abc.abstractmethod
    def draw(self, canvas: tk.Canvas):
        pass


class VillageBackground(Background):

    def __init__(self, name: str, canvas: GameCanvas, block_size: int):
        self._name = name

        self._canvas = canvas
        self._canvas.add_background(self)

        self._block_size = block_size

        self._grass = Sprite(name='grass',
                             canvas=self._canvas,
                             image_file='grass.png',
                             size=(self._block_size, self._block_size))

        self._stone = Sprite(name='stone',
                             canvas=self._canvas,
                             image_file='stone.jpeg',
                             size=(self._block_size, self._block_size))

        self._tree = Sprite(name='tree',
                            canvas=self._canvas,
                            image_file='tree.png',
                            size=(self._block_size * 2, self._block_size * 2))

    @property
    def name(self) -> str:
        return self._name

    def draw(self):
        x, y = 0, 0

        # LINE OF STONES
        for i in range(self._canvas.winfo_reqwidth() // self._block_size):
            self._canvas.create_image(x, y, image=self._stone.image, anchor='nw')
            x += self._block_size
        y += self._block_size

        # MIDDLE GRASS
        for i in range(self._canvas.winfo_reqheight() // self._block_size - 2):

            # LEFT STONE
            x = 0
            self._canvas.create_image(x, y, image=self._stone.image, anchor='nw')
            x += self._block_size

            # GRASS ROW
            for j in range(self._canvas.winfo_reqwidth() // self._block_size - 2):
                self._canvas.create_image(x, y, image=self._grass.image, anchor='nw')
                x += self._block_size

            # RIGHT STONE
            self._canvas.create_image(x, y, image=self._stone.image, anchor='nw')

            y += self._block_size

        # LINE OF STONES
        x = 0
        for i in range(self._canvas.winfo_reqwidth() // self._block_size):
            self._canvas.create_image(x, y, image=self._stone.image, anchor='nw')
            x += self._block_size
