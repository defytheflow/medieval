import os

import config
import utils

from sprite import Sprite


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
