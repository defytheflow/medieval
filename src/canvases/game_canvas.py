import tkinter as tk
from typing import Dict

import config

from widgets.behavior import KeyboardBoundWidget
from utils import lock_key_press


class GameCanvas(tk.Canvas, KeyboardBoundWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pressed = False
        self._sprites = {}      # type: Dict[str, Sprite]
        self._images = {}       # type: Dict[str, tk.PhotoImage]

    # Overrides KeyboardBoundWidget.
    def init_keyboard_binds(self):
        self.bind(config.KEY_BINDS['character-move-north'],
                  lambda e: lock_key_press(lambda: self._sprites['peasant'].move('north')))

        self.bind(config.KEY_BINDS['character-move-west'],
                  lambda e: lock_key_press(lambda: self._sprites['peasant'].move('west')))

        self.bind(config.KEY_BINDS['character-move-south'],
                  lambda e: lock_key_press(lambda: self._sprites['peasant'].move('south')))

        self.bind(config.KEY_BINDS['character-move-east'],
                  lambda e: lock_key_press(lambda: self._sprites['peasant'].move('east')))

    def add_sprite(self, sprite) -> None:
        self._sprites[sprite.get_name()] = sprite

    def add_image(self, image_name: str, image: tk.PhotoImage) -> None:
        self._images[image_name] = image
