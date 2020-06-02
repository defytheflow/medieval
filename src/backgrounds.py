import os
import abc
import random
import tkinter as tk

from typing import Dict

import config
from utils import create_photo_image

from canvases import GameCanvas


class Background(abc.ABC):

    @abc.abstractmethod
    def draw_on_canvas(self, canvas: GameCanvas) -> None:
        pass


class VillageBackground(Background):

    def __init__(self, block_size: int):
        self._block_size = block_size
        self._images: Dict[str, tk.PhotoImage] = {}

        for name in ('bridge', 'coast-rock', 'grass', 'road', 'water'):
            file = os.path.join(config.BG_ROOT, f'{name}.png')
            self._images[name] = create_photo_image(file, (block_size, block_size))

        file = os.path.join(config.BG_ROOT, 'tree.png')
        self._images['tree'] = create_photo_image(file, (block_size * 2, block_size * 2))

    # Overrides Background.
    def draw_on_canvas(self, canvas: GameCanvas) -> None:
        for name, image in self._images.items():
            canvas.add_image(name, image)

        self._draw_grass(canvas)
        self._draw_trees(canvas)
        self._draw_river(canvas)
        self._draw_bridge(canvas)
        self._draw_road(canvas)
        self._draw_lake(canvas)
        self._draw_houses(canvas)

    def _draw_image(self, canvas, col, row, image, tags):
        canvas.create_image(col * self._block_size,
                            row * self._block_size,
                            image=image,
                            anchor='nw',
                            tags=tags)

    def _draw_rectangle(self, canvas, col, row, fill, tags):
        canvas.create_rectangle(col * self._block_size,
                                row * self._block_size,
                                col * self._block_size + self._block_size,
                                row * self._block_size + self._block_size,
                                fill=fill,
                                tags=tags)

    def _draw_houses(self, canvas):
        # Upper houses.
        for col in range(14, 18):
            for row in range(4, 7):
                self._draw_rectangle(canvas, col, row, 'magenta', ['house', 'bg'])
        self._draw_image(canvas, 15, 7, self._images['road'], ['road', 'bg'])

        for col in range(20, 24):
            for row in range(4, 7):
                self._draw_rectangle(canvas, col, row, 'magenta', ['house', 'bg'])
        self._draw_image(canvas, 21, 7, self._images['road'], ['road', 'bg'])

        for col in range(26, 30):
            for row in range(4, 7):
                self._draw_rectangle(canvas, col, row, 'magenta', ['house', 'bg'])
        self._draw_image(canvas, 27, 7, self._images['road'], ['road', 'bg'])

        # Lower houses.
        for col in range(17, 21):
            for row in range(11, 14):
                self._draw_rectangle(canvas, col, row, 'magenta', ['house', 'bg'])
        self._draw_image(canvas, 18, 10, self._images['road'], ['road', 'bg'])

        for col in range(23, 27):
            for row in range(11, 14):
                self._draw_rectangle(canvas, col, row, 'magenta', ['house', 'bg'])
        self._draw_image(canvas, 24, 10, self._images['road'], ['road', 'bg'])

    def _draw_grass(self, canvas):
        for col in range(36):
            for row in range(24):
                self._draw_image(canvas, col, row, self._images['grass'],
                                 ['grass', 'bg'])

    def _draw_river(self, canvas):
        for col in range(6, 11):
            for row in range(0, 19):
                self._draw_image(canvas, col, row, self._images['water'],
                                 ['water', 'river', 'bg'])

        # River coast.
        for col in range(6, 7):
            for row in range(0, 19):
                self._draw_image(canvas, col, row, self._images['coast-rock'],
                                 ['coast-rock', 'river', 'bg'])
        for col in range(10, 11):
            for row in range(0, 19):
                self._draw_image(canvas, col, row, self._images['coast-rock'],
                                 ['coast-rock', 'river', 'bg'])

    def _draw_bridge(self, canvas):
        for col in range(6, 11):
            for row in range(8, 10):
                self._draw_image(canvas, col, row, self._images['bridge'],
                                 ['bridge', 'bg'])

    def _draw_road(self, canvas):
        # Before bridge vertical.
        for col in range(0, 2):
            for row in range(0, 10):
                self._draw_image(canvas, col, row, self._images['road'],
                                 ['road', 'bg'])

        # Before bridge horizontal.
        for col in range(2, 6):
            for row in range(8, 10):
                self._draw_image(canvas, col, row, self._images['road'],
                                 ['road', 'bg'])

        # Parallel house horizontal.
        for col in range(11, 31):
            for row in range(8, 10):
                self._draw_image(canvas, col, row, self._images['road'],
                                 ['road', 'bg'])

        # Parallel river vertical.
        for col in range(12, 14):
            for row in range(10, 18):
                self._draw_image(canvas, col, row, self._images['road'],
                                 ['road', 'bg'])

        # Before lake horizontal.
        for col in range(14, 32):
            for row in range(16, 18):
                self._draw_image(canvas, col, row, self._images['road'],
                                 ['road', 'bg'])

    def _draw_tree_image(self, canvas, col, row):
        canvas.create_image(col * self._block_size,
                            row * self._block_size,
                            image=self._images['tree'],
                            anchor='nw',
                            tags=['tree', 'bg'])

    def _draw_trees(self, canvas):
        for col in range(14, 31):
            for row in range(0, 3):
                if random.randint(0, 1) == 1:
                    self._draw_tree_image(canvas, col, row)


    def _draw_lake(self, canvas):
        for col in range(18, 30):
            for row in range(19, 24):
                self._draw_image(canvas, col, row, self._images['water'],
                                 ['water', 'lake', 'bg'])

        # Left coast rock,
        for col in range(18, 19):
            for row in range(20, 23):
                self._draw_image(canvas, col, row, self._images['coast-rock'],
                                 ['coast-rock', 'lake', 'bg'])

        # Right coast rock.
        for col in range(29, 30):
            for row in range(20, 23):
                self._draw_image(canvas, col, row, self._images['coast-rock'],
                                 ['coast-rock', 'lake', 'bg'])

        # Top coast rock.
        for col in range(19, 29):
            for row in range(19, 20):
                self._draw_image(canvas, col, row, self._images['coast-rock'],
                                 ['coast-rock', 'lake', 'bg'])

        # Bottom coast rock.
        for col in range(19, 29):
            for row in range(23, 24):
                self._draw_image(canvas, col, row, self._images['coast-rock'],
                                 ['coast-rock', 'lake', 'bg'])

        # Grass corners.
        self._draw_image(canvas, 18, 19, self._images['grass'], ['grass', 'bg'])
        self._draw_image(canvas, 29, 19, self._images['grass'], ['grass', 'bg'])
        self._draw_image(canvas, 18, 23, self._images['grass'], ['grass', 'bg'])
        self._draw_image(canvas, 29, 23, self._images['grass'], ['grass', 'bg'])
