#!/home/defytheflow/.envs/medieval/bin/python3

import tkinter as tk

import config

from frames import GameFrame, MapFrame, SettingsFrame
from widgets.behavior import KeyboardBoundWidget, MouseBoundWidget
from widgets.utils import get_all_widget_children

from backgrounds import GrassBackground
from level import Level
from sprites import Character


class MedievalApp(tk.Tk, KeyboardBoundWidget, MouseBoundWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Medieval')
        self.config(width=config.WIDTH, height=config.HEIGHT, bg=config.BG)
        self.geometry(f'{config.WIDTH}x{config.HEIGHT}')
        self.resizable(0, 0)

        self._current_frame = None  # type: tk.Frame
        self._frames = {}           # type: Dict[str, tk.Frame]

        self._init_frames()
        self._init_level()

        self._notify_keyboardbound_widgets()
        self._notify_mousebound_widgets()

        self.show_frame('game')

    # Overrides KeyboardBoundWidget.
    def init_keyboard_binds(self):
        self.bind_all(config.KEYBOARD_BINDS['show-game-frame'],
            lambda e: self.show_frame('game'))
        self.bind_all(config.KEYBOARD_BINDS['show-map-frame'],
            lambda e: self.show_frame('map'))
        self.bind_all(config.KEYBOARD_BINDS['show-settings-frame'],
            lambda e: self.show_frame('settings'))

    # Overrides MouseBoundWidget.
    def init_mouse_binds(self):
        self._frames['game'].settings_btn.bind('<1>',
            lambda e: self.show_frame('settings'))
        self._frames['game'].map_btn.bind('<1>',
            lambda e: self.show_frame('map'))
        self._frames['map'].return_btn.bind('<1>',
            lambda e: self.show_frame('game'))

    def show_frame(self, frame_tag: str):
        if self._current_frame:
            self._current_frame.forget()

        self._current_frame = self._frames[frame_tag]
        self._current_frame.pack(fill=tk.BOTH)
        self._current_frame.focus_set()

    def _init_frames(self):
        common_attrs = {
            'bg':     self['bg'],
            'width':  self['width'],
            'height': self['height'],
        }
        self._frames['game'] = GameFrame(self, **common_attrs)
        self._frames['map'] = MapFrame(self, **common_attrs)
        self._frames['settings'] = SettingsFrame(self, **common_attrs)

    def _init_level(self):
        self.bg = GrassBackground()  # FUCK !
        character = Character(tag='peasant',
                              size=(30, 30),
                              direction='south',
                              speed=3)
        level = Level(self._frames['game'].game_canvas, character, self.bg)
        level.play()

    def _notify_keyboardbound_widgets(self):
        for widget in get_all_widget_children(self) | {self}:
            if isinstance(widget, KeyboardBoundWidget):
                widget.init_keyboard_binds()

    def _notify_mousebound_widgets(self):
        for widget in get_all_widget_children(self) | {self}:
            if isinstance(widget, MouseBoundWidget):
                widget.init_mouse_binds()


if __name__ == '__main__':
    app = MedievalApp()
    app.mainloop()
