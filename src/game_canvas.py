import tkinter as tk

import utils

class GameCanvas(tk.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pressed = False

        self.bind('<KeyPress w>', lambda e: self._key_press_decorator(self._on_w, e))
        self.bind('<KeyPress a>', lambda e: self._key_press_decorator(self._on_a, e))
        self.bind('<KeyPress s>', lambda e: self._key_press_decorator(self._on_s, e))
        self.bind('<KeyPress d>', lambda e: self._key_press_decorator(self._on_d, e))

        self.focus_set()

    def _key_press_decorator(self, callback_func, event):
        if not self._pressed:
            self._pressed = True
            callback_func(event)
            self._pressed = False

    def _on_w(self, event):
        old_x, old_y = self.coords(self.character.id)

        self.character.direction = 'north'
        new_x = old_x
        new_y = old_y - self.character.width()

        self._animate_character_movement(old_x, old_y, new_x, new_y)
        self.character.reset_costume()
        self.character.redraw(self, new_x, new_y)

    def _on_a(self, event):
        old_x, old_y = self.coords(self.character.id)

        self.character.direction = 'west'
        new_x = old_x - self.character.width()
        new_y = old_y

        self._animate_character_movement(old_x, old_y, new_x, new_y)
        self.character.reset_costume()
        self.character.redraw(self, new_x, new_y)

    def _on_s(self, event):
        old_x, old_y = self.coords(self.character.id)

        self.character.direction = 'south'
        new_x = old_x
        new_y = old_y + self.character.width()

        self._animate_character_movement(old_x, old_y, new_x, new_y)
        self.character.reset_costume()
        self.character.redraw(self, new_x, new_y)

    def _on_d(self, event):
        old_x, old_y = self.coords(self.character.id)

        self.character.direction = 'east'
        new_x = old_x + self.character.width()
        new_y = old_y

        self._animate_character_movement(old_x, old_y, new_x, new_y)
        self.character.reset_costume()
        self.character.redraw(self, new_x, new_y)

    def _animate_character_movement(self, old_x, old_y, new_x, new_y):
        sleep_time = 10

        if old_x != new_x:
            if old_x < new_x:
                for i in range(1, self.character.width() + 1, self.character.speed):
                    self.character.switch_costume()
                    self.character.redraw(self, old_x + i, old_y)
                    self.after(sleep_time)
                    self.update()
            else:
                for i in range(1, self.character.width() + 1, self.character.speed):
                    self.character.switch_costume()
                    self.character.redraw(self, old_x - i, old_y)
                    self.after(sleep_time)
                    self.update()
        else:
            if old_y < new_y:
                for i in range(1, self.character.width() + 1, self.character.speed):
                    self.character.switch_costume()
                    self.character.redraw(self, old_x, old_y + i)
                    self.after(sleep_time)
                    self.update()
            else:
                for i in range(1, self.character.width() + 1, self.character.speed):
                    self.character.switch_costume()
                    self.character.redraw(self, old_x, old_y - i)
                    self.after(sleep_time)
                    self.update()
