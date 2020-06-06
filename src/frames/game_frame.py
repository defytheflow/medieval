import os
import tkinter as tk
from tkinter import ttk

from config import AssetsConfig, ColorsConfig, FontsConfig, GameCanvasConfig, KeyBindsConfig
from utils import create_photo_image
from widgets import KeyBoundWidget, MouseBoundWidget, StyledWidget, Tooltip
from widgets import bind_image_to_widget, bind_sound_to_widget


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


class GameCanvas(tk.Canvas, KeyBoundWidget, MouseBoundWidget):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.images = {}
        self.sprites = {}
        self.key_pressed = False

    def init_key_binds(self):
        ' Overrides KeyBoundWidget. '
        self.bind(KeyBindsConfig.character_move_north,
                  lambda e: self.move_sprite('peasant', 'north'))
        self.bind(KeyBindsConfig.character_move_west,
                  lambda e: self.move_sprite('peasant', 'west'))
        self.bind(KeyBindsConfig.character_move_south,
                  lambda e: self.move_sprite('peasant', 'south'))
        self.bind(KeyBindsConfig.character_move_east,
                  lambda e: self.move_sprite('peasant', 'east'))

    def init_mouse_binds(self):
        ' Overrides MouseBoundWidget. '
        self.bind('<Enter>', lambda e: self.focus_set())

    def cache_image(self, image_name, image):
        ' Stores reference to image. '
        if image in self.images.values():
            raise ValueError(f'Image {image} already stored in {self}.')
        self.images[image_name] = image

    def cache_sprite(self, sprite):
        ' Stores reference to sprite. '
        if sprite in self.sprites.values():
            raise ValueError(f'Sprite {sprite} already stored in {self}.')
        self.sprites[sprite.name] = sprite

    def move_sprite(self, sprite_name, direction):
        ' Sends a sprite a signal to move in direction. '
        self._lock_key_press(lambda: self.sprites.get(sprite_name).move(direction))

    def _lock_key_press(self, command):
        ' Internal method to stop key events from spamming. '
        if not self.key_pressed:
            self.key_pressed = True
            command()
            self.key_pressed = False

    # def init_style(self):
    #     self.style= ttk.style()

    #     self.style.configure('gf.tlabel',
    #                           padding=(10, 5),
    #                           background=colorsconfig.bg,
    #                           foreground=colorsconfig.fg,
    #                           borderwidth=5,
    #                           font=fontsconfig.p)

    #     self.style.configure('gf.tbutton',
    #                           background=colorsconfig.bg,
    #                           foreground=colorsconfig.fg,
    #                           borderwidth=5,
    #                           relief='raised')

    #     self.style.map('gf.tbutton',
    #                     background=[('active', colorsconfig.active_bg)])

    #     self.style.configure('gf.tradiobutton',
    #                           background=colorsconfig.bg,
    #                           foreground=colorsconfig.fg,
    #                           indicatordiameter=20,
    #                           focuscolor=colorsconfig.bg,
    #                           font=fontsconfig.p)

    #     self.style.map('gf.tradiobutton',
    #                     background=[('active', colorsconfig.bg)],
    #                     indicatorcolor=[('selected', colorsconfig.active_bg)])

    # self.hint_lbl = ttk.label(self, style='gf.tlabel', text='hint', relief='raised')
    # self.hint_lbl.pack(fill='both')
    # def _create_button(self, master, text, image_name):
    #     btn = ttk.button(master, style='gf.tbutton')
    #     tooltip(btn, text=text, bg=master['bg'], waittime=300)
    #     bind_image_to_widget(btn, os.path.join(assetsconfig.icons, image_name), (100, 100))
    #     bind_sound_to_widget(btn, '<1>', os.path.join(assetsconfig.sounds, 'button-click.wav'))
    #     return btn

    # # def _init_game_frame(self):
    #     # game_frame = ttk.frame(self, height=self.winfo_reqheight() * 0.8)
    #     # button_frame = tk.frame(game_frame, background=colorsconfig.bg)
    #     # self.map_btn = self._create_button(button_frame, 'map', 'map.png')
    #     # self.inventory_btn = self._create_button(button_frame, 'inventory', 'inventory.png')
    #     # self.market_btn = self._create_button(button_frame, 'market', 'market.png')
    #     # self.bank = self._create_button(button_frame, 'bank', 'bank.png')
    #     # self.smith = self._create_button(button_frame, 'smith', 'smith.png')
    #     # self.inventory_btn.configure(state='disabled')
    #     # self.market_btn.configure(state='disabled')
    #     # self.bank_btn.configure(state='disabled')
    #     # self.smith_btn.configure(state='disabled')

    #     # game_frame.pack(fill='both')
    #     # button_frame.pack(side='left', fill='both', expand=true)

    #     # for btn in button_frame.winfo_children():
    #     #     btn.pack(fill='both', expand=True)

