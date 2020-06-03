import tkinter as tk

import config

from widgets.behavior import (
    KeyboardBoundWidget,
    MouseBoundWidget,
)


class GameCanvas(tk.Canvas, KeyboardBoundWidget, MouseBoundWidget):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.images = {}
        self.sprites = {}
        self.key_pressed = False

    def init_keyboard_binds(self):
        ' Overrides KeyboardBoundWidget. '
        self.bind(config.KEY_BINDS['character-move-north'],
                  lambda e: self.move_sprite('peasant', 'north'))
        self.bind(config.KEY_BINDS['character-move-west'],
                  lambda e: self.move_sprite('peasant', 'west'))
        self.bind(config.KEY_BINDS['character-move-south'],
                  lambda e: self.move_sprite('peasant', 'south'))
        self.bind(config.KEY_BINDS['character-move-east'],
                  lambda e: self.move_sprite('peasant', 'east'))

    def init_mouse_binds(self):
        ' Overrides MouseBoundWidget. '
        self.bind('<Enter>', lambda e: self.focus_set())

    def add_image(self, image_name, image):
        if image in self.images.values():
            raise ValueError(f'Image {image} already stored in {self}.')
        self.images[image_name] = image

    def add_sprite(self, sprite):
        if sprite in self.sprites.values():
            raise ValueError(f'Sprite {sprite} already stored in {self}.')
        self.sprites[sprite.name] = sprite

    def move_sprite(self, sprite_name, direction):
        self._lock_key_press(lambda: self.sprites.get(sprite_name).move(direction))

    def _lock_key_press(self, command):
        if not self.key_pressed:
            self.key_pressed = True
            command()
            self.key_pressed = False
