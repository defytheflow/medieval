import tkinter as tk
from typing import Callable

import config

from widgets.behavior import KeyboardBoundWidget


class GameCanvas(tk.Canvas, KeyboardBoundWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pressed = False
        self._sprites = {}      # type: Dict[str, Sprite]
        self._images = {}       # type: Dict[str, tk.PhotoImage]

    # Overrides KeyboardBoundWidget.
    def init_keyboard_binds(self):
        self.bind(config.KEY_BINDS['character-move-up'],
            lambda e: self._lock_key(lambda: self._sprites['peasant'].move('north')))
        self.bind(config.KEY_BINDS['character-move-left'],
            lambda e: self._lock_key(lambda: self._sprites['peasant'].move('west')))
        self.bind(config.KEY_BINDS['character-move-down'],
            lambda e: self._lock_key(lambda: self._sprites['peasant'].move('south')))
        self.bind(config.KEY_BINDS['character-move-right'],
            lambda e: self._lock_key(lambda: self._sprites['peasant'].move('east')))

    def add_sprite(self, sprite) -> None:
        self._sprites[sprite.get_name()] = sprite

    def add_image(self, image_name: str, image: tk.PhotoImage) -> None:
        self._images[image_name] = image

    def _lock_key(self, command: Callable):
        if not self._pressed:
            self._pressed = True
            command()
            self._pressed = False
