import tkinter as tk
from typing import Dict

import config

from utils import lock_key_press
from widgets.behavior import KeyboardBoundWidget


class GameCanvas(tk.Canvas, KeyboardBoundWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._images: Dict[str, tk.PhotoImage] = {}
        self._sprites: Dict[str, 'Sprite'] = {}

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    # Overrides KeyboardBoundWidget.
    def init_keyboard_binds(self):
        self.bind(config.KEY_BINDS['character-move-north'],
                  lambda e: lock_key_press(lambda: self._sprites.get('peasant').move('north')))

        self.bind(config.KEY_BINDS['character-move-west'],
                  lambda e: lock_key_press(lambda: self._sprites.get('peasant').move('west')))

        self.bind(config.KEY_BINDS['character-move-south'],
                  lambda e: lock_key_press(lambda: self._sprites.get('peasant').move('south')))

        self.bind(config.KEY_BINDS['character-move-east'],
                  lambda e: lock_key_press(lambda: self._sprites.get('peasant').move('east')))

    def add_image(self, image_name: str, image: tk.PhotoImage) -> None:
        if image in self._images.values():
            raise ValueError(f'PhotoImage {image} already stored in {self}')
        self._images[image_name] = image

    def add_sprite(self, sprite: 'Sprite') -> None:
        if sprite in self._sprites.values():
            raise ValueError(f'Sprite {sprite} already stored in {self}.')
        self._sprites[sprite.get_name()] = sprite
