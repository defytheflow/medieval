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
            lambda e: self._lock_key(self._move_up))
        self.bind(config.KEY_BINDS['character-move-left'],
            lambda e: self._lock_key(self._move_left))
        self.bind(config.KEY_BINDS['character-move-down'],
            lambda e: self._lock_key(self._move_down))
        self.bind(config.KEY_BINDS['character-move-right'],
            lambda e: self._lock_key(self._move_right))

    def add_sprite(self, sprite) -> None:
        self._sprites[sprite.get_name()] = sprite

    def add_image(self, image_name: str, image: tk.PhotoImage) -> None:
        self._images[image_name] = image

    def _lock_key(self, command: Callable):
        if not self._pressed:
            self._pressed = True
            command()
            self._pressed = False

    def _move_up(self):
        print(self._sprites)
        print(self._images)
        x, y = self.coords(self._sprites['peasant'].get_canvas_id())

        self._sprites['peasant'].set_direction('north')
        y -= self._sprites['peasant'].get_width()

        self._animate_character_movement(x, y + self._sprites['peasant'].get_width(), x, y)
        self._sprites['peasant'].reset_costume()
        self._sprites['peasant'].redraw_on_game_canvas(x, y)

    def _move_left(self):
        old_x, old_y = self.coords(self._sprites['peasant'].get_canvas_id())

        self._sprites['peasant'].set_direction('west')
        new_x = old_x - self._sprites['peasant'].get_width()
        new_y = old_y

        self._animate_character_movement(old_x, old_y, new_x, new_y)
        self._sprites['peasant'].reset_costume()
        self._sprites['peasant'].redraw_on_game_canvas(new_x, new_y)

    def _move_down(self):
        old_x, old_y = self.coords(self._sprites['peasant'].get_canvas_id())

        self._sprites['peasant'].set_direction('south')
        new_x = old_x
        new_y = old_y + self._sprites['peasant'].get_width()

        self._animate_character_movement(old_x, old_y, new_x, new_y)
        self._sprites['peasant'].reset_costume()
        self._sprites['peasant'].redraw_on_game_canvas(new_x, new_y)

    def _move_right(self):
        old_x, old_y = self.coords(self._sprites['peasant'].get_canvas_id())

        self._sprites['peasant'].set_direction('east')
        new_x = old_x + self._sprites['peasant'].get_width()
        new_y = old_y

        self._animate_character_movement(old_x, old_y, new_x, new_y)
        self._sprites['peasant'].reset_costume()
        self._sprites['peasant'].redraw_on_game_canvas(new_x, new_y)

    def _animate_character_movement(self, old_x, old_y, new_x, new_y):
        sleep_time = 10

        if old_x != new_x:
            if old_x < new_x:
                for i in range(1, self._sprites['peasant'].get_width() + 1, self._sprites['peasant'].get_speed()):
                    self._sprites['peasant'].switch_costume()
                    self._sprites['peasant'].redraw_on_game_canvas(old_x + i, old_y)
                    self.after(sleep_time)
                    self.update()
            else:
                for i in range(1, self._sprites['peasant'].get_width() + 1, self._sprites['peasant'].get_speed()):
                    self._sprites['peasant'].switch_costume()
                    self._sprites['peasant'].redraw_on_game_canvas(old_x - i, old_y)
                    self.after(sleep_time)
                    self.update()
        else:
            if old_y < new_y:
                for i in range(1, self._sprites['peasant'].get_width() + 1, self._sprites['peasant'].get_speed()):
                    self._sprites['peasant'].switch_costume()
                    self._sprites['peasant'].redraw_on_game_canvas(old_x, old_y + i)
                    self.after(sleep_time)
                    self.update()
            else:
                for i in range(1, self._sprites['peasant'].get_width() + 1, self._sprites['peasant'].get_speed()):
                    self._sprites['peasant'].switch_costume()
                    self._sprites['peasant'].redraw_on_game_canvas(old_x, old_y - i)
                    self.after(sleep_time)
                    self.update()
