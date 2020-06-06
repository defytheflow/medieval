import tkinter as tk
from tkinter import ttk

from config import KeyBindsConfig, GameMapConfig
from game_map import GameMap
from geometry import Oriented, Positionable, Rectangular
from widgets import KeyBoundWidget, MouseBoundWidget


class GameCanvas(tk.Canvas,
                 Oriented, Positionable, Rectangular,
                 KeyBoundWidget, MouseBoundWidget):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        Oriented.__init__(self, 'north')
        Rectangular.__init__(self, (self.winfo_reqwidth(), self.winfo_reqheight()))
        Positionable.__init__(self, (0, 0))

        self.images = {}
        self.sprites = {}
        self.key_pressed = False

        self.map = GameMap(GameMapConfig.size, self)
        self.map.place_rectangle(pos=(0, 0), dim=(500, 500), fill='green')
        self.map.draw()

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    def init_key_binds(self):
        self.bind(KeyBindsConfig.character_move_north,
                  lambda e: self.move_sprite('peasant', 'north'))
        self.bind(KeyBindsConfig.character_move_west,
                  lambda e: self.move_sprite('peasant', 'west'))
        self.bind(KeyBindsConfig.character_move_south,
                  lambda e: self.move_sprite('peasant', 'south'))
        self.bind(KeyBindsConfig.character_move_east,
                  lambda e: self.move_sprite('peasant', 'east'))

    def init_mouse_binds(self):
        self.bind('<Enter>', lambda e: self.focus_set())

    def save_image(self, name, image):
        self.images[name] = image

    def save_sprite(self, sprite):
        self.sprites[sprite.name] = sprite

    def move(self, direction):
        self.direction = direction

        if direction == 'north':
            self.position = (self.x, self.y - self.sprites['peasant'].speed)
        elif direction == 'west':
            self.position = (self.x - self.sprites['peasant'].speed, self.y)
        elif direction == 'south':
            self.position = (self.x, self.y + self.sprites['peasant'].speed)
        elif direction == 'east':
            self.position = (self.x + self.sprites['peasant'].speed, self.y)

        self.map.redraw()

    def move_sprite(self, name, direction):
        self.move(direction)
        self._lock_key_press(lambda: self.sprites[name].move(direction))

    def _lock_key_press(self, command):
        ' Internal method to stop key events from spamming. '
        if not self.key_pressed:
            self.key_pressed = True
            command()
            self.key_pressed = False
