import os
import tkinter as tk
from tkinter import ttk

from config import (
    AssetsConfig,
    ColorsConfig,
    FontsConfig,
    GameCanvasConfig,
    KeyBindsConfig,
)

from widgets import (
    KeyBoundWidget,
    MouseBoundWidget,
    StyledWidget,
    Tooltip,
    bind_image_to_widget,
    bind_sound_to_widget,
    get_widget_parent,
)

from canvases import GameCanvas
from utils import create_photo_image


class GameFrame(ttk.Frame, KeyBoundWidget, MouseBoundWidget, StyledWidget):

    BD = 5

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.hint_lbl = ttk.Label(self, style='GF.TLabel', text='Hint', relief='raised')
        self.hint_lbl.pack(fill='both')

        self._init_game_frame()

    def focus_set(self):
        super().focus_set()
        self.game_canvas.focus_set()

    def init_key_binds(self):
        self.bind_all(KeyBindsConfig.show_game,
                      lambda e: get_widget_parent(self).show_frame('game'))
        self.bind_all(KeyBindsConfig.show_map,
                      lambda e: get_widget_parent(self).show_frame('map'))

    def init_mouse_binds(self):
        self.map_btn.bind('<1>', lambda e: get_widget_parent(self).show_frame('map'))

    def init_style(self):
        self.style= ttk.Style()

        self.style.configure('GF.TLabel',
                              padding=(10, 5),
                              background=ColorsConfig.bg,
                              foreground=ColorsConfig.fg,
                              borderwidth=5,
                              font=FontsConfig.p)

        self.style.configure('GF.TButton',
                              background=ColorsConfig.bg,
                              foreground=ColorsConfig.fg,
                              borderwidth=5,
                              relief='raised')

        self.style.map('GF.TButton',
                        background=[('active', ColorsConfig.active_bg)])

        self.style.configure('GF.TRadiobutton',
                              background=ColorsConfig.bg,
                              foreground=ColorsConfig.fg,
                              indicatordiameter=20,
                              focuscolor=ColorsConfig.bg,
                              font=FontsConfig.p)

        self.style.map('GF.TRadiobutton',
                        background=[('active', ColorsConfig.bg)],
                        indicatorcolor=[('selected', ColorsConfig.active_bg)])

    def _create_button(self, master, text, image_name):
        btn = ttk.Button(master, style='GF.TButton')
        Tooltip(btn, text=text, bg=master['bg'], waittime=300)
        bind_image_to_widget(btn, os.path.join(AssetsConfig.icons, image_name), (100, 100))
        bind_sound_to_widget(btn, '<1>', os.path.join(AssetsConfig.sounds, 'button-click.wav'))
        return btn

    def _init_game_frame(self):
        game_frame = ttk.Frame(self, height=self.winfo_reqheight() * 0.8)

        self.game_canvas = GameCanvas(game_frame,
                                      background=ColorsConfig.bg,
                                      width=GameCanvasConfig.width,
                                      height=GameCanvasConfig.height,
                                      relief='raised')

        button_frame = tk.Frame(game_frame, background=ColorsConfig.bg)

        self.map_btn = self._create_button(button_frame, 'Map', 'map.png')
        self.inventory_btn = self._create_button(button_frame, 'Inventory', 'inventory.png')
        self.market_btn = self._create_button(button_frame, 'Market', 'market.png')
        self.bank = self._create_button(button_frame, 'Bank', 'bank.png')
        self.smith = self._create_button(button_frame, 'Smith', 'smith.png')

        # self.inventory_btn.configure(state='disabled')
        # self.market_btn.configure(state='disabled')
        # self.bank_btn.configure(state='disabled')
        # self.smith_btn.configure(state='disabled')

        game_frame.pack(fill='both')
        self.game_canvas.pack(side='left', fill='both')
        button_frame.pack(side='left', fill='both', expand=True)

        for btn in button_frame.winfo_children():
            btn.pack(fill='both', expand=True)
