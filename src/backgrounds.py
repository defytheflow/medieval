import os
import abc
import tkinter as tk
from typing import Dict

import config
from utils import create_photo_image
from canvases import GameCanvas


class Background(abc.ABC):

    @abc.abstractmethod
    def draw_on_game_canvas(self, game_canvas: GameCanvas) -> None:
        pass


class VillageBackground(Background):

    def __init__(self, block_size: int):
        self._block_size = block_size

        self._images = {}  # type: Dict[str, tk.PhotoImage]
        for image_name in ('grass', 'stone', 'tree'):
            image_file = os.path.join(config.SPRITES_ROOT, f'{image_name}.png')
            self._images[image_name] = create_photo_image(image_file, (block_size, block_size))

    # Overrides Background.
    def draw_on_game_canvas(self, game_canvas: GameCanvas) -> None:
        for name, image in self._images.items():
            game_canvas.add_image(name, image)

        x, y = 0, 0

        # LINE OF STONES
        for i in range(game_canvas.winfo_reqwidth() // self._block_size):
            game_canvas.create_image(x, y, image=self._images['stone'], anchor='nw', tags=['stone'])
            x += self._block_size
        y += self._block_size

        # MIDDLE GRASS
        for i in range(game_canvas.winfo_reqheight() // self._block_size - 2):

            # LEFT STONE
            x = 0
            game_canvas.create_image(x, y, image=self._images['stone'], anchor='nw', tags=['stone'])
            x += self._block_size

            # GRASS ROW
            for j in range(game_canvas.winfo_reqwidth() // self._block_size - 2):
                game_canvas.create_image(x, y, image=self._images['grass'], anchor='nw', tags=['grass'])
                x += self._block_size

            # RIGHT STONE
            game_canvas.create_image(x, y, image=self._images['stone'], anchor='nw', tags=['stone'])
            y += self._block_size

        # LINE OF STONES
        x = 0
        for i in range(game_canvas.winfo_reqwidth() // self._block_size):
            game_canvas.create_image(x, y, image=self._images['stone'], anchor='nw', tags=['stone'])
            x += self._block_size
