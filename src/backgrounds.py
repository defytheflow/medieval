import abc
import tkinter as tk

from sprites import Sprite


class Background(abc.ABC):

    @abc.abstractmethod
    def draw(self):
        pass


class GrassBackground(Background):

    BLOCK_SIZE = 30

    def __init__(self):
        self._stone = Sprite(file='stone.jpeg',
                            size=(self.BLOCK_SIZE, self.BLOCK_SIZE))
        self._grass = Sprite(file='carpet.png',
                            size=(self.BLOCK_SIZE, self.BLOCK_SIZE))

    def draw(self, canvas):
        x, y = 0, 0

        # LINE OF STONES
        for i in range(canvas.winfo_reqwidth() // self.BLOCK_SIZE):
            canvas.create_image(x, y, image=self._stone.image, anchor='nw')
            x += self.BLOCK_SIZE
        y += self.BLOCK_SIZE

        # MIDDLE GRASS
        for i in range(canvas.winfo_reqheight() // self.BLOCK_SIZE - 2):

            # LEFT STONE
            x = 0
            canvas.create_image(x, y, image=self._stone.image, anchor='nw')
            x += self.BLOCK_SIZE

            # GRASS ROW
            for j in range(canvas.winfo_reqwidth() // self.BLOCK_SIZE - 2):
                canvas.create_image(x, y, image=self._grass.image, anchor='nw')
                x += self.BLOCK_SIZE

            # RIGHT STONE
            canvas.create_image(x, y, image=self._stone.image, anchor='nw')

            y += self.BLOCK_SIZE

        # LINE OF STONES
        x = 0
        for i in range(canvas.winfo_reqwidth() // self.BLOCK_SIZE):
            canvas.create_image(x, y, image=self._stone.image, anchor='nw')
            x += self.BLOCK_SIZE
