#!python3

import tkinter as tk
from tkinter import ttk

from config import ColorsConfig, GameCanvasConfig, KeyBindsConfig, WindowConfig
from frames import GameFrame, MapFrame
from geometry import Position, Size, get_center_position
from sprite import Sprite
from widgets import KeyBoundWidget, MouseBoundWidget, StyledWidget
from widgets import get_all_widget_children


class MedievalApp(tk.Tk, StyledWidget):

    def __init__(self):
        super().__init__()

        self.title(WindowConfig.title)
        self.geometry(f'{WindowConfig.width}x{WindowConfig.height}')
        self.resizable(0, 0)
        self.update_idletasks()

        self.current_frame = None
        self.frames = {  # <- Add new frames here.
            'game': GameFrame,
            'map':  MapFrame,
        }

        self.create_frames()
        self.create_character()

        self.notify_widgets(self)
        self.show_frame('game')

    def init_style(self):
        self.style = ttk.Style()
        self.style.configure('MA.TFrame', background=ColorsConfig.bg)

    def show_frame(self, frame_name):
        if self.current_frame:
            self.current_frame.forget()

        self.current_frame = self.frames[frame_name]
        self.current_frame.pack(fill='both', expand=True)
        self.current_frame.focus_set()

    def create_frames(self):
        for frame_name, frame_cls in self.frames.items():
            self.frames[frame_name] = frame_cls(self, style='MA.TFrame',
                                                width=WindowConfig.width,
                                                height=WindowConfig.height)

    def create_character(self):
        game_canvas = self.frames['game'].canvas
        character = Sprite('peasant', game_canvas, Size(50, 50), Position(0, 0), speed=5)
        character.position = get_center_position(game_canvas.size, character.size)
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
