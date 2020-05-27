import os
import tkinter as tk

import utils
import config

from widgets import TitleFrame, BilingualLabel, Combobox, ToolTipButton, ChoiceButton
from canvases import GameCanvas, DialogueCanvas, MapCanvas


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
            file=os.path.join(config.ICONS_ROOT, 'settings.png'),
            text_dict={'eng': 'Settings', 'rus': 'Настройки'})

        self.map_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_ROOT, 'map.png'),
            text_dict={'eng': 'Map', 'rus': 'Карта'})

        self.inventory_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_ROOT, 'inventory.png'),
            text_dict={'eng': 'Inventory', 'rus': 'Инвентарь'})
        self.inventory_btn.configure(state=tk.DISABLED)

        self.market_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_ROOT, 'market.png'),
            text_dict={'eng': 'Market', 'rus': 'Магазин'})
        self.market_btn.configure(state=tk.DISABLED)

        self.bank_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_ROOT, 'bank.png'),
            text_dict={'eng': 'Bank', 'rus': 'Банк'})
        self.bank_btn.configure(state=tk.DISABLED)

        self.smith_btn = ToolTipButton(
            self.buttons_frame,
            file=os.path.join(config.ICONS_ROOT, 'smith.png'),
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


class SettingsFrame(TitleFrame):

    FONT_NAME = 'Dejavu Serif'
    PADY = 50
    PADX = 25
    BORDERWIDTH = 5
    WIDGET_WIDTH = 350
    LABEL_WIDTH = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         text_dict={'eng': 'Settings', 'rus': 'Настройки'},
                         **kwargs)
        # Public Variables.
        self.lang_var = tk.StringVar(self)
        self.lang_var.set('English')

        # Public bindable Comboboxes.
        self.lang_combobox = None

        self._init_lang_frame()
        self._init_scale_frame()

    def _init_lang_frame(self):
        """
            Handles construction of the lang frame.
        """
        lang_frame = tk.Frame(
            self,
            background=self['background'],
            pady=self.PADY * 2
        )
        lang_frame.pack()

        lang_lbl = BilingualLabel(
            lang_frame,
            text_dict={'eng': 'Language', 'rus': 'Язык'},
            width=self.LABEL_WIDTH,
            foreground='#000',
            background=self['background'],
            font=(self.FONT_NAME, '20', 'bold'),
            anchor=tk.NW,
        )
        lang_lbl.pack(side=tk.LEFT)

        self.lang_combobox = Combobox(
            lang_frame,
            values=['Русский', 'English'],
            textvariable=self.lang_var,
            state='readonly',
            background=self['background'],
            font=(self.FONT_NAME, '20'),
        )

        self.lang_combobox.pack(side=tk.LEFT)

    def _init_scale_frame(self):
        scale_frame = tk.Frame(
            self,
            background=self['background'],
        )
        scale_frame.pack()

        scale_lbl = BilingualLabel(
            scale_frame,
            text_dict={
                'eng': 'Scroller',
                'rus': 'Ползунок'
            },
            foreground='#000',
            background=self['background'],
            font=(self.FONT_NAME, '20', 'bold'),
            width=self.LABEL_WIDTH,
            anchor=tk.NW,
        )
        scale_lbl.pack(side=tk.LEFT)

        scale = tk.Scale(
            scale_frame,
            orient='horizontal',
            length=self.WIDGET_WIDTH + 15,
            background=self['background'],
            borderwidth=self.BORDERWIDTH,
            relief=tk.SUNKEN,
            highlightbackground=self['background'],
            activebackground=config.ACTIVE_BG_COLOR,
            font=(self.FONT_NAME, '20'),
            troughcolor=self['background'],
        )
        scale.pack(side=tk.LEFT)


class MapFrame(TitleFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, text_dict={'eng': 'Map', 'rus': 'Карта'},
                         **kwargs)

        self.canvas = MapCanvas(
            self,
            width=self['width'],
            height=self['height'] - self.return_btn.winfo_reqheight(),
            background=self['background'],
            highlightbackground=self['background'])

        self.canvas.pack(fill=tk.BOTH, expand=True)
