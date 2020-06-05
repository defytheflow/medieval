import os
import abc
import random
import tkinter as tk

from config import (
    AssetsConfig,
)

from utils import (
    create_photo_image,
)


def delete_overlapping(canvas, pos1, pos2):
    for item in canvas.find_overlapping(*pos1, *pos2):
        canvas.delete(item)


class Background(abc.ABC):

    @abc.abstractmethod
    def draw_on_canvas(self, canvas):
        pass


class VillageBackground(Background):

    def __init__(self, block_size):
        self.block_size = block_size
        self.images = self.create_images({  # <- Add new backgrounds here.
                'bridge': (block_size, block_size),
                 'coast': (block_size, block_size),
                 'grass': (block_size, block_size),
                  'road': (block_size, block_size),
                 'water': (block_size, block_size),
                  'tree': (block_size * 2, block_size * 2),
        })

    def cache_images(self, canvas):
        for name, image in self.images.items():
            canvas.cache_image(name, image)

    def draw_on_canvas(self, canvas):
        ' Overrides Background. '
        self.cache_images(canvas)

        self.draw_grass(canvas)
        self.draw_river(canvas)
        self.draw_bridge(canvas)
        self.draw_road(canvas)
        self.draw_lake(canvas)
        self.draw_houses(canvas)
        self.draw_trees(canvas)


    def draw_grass(self, canvas):
        for x in range(0, 36 * self.block_size, self.block_size):
            for y in range(0, 24 * self.block_size, self.block_size):
                canvas.create_image(x, y, image=self.images['grass'],
                                    anchor='nw', tags=['grass'])


    def draw_river(self, canvas):
        # River
        for col in range(6 * self.block_size, 11 * self.block_size, self.block_size):
            x = col * self.block_size
            for row in range(0, 19):
                y = row * self.block_size
                delete_overlapping(canvas, (x, y), (x + self.block_size, y + self.block_size))
                canvas.create_image(x, y, image=self.images['water'], anchor='nw', tags=['water'])

        # Left coast.
        for col in range(6, 7):
            x = col * self.block_size
            for row in range(0, 19):
                y = row * self.block_size
                canvas.create_image(x, y, image=self.images['coast'], anchor='nw', tags=['coast'])

        # Right coast.
        for col in range(10, 11):
            x = col * self.block_size
            for row in range(0, 19):
                y = row * self.block_size
                canvas.create_image(x, y, image=self.images['coast'], anchor='nw', tags=['coast'])

    def draw_trees(self, canvas):
        for col in range(14, 31):
            for row in range(0, 3):
                if random.randint(0, 1):
                    self._draw_tree_image(canvas, col, row)

    def _draw_image(self, canvas, col, row, image, tags):
        canvas.create_image(col * self.block_size,
                            row * self.block_size,
                            image=image,
                            anchor='nw',
                            tags=tags)

    def _draw_rectangle(self, canvas, col, row, fill, tags):
        canvas.create_rectangle(col * self.block_size,
                                row * self.block_size,
                                col * self.block_size + self.block_size,
                                row * self.block_size + self.block_size,
                                fill=fill,
                                tags=tags)


    def delete_overlapping_items(self, canvas, col, row):
        overlap_items = canvas.find_overlapping(col * self.block_size,
                                                row * self.block_size,
                                                col * self.block_size + self.block_size,
                                                row * self.block_size + self.block_size)
        for item in overlap_items:
            canvas.delete(item)

    def _draw_tree_image(self, canvas, col, row):
        canvas.create_image(col * self.block_size,
                            row * self.block_size,
                            image=self.images['tree'],
                            anchor='nw',
                            tags=['tree', 'bg'])


    def draw_bridge(self, canvas):
        for col in range(6, 11):
            x = col * self.block_size
            for row in range(8, 10):
                y = row * self.block_size
                delete_overlapping(canvas, (x, y), (x + self.block_size, y + self.block_size))
                canvas.create_image(x, y, image=self.images['bridge'], anchor='nw', tags=['bridge'])



    def draw_houses(self, canvas):
        # upper houses.
        for col in range(14, 18):
            for row in range(4, 7):
                # self.delete_overlapping_items(canvas, col, row)
                self._draw_rectangle(canvas, col, row, 'magenta', ['house', 'bg'])

        # self.delete_overlapping_items(canvas, 15, 7)
        self._draw_image(canvas, 15, 7, self.images['road'], ['road', 'bg'])

        for col in range(20, 24):
            for row in range(4, 7):
                # self.delete_overlapping_items(canvas, col, row)
                self._draw_rectangle(canvas, col, row, 'magenta', ['house', 'bg'])

        # self.delete_overlapping_items(canvas, 21, 7)
        self._draw_image(canvas, 21, 7, self.images['road'], ['road', 'bg'])

        for col in range(26, 30):
            for row in range(4, 7):
                # self.delete_overlapping_items(canvas, col, row)
                self._draw_rectangle(canvas, col, row, 'magenta', ['house', 'bg'])

        # self.delete_overlapping_items(canvas, 27, 7)
        self._draw_image(canvas, 27, 7, self.images['road'], ['road', 'bg'])

        # lower houses.
        for col in range(17, 21):
            for row in range(11, 14):
                # self.delete_overlapping_items(canvas, col, row)
                self._draw_rectangle(canvas, col, row, 'magenta', ['house', 'bg'])

        # self.delete_overlapping_items(canvas, 18, 10)
        self._draw_image(canvas, 18, 10, self.images['road'], ['road', 'bg'])

        for col in range(23, 27):
            for row in range(11, 14):
                # self.delete_overlapping_items(canvas, col, row)
                self._draw_rectangle(canvas, col, row, 'magenta', ['house', 'bg'])

        # self.delete_overlapping_items(canvas, 24, 10)
        self._draw_image(canvas, 24, 10, self.images['road'], ['road', 'bg'])

    def draw_road(self, canvas):
        # Before bridge vertical.
        for col in range(0, 2):
            for row in range(0, 10):
                self.delete_overlapping_items(canvas, col, row)
                self._draw_image(canvas, col, row, self.images['road'], ['road', 'bg'])

        # Before bridge horizontal.
        for col in range(2, 6):
            for row in range(8, 10):
                self.delete_overlapping_items(canvas, col, row)
                self._draw_image(canvas, col, row, self.images['road'], ['road', 'bg'])

        # Parallel house horizontal.
        for col in range(11, 31):
            for row in range(8, 10):
                self.delete_overlapping_items(canvas, col, row)
                self._draw_image(canvas, col, row, self.images['road'], ['road', 'bg'])

        # Parallel river vertical.
        for col in range(12, 14):
            for row in range(10, 18):
                self.delete_overlapping_items(canvas, col, row)
                self._draw_image(canvas, col, row, self.images['road'], ['road', 'bg'])

        # Before lake horizontal.
        for col in range(14, 32):
            for row in range(16, 18):
                self.delete_overlapping_items(canvas, col, row)
                self._draw_image(canvas, col, row, self.images['road'], ['road', 'bg'])


    def draw_lake(self, canvas):
        for col in range(18, 30):
            for row in range(19, 24):
                self.delete_overlapping_items(canvas, col, row)
                self._draw_image(canvas, col, row, self.images['water'], ['water', 'lake', 'bg'])

        # Left coast.
        for col in range(18, 19):
            for row in range(20, 23):
                self._draw_image(canvas, col, row, self.images['coast'], ['coast'])

        # Right coast.
        for col in range(29, 30):
            for row in range(20, 23):
                self._draw_image(canvas, col, row, self.images['coast'], ['coast'])

        # Top coast.
        for col in range(19, 29):
            for row in range(19, 20):
                self._draw_image(canvas, col, row, self.images['coast'], ['coast'])

        # Bottom coast.
        for col in range(19, 29):
            for row in range(23, 24):
                self._draw_image(canvas, col, row, self.images['coast'], ['coast'])

        # Grass corners.
        self.delete_overlapping_items(canvas, 18, 19)
        self._draw_image(canvas, 18, 19, self.images['grass'], ['grass', 'bg'])

        self.delete_overlapping_items(canvas, 29, 19)
        self._draw_image(canvas, 29, 19, self.images['grass'], ['grass', 'bg'])

        self.delete_overlapping_items(canvas, 18, 23)
        self._draw_image(canvas, 18, 23, self.images['grass'], ['grass', 'bg'])

        self.delete_overlapping_items(canvas, 29, 23)
        self._draw_image(canvas, 29, 23, self.images['grass'], ['grass', 'bg'])

    @staticmethod
    def create_images(bg_dict):
        return {
            name: create_photo_image(os.path.join(AssetsConfig.bg, f'{name}.png'), size)
            for name, size in bg_dict.items()
        }
