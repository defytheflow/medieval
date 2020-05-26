import os
import tkinter as tk

import config
from widgets import ToolTipButton, BilingualLabel

from .canvases import GameCanvas, DialogueCanvas
from .widgets import ChoiceButton


class GameFrame(tk.Frame):

    FOREGROUND = '#000'
    BORDERWIDTH = 5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.hint_frame = None
        self.game_frame = None
        self.dialogue_frame = None

        self.game_canvas = None
        self.dialogue_canvas = None

        self.settings_btn = None
        self.map_btn = None
        self.inventory_btn = None
        self.market_btn = None
        self.bank_btn = None
        self.smith_btn = None

        self.hint_lbl = None
        self.dialogue_lbl = None

        self.choice_var = tk.IntVar(self)

        self._init_hint_frame()
        self._init_game_frame()
        self._init_dialogue_frame()

    def _init_hint_frame(self):
        self.hint_frame = tk.Frame(self)
        self.hint_frame.pack(fill=tk.BOTH)

        self.hint_lbl = BilingualLabel(
            self.hint_frame,
            text_dict={'eng': 'Hint:', 'rus': 'Подсказка:'},
            background=self['background'],
            foreground=self.FOREGROUND,
            borderwidth=self.BORDERWIDTH,
            padx=10,
            relief=tk.RAISED,
            anchor=tk.NW)
        self.hint_lbl.pack(fill=tk.BOTH)

    def _init_game_frame(self):
        self.game_frame = tk.Frame(self)
        self.game_canvas = GameCanvas(
            self.game_frame,
            width=self['width'] * 9 / 10,
            height=self['height'] * 7 / 9,
            highlightbackground='#000',
            relief=tk.FLAT)

        self.game_canvas.generate_level(1)

        self.game_frame.pack(fill=tk.BOTH)
        self.game_canvas.pack(side=tk.LEFT, fill=tk.BOTH)

        self._init_buttons_frame()

    def _init_buttons_frame(self):
        self.buttons_frame = tk.Frame(self.game_frame)

        self.settings_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_PATH, 'settings.png'),
            text_dict={'eng': 'Settings', 'rus': 'Настройки'})

        self.map_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_PATH, 'map.png'),
            text_dict={'eng': 'Map', 'rus': 'Карта'})

        self.inventory_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_PATH, 'inventory.png'),
            text_dict={'eng': 'Inventory', 'rus': 'Инвентарь'})
        self.inventory_btn.configure(state=tk.DISABLED)

        self.market_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_PATH, 'market.png'),
            text_dict={'eng': 'Market', 'rus': 'Магазин'})
        self.market_btn.configure(state=tk.DISABLED)

        self.bank_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_PATH, 'bank.png'),
            text_dict={'eng': 'Bank', 'rus': 'Банк'})
        self.bank_btn.configure(state=tk.DISABLED)

        self.smith_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_PATH, 'smith.png'),
            text_dict={'eng': 'Smith', 'rus': 'Кузнец'})
        self.smith_btn.configure(state=tk.DISABLED)

        self.buttons_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.settings_btn.pack(fill=tk.BOTH, expand=True)
        self.map_btn.pack(fill=tk.BOTH, expand=True)
        self.inventory_btn.pack(fill=tk.BOTH, expand=True)
        self.market_btn.pack(fill=tk.BOTH, expand=True)
        self.bank_btn.pack(fill=tk.BOTH, expand=True)
        self.smith_btn.pack(fill=tk.BOTH, expand=True)

    def _init_dialogue_frame(self):
        self.dialogue_frame = tk.Frame(self)

        self.dialogue_canvas = DialogueCanvas(
            self.dialogue_frame,
            width=180,
            background=self['background'],
            borderwidth=self.BORDERWIDTH,
            highlightbackground='#000',
            relief=tk.RAISED)

        self.dialogue_frame.pack(fill=tk.BOTH)
        self.dialogue_canvas.pack(side=tk.LEFT, fill=tk.BOTH)

        self._init_choice_frame()

    def _init_choice_frame(self):
        self.choice_frame = tk.Frame(
            self.dialogue_frame,
            width=(self['width'] - int(self.dialogue_canvas['width'])),
            background=self['background'],
            borderwidth=5,
            relief=tk.RAISED)

        self.dialogue_lbl = BilingualLabel(
            self.choice_frame,
            text_dict={'eng': 'Question', 'rus': 'Вопрос'},
            background=self['background'],
            foreground=self.FOREGROUND,
            borderwidth=self.BORDERWIDTH,
            padx=10,
            relief=tk.RAISED,
            anchor=tk.NW)

        choice_btn1 = ChoiceButton(
            self.choice_frame,
            text='Yes',
            value=1,
            variable=self.choice_var)

        choice_btn2 = ChoiceButton(
            self.choice_frame,
            text='No',
            value=2,
            variable=self.choice_var)

        self.choice_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.dialogue_lbl.pack(fill=tk.BOTH)

        choice_btn1.pack(side=tk.LEFT, expand=True)
        choice_btn2.pack(side=tk.LEFT, expand=True)
