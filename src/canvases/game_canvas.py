import tkinter as tk
from typing import Callable

import config

from widgets.behavior import KeyboardBoundWidget


class GameCanvas(tk.Canvas, KeyboardBoundWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pressed = False

    # Overrides KeyboardBoundWidget.
    def init_keyboard_binds(self):
        self.bind(config.KEY_BINDS['game-move-up'],
            lambda e: self._lock_key(self._move_up))
        self.bind(config.KEY_BINDS['game-move-left'],
            lambda e: self._lock_key(self._move_left))
        self.bind(config.KEY_BINDS['game-move-down'],
            lambda e: self._lock_key(self._move_down))
        self.bind(config.KEY_BINDS['game-move-right'],
            lambda e: self._lock_key(self._move_right))

    def _lock_key(self, command: Callable):
        if not self._pressed:
            self._pressed = True
            command()
            self._pressed = False

    def _move_up(self):
        old_x, old_y = self.coords(self.character.id)

        self.character.direction = 'north'
        new_x = old_x
        new_y = old_y - self.character.width

        self._animate_character_movement(old_x, old_y, new_x, new_y)
        self.character.reset_costume()
        self.character.redraw(self, new_x, new_y)

    def _move_left(self):
        old_x, old_y = self.coords(self.character.id)

        self.character.direction = 'west'
        new_x = old_x - self.character.width
        new_y = old_y

        self._animate_character_movement(old_x, old_y, new_x, new_y)
        self.character.reset_costume()
        self.character.redraw(self, new_x, new_y)

    def _move_down(self):
        old_x, old_y = self.coords(self.character.id)

        self.character.direction = 'south'
        new_x = old_x
        new_y = old_y + self.character.width

        self._animate_character_movement(old_x, old_y, new_x, new_y)
        self.character.reset_costume()
        self.character.redraw(self, new_x, new_y)

    def _move_right(self):
        old_x, old_y = self.coords(self.character.id)

        self.character.direction = 'east'
        new_x = old_x + self.character.width
        new_y = old_y

        self._animate_character_movement(old_x, old_y, new_x, new_y)
        self.character.reset_costume()
        self.character.redraw(self, new_x, new_y)

    def _animate_character_movement(self, old_x, old_y, new_x, new_y):
        sleep_time = 10

        if old_x != new_x:
            if old_x < new_x:
                for i in range(1, self.character.width + 1, self.character.speed):
                    self.character.switch_costume()
                    self.character.redraw(self, old_x + i, old_y)
                    self.after(sleep_time)
                    self.update()
            else:
                for i in range(1, self.character.width + 1, self.character.speed):
                    self.character.switch_costume()
                    self.character.redraw(self, old_x - i, old_y)
                    self.after(sleep_time)
                    self.update()
        else:
            if old_y < new_y:
                for i in range(1, self.character.width + 1, self.character.speed):
                    self.character.switch_costume()
                    self.character.redraw(self, old_x, old_y + i)
                    self.after(sleep_time)
                    self.update()
            else:
                for i in range(1, self.character.width + 1, self.character.speed):
                    self.character.switch_costume()
                    self.character.redraw(self, old_x, old_y - i)
                    self.after(sleep_time)
                    self.update()
