import abc
import tkinter as tk
from typing import Dict

from sprites import Sprite


class Background(abc.ABC):

    @abc.abstractmethod
    def draw_on_canvas(self, canvas: tk.Canvas):
        pass


class VillageBackground(Background):

    def __init__(self, name: str, canvas, block_size: int):
        self._name = name
        self._canvas = canvas
        self._block_size = block_size
        self._sprites = {}  # type: Dict[str, Sprite]

        self._sprites['grass'] = Sprite(
            name='grass',
            canvas=canvas,
            image_file='grass.png',
            size=(block_size, block_size))

        self._sprites['stone'] = Sprite(
            name='stone',
            canvas=canvas,
            image_file='stone.jpeg',
            size=(block_size, block_size))

        self._sprites['tree'] = Sprite(
            name='tree',
            canvas=canvas,
            image_file='tree.png',
            size=(block_size * 2, block_size * 2))

    # Overrides Background.
    def draw_on_canvas(self):
        x, y = 0, 0

        # LINE OF STONES
        for i in range(self._canvas.winfo_reqwidth() // self._block_size):
            self._sprites['stone'].draw_on_canvas(x, y)
            x += self._block_size
        y += self._block_size

        # MIDDLE GRASS
        for i in range(self._canvas.winfo_reqheight() // self._block_size - 2):

            # LEFT STONE
            x = 0
            self._sprites['stone'].draw_on_canvas(x, y)
            x += self._block_size

            # GRASS ROW
            for j in range(self._canvas.winfo_reqwidth() // self._block_size - 2):
                self._sprites['grass'].draw_on_canvas(x, y)
                x += self._block_size

            # RIGHT STONE
            self._sprites['stone'].draw_on_canvas(x, y)
            y += self._block_size

        # LINE OF STONES
        x = 0
        for i in range(self._canvas.winfo_reqwidth() // self._block_size):
            self._sprites['stone'].draw_on_canvas(x, y)
            x += self._block_size
