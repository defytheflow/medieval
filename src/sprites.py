import os

import config
import utils


class Sprite:

    def __init__(self, file, size):
        self._size = size
        self._image = utils.create_photo_image(
            os.path.join(config.SPRITES_ROOT, file), size)

    @property
    def size(self) -> int:
        return self._size

    @property
    def image(self) -> 'tk.PhotoImage':
        return self._image

    @image.setter
    def image(self, file):
        self._image = utils.create_photo_image(
            os.path.join(config.SPRITES_ROOT, file), self._size)


class Character(Sprite):

    def __init__(self, name, size, direction=''):
        self._name = name
        self._direction = direction if direction else 'south'
        super().__init__(size=size,
                         file=os.path.join(self._name, f'{self._direction}.png'))

    @property
    def direction(self) -> str:
        return self._direction

    @direction.setter
    def direction(self, direction):
        if not direction in ('north', 'south', 'west', 'east'):
            raise ValueError(f'Invalid direction value {direction}')
        self._direction = direction
        self.image = os.path.join(self._name, f'{self._direction}.png')
