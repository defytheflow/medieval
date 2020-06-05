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
    KeyBoundWidget,
    MouseBoundWidget,
    StyledWidget,
)

from widgets.utils import (
    get_all_widget_children,
)

from backgrounds import VillageBackground
from sprite import Sprite


class MedievalApp(tk.Tk, StyledWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(config.WINDOW['title'])
        self.geometry(f"{config.WINDOW['width']}x{config.WINDOW['height']}")
        self.resizable(0, 0)

        self.current_frame = None
        self.frames = {  # <- Add new frames here.
                'game': GameFrame,
                 'map': MapFrame,
            'settings': SettingsFrame
        }

        self.init_frames()
        self.init_level()

        self.notify_widgets(self)
        self.show_frame('game')

    def init_style(self):
        ' Overrides StyledWidget. '
        self.style = ttk.Style()
        self.style.configure('MA.TFrame', background=config.COLORS['bg'])

    def show_frame(self, frame_name):
        if self.current_frame:
            self.current_frame.forget()

        self.current_frame = self.frames[frame_name]
        self.current_frame.pack(fill='both', expand=True)
        self.current_frame.focus_set()

    def init_frames(self):
        for frame_name, frame_cls, in self.frames.items():
            self.frames[frame_name] = frame_cls(self,
                                                style='MA.TFrame',
                                                width=config.WINDOW['width'],
                                                height=config.WINDOW['height'])

    def init_level(self):
        background = VillageBackground(config.GAME_CANVAS['block_size'])
        character = Sprite(name='peasant',
                           canvas=self.frames['game'].game_canvas,
                           position=(0, 0),
                           size=(config.GAME_CANVAS['block_size'],
                                 config.GAME_CANVAS['block_size']),
                           speed=3)

        background.draw_on_canvas(self.frames['game'].game_canvas)
        character.draw_on_canvas()

    @staticmethod
    def notify_widgets(root):
        for widget in get_all_widget_children(root) + [root]:
            if isinstance(widget, KeyBoundWidget):
                widget.init_key_binds()
            if isinstance(widget, MouseBoundWidget):
                widget.init_mouse_binds()
            if isinstance(widget, StyledWidget):
                widget.init_style()


if __name__ == '__main__':
    app = MedievalApp()
    app.mainloop()
