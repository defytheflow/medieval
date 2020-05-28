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

    def width(self) -> int:
        return self._size[0]

    def height(self) -> int:
        return self._size[1]

    @property
    def image(self) -> 'tk.PhotoImage':
        return self._image

    @image.setter
    def image(self, file):
        self._image = utils.create_photo_image(
            os.path.join(config.SPRITES_ROOT, file), self._size)


class Character(Sprite):

    def __init__(self, name, size, direction, speed=1):
        self._name = name
        self._direction = direction
        self._speed = speed
        self._costume_num = 0
        super().__init__(size=size,
                         file=os.path.join(self._name, f'{self._direction}.png'))

    @property
    def name(self) -> str:
        return self._name

    @property
    def direction(self) -> str:
        return self._direction

    @direction.setter
    def direction(self, direction):
        if not direction in ('north', 'south', 'west', 'east'):
            raise ValueError(f'Invalid direction value {direction}')
        self._direction = direction
        self.image = os.path.join(self._name, f'{self._direction}.png')

    @property
    def speed(self) -> int:
        return self._speed

    def switch_costume(self):
        self._costume_num += 1

        if self._costume_num > 2:
            self._costume_num = 1

        self.image = os.path.join(
            self._name, f'{self._direction}-{self._costume_num}.png')

    def reset_costume(self):
        self.image = os.path.join(self._name, f'{self._direction}.png')

    def draw(self, canvas, x, y):
        self.id = canvas.create_image(
            x, y, image=self.image, anchor='nw', tags='character')

    def redraw(self, canvas, x, y):
        canvas.delete(self.id)
        self.id = canvas.create_image(
            x, y, image=self.image, anchor='nw', tags='character')
