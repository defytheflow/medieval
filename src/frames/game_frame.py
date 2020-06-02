import os
import tkinter as tk
from tkinter import ttk

import config

from utils import (
    bind_image,
    bind_sound,
    create_photo_image,
)

from widgets.behavior import (
    KeyboardBoundWidget,
    MouseBoundWidget,
)

from widgets.bilingual import (
    BilingualRadiobutton,
    BilingualLabel,
    BilingualButton,
    BilingualTooltip,
)

from widgets.utils import get_widget_parent

from canvases import (
    DialogueCanvas,
    GameCanvas,
)


class GameFrame(tk.Frame, KeyboardBoundWidget, MouseBoundWidget):

    BD = 5
    LBL_PADX = 10

    def __init__(self, master: tk.Tk, **kwargs):
        super().__init__(master, **kwargs)

        self.choice_var = tk.IntVar(self)

        self._init_hint_frame()
        self._init_game_frame()
        self._init_dialogue_frame()

    # Overrides tk.Frame.
    def focus_set(self):
        super().focus_set()
        self.game_canvas.focus_set()

    # Overrides KeyboardBoundWidget.
    def init_keyboard_binds(self):
        self.bind_all(config.KEY_BINDS['show-game'],
            lambda e: get_widget_parent(self).show_frame('game'))
        self.bind_all(config.KEY_BINDS['show-map'],
            lambda e: get_widget_parent(self).show_frame('map'))
        self.bind_all(config.KEY_BINDS['show-settings'],
            lambda e: get_widget_parent(self).show_frame('settings'))

    # Overrides MouseBoundWidget.
    def init_mouse_binds(self):
        self.settings_btn.bind('<1>',
            lambda e: get_widget_parent(self).show_frame('settings'))
        self.map_btn.bind('<1>',
            lambda e: get_widget_parent(self).show_frame('map'))

    def _init_hint_frame(self):
        hint_frame = tk.Frame(self)
        self.hint_lbl = BilingualLabel(hint_frame,
            bg=self['bg'],
            bd=self.BD,
            text_dict={'eng': 'Hint:', 'rus': 'Подсказка:'},
            padx=self.LBL_PADX,
            relief='raised',
            anchor='nw')

        hint_frame.pack(fill='both')
        self.hint_lbl.pack(fill='both')

    def _init_game_frame(self):
        game_frame = tk.Frame(self, height=self.winfo_reqheight() * 0.8,
                              bg=self['bg'])

        self.game_canvas = GameCanvas(game_frame,
            width=self.winfo_reqwidth() * 0.8,
            height=game_frame.winfo_reqheight(),
            highlightbackground=config.HIGHLIGHT_BG)

        buttons_frame = tk.Frame(game_frame)

        ttk.Style().configure('GF.TButton',
            background=config.BG,
            borderwidth=5,
            relief='raised'
        )

        ttk.Style().map('GF.TButton',
            background=[('active', config.ACTIVE_BG)]
        )

        self.settings_btn = BilingualButton(buttons_frame,
            text_dict={'eng': 'Settings', 'rus': 'Настройки'}, style='GF.TButton')

        BilingualTooltip(self.settings_btn,
            text_dict={'eng': 'Settings', 'rus': 'Настройки'},
            bg=self['bg'], waittime=300)

        bind_image(self.settings_btn, os.path.join(config.ICONS_ROOT, 'settings.png'), (100, 100))

        self.map_btn = BilingualButton(buttons_frame,
            text_dict={'eng': 'Map', 'rus': 'Карта'}, style='GF.TButton')

        BilingualTooltip(self.map_btn,
            text_dict={'eng': 'Map', 'rus': 'Карта'},
            bg=self['bg'], waittime=300)

        bind_image(self.map_btn, os.path.join(config.ICONS_ROOT, 'map.png'), (100, 100))

        self.inventory_btn = BilingualButton(buttons_frame,
            text_dict={'eng': 'Inventory', 'rus': 'Инвентарь'}, style='GF.TButton')
        self.inventory_btn.configure(state='disabled')

        BilingualTooltip(self.inventory_btn,
            text_dict={'eng': 'Inventory', 'rus': 'Инвентарь'},
            bg=self['bg'], waittime=300)

        bind_image(self.inventory_btn, os.path.join(config.ICONS_ROOT, 'inventory.png'), (100, 100))

        self.market_btn = BilingualButton(buttons_frame,
            text_dict={'eng': 'Market', 'rus': 'Магазин'}, style='GF.TButton')
        self.market_btn.configure(state='disabled')

        BilingualTooltip(self.market_btn,
            text_dict={'eng': 'Market', 'rus': 'Магазин'},
            bg=self['bg'], waittime=300)

        bind_image(self.market_btn, os.path.join(config.ICONS_ROOT, 'market.png'), (100, 100))

        self.bank_btn = BilingualButton(buttons_frame,
            text_dict={'eng': 'Bank', 'rus': 'Банк'}, style='GF.TButton')
        self.bank_btn.configure(state='disabled')

        BilingualTooltip(self.bank_btn,
            text_dict={'eng': 'Bank', 'rus': 'Банк'},
            bg=self['bg'], waittime=300)

        bind_image(self.bank_btn, os.path.join(config.ICONS_ROOT, 'bank.png'), (100, 100))

        self.smith_btn = BilingualButton(buttons_frame,
            text_dict={'eng': 'Smith', 'rus': 'Кузнец'}, style='GF.TButton')
        self.smith_btn.configure(state='disabled')

        BilingualTooltip(self.smith_btn,
            text_dict={'eng': 'Smith', 'rus': 'Кузнец'},
            bg=self['bg'], waittime=300)

        bind_image(self.smith_btn, os.path.join(config.ICONS_ROOT, 'smith.png'), (100, 100))

        game_frame.pack(fill='both')
        self.game_canvas.pack(side='left', fill='both')

        buttons_frame.pack(side='left', fill='both')

        for btn in buttons_frame.winfo_children():
            btn.pack(fill='both', expand=True)
            bind_sound(btn, '<1>', os.path.join(config.SOUNDS_ROOT, 'click.wav'))

    def _init_dialogue_frame(self):
        dialogue_frame = tk.Frame(self)

        self.dialogue_canvas = DialogueCanvas(dialogue_frame,
            width=self.winfo_reqwidth() * 0.13,
            height=self.winfo_reqheight() * 0.2,
            bg=self['bg'],
            bd=self.BD,
            highlightbackground=config.HIGHLIGHT_BG,
            relief='raised')

        choice_frame = tk.Frame(dialogue_frame,
            bg=self['bg'],
            bd=self.BD,
            relief='raised')

        self.dialogue_lbl = BilingualLabel(choice_frame,
            bg=self['bg'],
            bd=self.BD,
            text_dict={'eng': 'Question', 'rus': 'Вопрос'},
            padx=self.LBL_PADX,
            relief='raised',
            anchor='nw')

        common_attrs = {
            'bg':                  self['bg'],
            'activebackground':    self['bg'],
            'highlightbackground': self['bg'],
            'compound':            'center',
        }

        btn1 = BilingualRadiobutton(choice_frame,
            text_dict={'eng': 'yes', 'rus': 'да'},
            value=1,
            variable=self.choice_var,
            **common_attrs)

        btn2 = BilingualRadiobutton(choice_frame,
            text_dict={'eng': 'no', 'rus': 'нет'},
            value=2,
            variable=self.choice_var,
            **common_attrs)

        for btn in (btn1, btn2):
            bind_image(btn, os.path.join(config.ICONS_ROOT, 'choice.png'), (180, 90))

        dialogue_frame.pack(fill='both')
        self.dialogue_canvas.pack(side='left', fill='both')

        choice_frame.pack(side='left', fill='both', expand=True)
        self.dialogue_lbl.pack(fill='both')

        btn1.pack(side='left', expand=True)
        btn2.pack(side='left', expand=True)
