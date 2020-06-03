#!/home/defytheflow/.envs/medieval/bin/python3

import tkinter as tk
from tkinter import ttk

import config

from frames import (
    GameFrame,
    MapFrame,
    SettingsFrame,
)

from widgets.behavior import (
    KeyboardBoundWidget,
    MouseBoundWidget,
    StyledWidget,
)

from widgets.utils import notify_widget_class
from backgrounds import VillageBackground
from sprite import Sprite


class MedievalApp(tk.Tk, StyledWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Medieval')
        self.geometry(f'{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}')
        self.resizable(0, 0)

        self._current_frame = None
        self.frames = {}

        self._init_frames()
        self._init_level()

        notify_widget_class(self, KeyboardBoundWidget, 'init_keyboard_binds')
        notify_widget_class(self, MouseBoundWidget, 'init_mouse_binds')
        notify_widget_class(self, StyledWidget, 'init_style')

        self.show_frame('game')

    def show_frame(self, frame_tag: str):
        if self._current_frame:
            self._current_frame.forget()

        self._current_frame = self.frames[frame_tag]
        self._current_frame.pack(fill=tk.BOTH, expand=True)
        self._current_frame.focus_set()

    def init_style(self):
        ' Overrides StyledWidget. '
        self.style = ttk.Style()
        self.style.configure('MA.TFrame', background=config.BG)

    def _init_frames(self):
        frames_dict = {
            'game':     GameFrame,
            'map':      MapFrame,
            'settings': SettingsFrame
        }

        for name, frame_cls in frames_dict.items():
            self.frames[name] = frame_cls(self,
                                          style='MA.TFrame',
                                          width=config.WINDOW_WIDTH,
                                          height=config.WINDOW_HEIGHT)

    def _init_level(self):
        game_canvas = self.frames['game'].game_canvas

        background = VillageBackground(config.BLOCK_SIZE)
        peasant = Sprite(
            name='peasant',
            canvas=game_canvas,
            position=(0, 0),
            size=(config.BLOCK_SIZE, config.BLOCK_SIZE),
            speed=3)

        background.draw_on_canvas(game_canvas)
        peasant.draw_on_canvas()


if __name__ == '__main__':
    app = MedievalApp()
    app.mainloop()
