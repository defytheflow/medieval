import os
import tkinter as tk

import utils
import config

from widgets import (
    TitleFrame, BilingualLabel, Combobox, ToolTipButton,
    ChoiceButton)
from canvases import GameCanvas, DialogueCanvas, MapCanvas


class MainFrame(tk.Frame):

    BORDERWIDTH = 5
    BORDERCOLOR = '#000'

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

        self.hint_lbl = BilingualLabel(
            self.hint_frame,
            text_dict={'eng': 'Hint:', 'rus': 'Подсказка:'},
            background=self['background'],
            borderwidth=self.BORDERWIDTH,
            padx=10,
            relief='raised',
            anchor='nw')

        self.hint_frame.pack(fill='both')
        self.hint_lbl.pack(fill='both')

    def _init_game_frame(self):
        self.game_frame = tk.Frame(self)

        self.game_canvas = GameCanvas(
            self.game_frame,
            width=self.winfo_reqwidth() * 0.9,
            height=self.winfo_reqheight() * 0.78,
            highlightbackground=self.BORDERCOLOR)

        self.game_frame.pack(fill='both')
        self.game_canvas.pack(side='left', fill='both')

        self._init_buttons_frame()

    def _init_buttons_frame(self):
        self.buttons_frame = tk.Frame(self.game_frame)

        self.settings_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_ROOT, 'settings.png'),
            text_dict={'eng': 'Settings', 'rus': 'Настройки'},
            background=self['background'],
            borderwidth=5,
            highlightbackground=self.BORDERCOLOR,
            activebackground='#7f6f28',
            relief='raised')

        self.map_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_ROOT, 'map.png'),
            text_dict={'eng': 'Map', 'rus': 'Карта'},
            background=self['background'],
            borderwidth=5,
            highlightbackground=self.BORDERCOLOR,
            activebackground='#7f6f28',
            relief='raised')

        self.inventory_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_ROOT, 'inventory.png'),
            text_dict={'eng': 'Inventory', 'rus': 'Инвентарь'},
            background=self['background'],
            borderwidth=5,
            highlightbackground=self.BORDERCOLOR,
            activebackground='#7f6f28',
            relief='raised')

        self.inventory_btn.configure(state='disabled')

        self.market_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_ROOT, 'market.png'),
            text_dict={'eng': 'Market', 'rus': 'Магазин'},
            background=self['background'],
            borderwidth=5,
            highlightbackground=self.BORDERCOLOR,
            activebackground='#7f6f28',
            relief='raised')

        self.market_btn.configure(state='disabled')

        self.bank_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_ROOT, 'bank.png'),
            text_dict={'eng': 'Bank', 'rus': 'Банк'},
            background=self['background'],
            borderwidth=5,
            highlightbackground=self.BORDERCOLOR,
            activebackground='#7f6f28',
            relief='raised')

        self.bank_btn.configure(state='disabled')

        self.smith_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_ROOT, 'smith.png'),
            text_dict={'eng': 'Smith', 'rus': 'Кузнец'},
            background=self['background'],
            borderwidth=5,
            highlightbackground=self.BORDERCOLOR,
            activebackground='#7f6f28',
            relief='raised')


        self.smith_btn.configure(state='disabled')

        self.buttons_frame.pack(side='left', fill='both', expand=True)

        for btn in self.buttons_frame.winfo_children():
            btn.pack(fill='both', expand=True)

    def _init_dialogue_frame(self):
        self.dialogue_frame = tk.Frame(self)

        self.dialogue_canvas = DialogueCanvas(
            self.dialogue_frame,
            width=self.winfo_reqwidth() * 0.15,
            height=self.winfo_reqheight() * 0.2,
            background=self['background'],
            borderwidth=self.BORDERWIDTH,
            highlightbackground=self.BORDERCOLOR,
            relief='raised')

        self.dialogue_frame.pack(fill='both')
        self.dialogue_canvas.pack(side='left', fill='both')

        self._init_choice_frame()

    def _init_choice_frame(self):
        self.choice_frame = tk.Frame(
            self.dialogue_frame,
            background=self['background'],
            borderwidth=self.BORDERWIDTH,
            relief='raised')

        self.dialogue_lbl = BilingualLabel(
            self.choice_frame,
            text_dict={'eng': 'Question', 'rus': 'Вопрос'},
            background=self['background'],
            borderwidth=self.BORDERWIDTH,
            padx=10,
            relief='raised',
            anchor='nw')

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

        self.choice_frame.pack(side='left', fill='both', expand=True)
        self.dialogue_lbl.pack(fill='both')

        choice_btn1.pack(side='left', expand=True)
        choice_btn2.pack(side='left', expand=True)


class SettingsFrame(tk.Frame):

    FONT = ('Dejavu Serif', 20)
    LBL_WIDTH = 10
    WIDGET_WIDTH = 350

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title_frame = TitleFrame(
            self,
            text_dict={'eng': 'Settings', 'rus': 'Настройки'},
            background=self['background'],
            font=('DejaVu Serif', 32, 'bold italic'))

        self.title_frame.pack(fill='both')

        self.lang_frame = None
        self.scale_frame = None
        self.lang_combobox = None
        self.lang_lbl = None
        self.lang_var = tk.StringVar(self)
        self.lang_var.set('English')

        self._init_lang_frame()
        self._init_scale_frame()

    def _init_lang_frame(self):
        self.lang_frame = tk.Frame(
            self,
            background=self['background'],
            pady=100)

        self.lang_lbl = BilingualLabel(
            self.lang_frame,
            text_dict={'eng': 'Language', 'rus': 'Язык'},
            width=self.LBL_WIDTH,
            background=self['background'],
            font=self.FONT + ('bold',),
            anchor='nw')

        self.lang_combobox = Combobox(
            self.lang_frame,
            values=['Русский', 'English'],
            textvariable=self.lang_var,
            state='readonly',
            background=self['background'],
            font=self.FONT)

        self.lang_frame.pack()
        self.lang_lbl.pack(side='left')
        self.lang_combobox.pack(side='left')

    def _init_scale_frame(self):
        self.scale_frame = tk.Frame(self, background=self['background'])

        scale_lbl = BilingualLabel(
            self.scale_frame,
            text_dict={'eng': 'Scroller', 'rus': 'Ползунок'},
            width=self.LBL_WIDTH,
            background=self['background'],
            font=self.FONT + ('bold',),
            anchor='nw')

        scale = tk.Scale(
            self.scale_frame,
            orient='horizontal',
            length=self.WIDGET_WIDTH + 15,
            background=self['background'],
            borderwidth=5,
            relief=tk.SUNKEN,
            highlightbackground=self['background'],
            activebackground=config.ACTIVE_BG_COLOR,
            font=self.FONT,
            troughcolor=self['background'])

        self.scale_frame.pack()
        scale_lbl.pack(side='left')
        scale.pack(side='left')


class MapFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title_frame = TitleFrame(
            self,
            text_dict={'eng': 'Map', 'rus': 'Карта'},
            background=self['background'],
            font=('DejaVu Serif', 32, 'bold italic'))

        self.canvas = MapCanvas(
            self,
            width=self.winfo_reqwidth(),
            height=self.winfo_reqheight() - self.title_frame.return_btn.winfo_reqheight(),
            background=self['background'],
            highlightbackground=self['background'])

        self.title_frame.pack(fill='both')
        self.canvas.pack(fill='both', expand=True)
