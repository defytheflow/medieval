import os

import config
import utils


class Sprite:

    def __init__(self, file, size):
        self._size = size
        self._image = utils.create_photo_image(
            os.path.join(config.SPRITES_PATH, file), size)

    @property
    def size(self) -> int:
        return self._size

    @property
    def image(self) -> 'tk.PhotoImage':
        return self._image

    @image.setter
    def image(self, file):
        self._image = utils.create_photo_image(
            os.path.join(config.SPRITES_PATH, file), self._size)
