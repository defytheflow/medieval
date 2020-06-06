import tkinter as tk
from tkinter import ttk

from config import ColorsConfig, GameCanvasConfig, KeyBindsConfig
from game_canvas import GameCanvas
from widgets import KeyBoundWidget


class GameFrame(ttk.Frame, KeyBoundWidget):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = master
        self.canvas = GameCanvas(self,
                                 background=ColorsConfig.bg,
                                 width=GameCanvasConfig.width,
                                 height=GameCanvasConfig.height,
                                 relief='raised')
        self.canvas.pack(side='left', fill='both')

    def focus_set(self):
        super().focus_set()
        self.canvas.focus_set()

    def init_key_binds(self):
        self.bind_all(KeyBindsConfig.show_game, lambda e: self.controller.show_frame('game'))
        self.bind_all(KeyBindsConfig.show_map, lambda e: self.controller.show_frame('map'))
