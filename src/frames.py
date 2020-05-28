import os
import tkinter as tk

import utils
import config

from widgets import (
    BilingualLabel, BilingualButton, BilingualTooltip, BilingualRadiobutton,
    TitleFrame, Combobox)

from canvases import DialogueCanvas, MapCanvas
from game_canvas import GameCanvas


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

        self.hint_lbl = BilingualLabel(self.hint_frame,
            text_dict={'eng': 'Hint:', 'rus': 'Подсказка:'},
            background=self['background'],
            borderwidth=self.BORDERWIDTH,
            padx=10,
            relief='raised',
            anchor='nw')

        self.hint_frame.pack(fill='both')
        self.hint_lbl.pack(fill='both')

    def _init_game_frame(self):
        self.game_frame = tk.Frame(self, height=self.winfo_reqheight() * 0.8)

        self.game_canvas = GameCanvas(
            self.game_frame,
            width=self.winfo_reqwidth() * 0.9,
            height=self.game_frame.winfo_reqheight(),
            highlightbackground=self.BORDERCOLOR)

        self.game_frame.pack(fill='both')
        self.game_canvas.pack(side='left', fill='both')

        self._init_buttons_frame()

    def _init_buttons_frame(self):
        self.buttons_frame = tk.Frame(self.game_frame)

        common_attrs = {
            'background': self['background'],
            'borderwidth': 5,
            'highlightbackground': self.BORDERCOLOR,
            'activebackground': '#7f6f28',
            'relief': 'raised',
        }

        self.settings_btn = BilingualButton(self.buttons_frame,
            text_dict={'eng': 'Settings', 'rus': 'Настройки'}, **common_attrs)

        BilingualTooltip(self.settings_btn,
            text_dict={'eng': 'Settings', 'rus': 'Настройки'},
            bg=self['background'],
            waittime=300)

        utils.bind_image(self.settings_btn,
            os.path.join(config.ICONS_ROOT, 'settings.png'), (100, 100))

        self.map_btn = BilingualButton(self.buttons_frame,
            text_dict={'eng': 'Map', 'rus': 'Карта'}, **common_attrs)

        BilingualTooltip(self.map_btn,
            text_dict={'eng': 'Map', 'rus': 'Карта'},
            bg=self['background'],
            waittime=300)

        utils.bind_image(self.map_btn,
            os.path.join(config.ICONS_ROOT, 'map.png'), (100, 100))

        self.inventory_btn = BilingualButton(self.buttons_frame,
            text_dict={'eng': 'Inventory', 'rus': 'Инвентарь'}, **common_attrs)
        self.inventory_btn.configure(state='disabled')

        BilingualTooltip(self.inventory_btn,
            text_dict={'eng': 'Inventory', 'rus': 'Инвентарь'},
            bg=self['background'],
            waittime=300)

        utils.bind_image(self.inventory_btn,
            os.path.join(config.ICONS_ROOT, 'inventory.png'), (100, 100))

        self.market_btn = BilingualButton(self.buttons_frame,
            text_dict={'eng': 'Market', 'rus': 'Магазин'}, **common_attrs)
        self.market_btn.configure(state='disabled')

        BilingualTooltip(self.market_btn,
            text_dict={'eng': 'Market', 'rus': 'Магазин'},
            bg=self['background'],
            waittime=300)

        utils.bind_image(self.market_btn,
            os.path.join(config.ICONS_ROOT, 'market.png'), (100, 100))

        self.bank_btn = BilingualButton(self.buttons_frame,
            text_dict={'eng': 'Bank', 'rus': 'Банк'}, **common_attrs)
        self.bank_btn.configure(state='disabled')

        BilingualTooltip(self.bank_btn,
            text_dict={'eng': 'Bank', 'rus': 'Банк'},
            bg=self['background'],
            waittime=300)

        utils.bind_image(self.bank_btn,
            os.path.join(config.ICONS_ROOT, 'bank.png'), (100, 100))

        self.smith_btn = BilingualButton(self.buttons_frame,
            text_dict={'eng': 'Smith', 'rus': 'Кузнец'}, **common_attrs)
        self.smith_btn.configure(state='disabled')

        BilingualTooltip(self.smith_btn,
            text_dict={'eng': 'Smith', 'rus': 'Кузнец'},
            bg=self['background'],
            waittime=300)

        utils.bind_image(self.smith_btn,
            os.path.join(config.ICONS_ROOT, 'smith.png'), (100, 100))

        self.buttons_frame.pack(side='left', fill='both', expand=True)

        for btn in self.buttons_frame.winfo_children():
            btn.pack(fill='both', expand=True)
            utils.bind_sound(btn, os.path.join(config.SOUNDS_ROOT, 'click.wav'))

    def _init_dialogue_frame(self):
        self.dialogue_frame = tk.Frame(self)

        self.dialogue_canvas = DialogueCanvas(
            self.dialogue_frame,
            width=self.winfo_reqwidth() * 0.13,
            # width=self.winfo_reqwidth() * 0.15,
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

        file = os.path.join(config.ICONS_ROOT, 'choice.png')
        image = utils.create_photo_image(file, (180, 90))

        common_attrs = {
            'background': self['background'],
            'activebackground': self['background'],
            'highlightbackground': self['background'],
            'compound': 'center',
        }

        btn1 = BilingualRadiobutton(self.choice_frame,
            text_dict={'eng': 'yes', 'rus': 'да'},
            value=1,
            variable=self.choice_var,
            **common_attrs)

        utils.bind_image(btn1,
            os.path.join(config.ICONS_ROOT, 'choice.png'), (180, 90))

        btn2 = BilingualRadiobutton(self.choice_frame,
            text_dict={'eng': 'no', 'rus': 'нет'},
            value=2,
            variable=self.choice_var,
            **common_attrs)

        utils.bind_image(btn2,
            os.path.join(config.ICONS_ROOT, 'choice.png'), (180, 90))

        self.choice_frame.pack(side='left', fill='both', expand=True)
        self.dialogue_lbl.pack(fill='both')

        btn1.pack(side='left', expand=True)
        btn2.pack(side='left', expand=True)


class SettingsFrame(tk.Frame):

    FONT = ('Dejavu Serif', 20)
    LBL_WIDTH = 10
    WIDGET_WIDTH = 350

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title_frame = TitleFrame(self,
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
