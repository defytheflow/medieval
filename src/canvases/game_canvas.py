import tkinter as tk

import config

from widgets.behavior import (
    KeyBoundWidget,
    MouseBoundWidget,
)


class GameCanvas(tk.Canvas, KeyBoundWidget, MouseBoundWidget):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.images = {}
        self.sprites = {}
        self.key_pressed = False

    def init_key_binds(self):
        ' Overrides KeyBoundWidget. '
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

    def cache_image(self, image_name, image):
        ' Stores reference to image. '
        if image in self.images.values():
            raise ValueError(f'Image {image} already stored in {self}.')
        self.images[image_name] = image

    def cache_sprite(self, sprite):
        ' Stores reference to sprite. '
        if sprite in self.sprites.values():
            raise ValueError(f'Sprite {sprite} already stored in {self}.')
        self.sprites[sprite.name] = sprite

    def move_sprite(self, sprite_name, direction):
        ' Sends a sprite a signal to move in direction. '
        self._lock_key_press(lambda: self.sprites.get(sprite_name).move(direction))

    def _lock_key_press(self, command):
        ' Internal method to stop key events from spamming. '
        if not self.key_pressed:
            self.key_pressed = True
            command()
            self.key_pressed = False
