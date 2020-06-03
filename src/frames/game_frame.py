import os
import tkinter as tk
from tkinter import ttk
from typing import Dict

import config

from canvases import (
    DialogueCanvas,
    GameCanvas,
)

from utils import (
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

from widgets.utils import (
    get_widget_parent,
    bind_image_to_widget,
    bind_sound_to_widget,
)


class GameFrame(tk.Frame, KeyboardBoundWidget, MouseBoundWidget):

    BD = 5
    LBL_PADX = 10

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.choice_var = tk.IntVar(self)

        ttk.Style().configure('GF.TLabel',
                              padding=(10, 5),
                              background=config.BG,
                              foreground=config.FG,
                              borderwidth=5,
                              relief='raised')

        ttk.Style().configure('GF.TButton',
                              background=config.BG,
                              foreground=config.FG,
                              borderwidth=5,
                              relief='raised')

        ttk.Style().map('GF.TButton',
                        background=[('active', config.ACTIVE_BG)])

        self._init_hint_frame()
        self._init_game_frame()
        self._init_dialogue_frame()

    # Overrides tk.Frame.
    def focus_set(self):
        super().focus_set()
        self.game_canvas.focus_set()

    # Overrides KeyboardBoundWidget.
    def init_keyboard_binds(self):
        self.bind_all(config.KEY_BINDS['show-game'], lambda e: get_widget_parent(self).show_frame('game'))
        self.bind_all(config.KEY_BINDS['show-map'], lambda e: get_widget_parent(self).show_frame('map'))
        self.bind_all(config.KEY_BINDS['show-settings'], lambda e: get_widget_parent(self).show_frame('settings'))

    # Overrides MouseBoundWidget.
    def init_mouse_binds(self):
        self.settings_btn.bind('<1>', lambda e: get_widget_parent(self).show_frame('settings'))
        self.map_btn.bind('<1>', lambda e: get_widget_parent(self).show_frame('map'))

    def _init_hint_frame(self):
        hint_frame = tk.Frame(self)
        self.hint_lbl = BilingualLabel(hint_frame,
                                       style='GF.TLabel',
                                       text_dict={'eng': 'Hint:', 'rus': 'Подсказка:'})
                                       # padx=self.LBL_PADX,

        hint_frame.pack(fill='both')
        self.hint_lbl.pack(fill='both')

    def _create_button(self,
                       master:     tk.Frame,
                       text_dict:  Dict[str, str],
                       image_name: str) -> BilingualButton:

        btn = BilingualButton(master,
                              style='GF.TButton',
                              text_dict=text_dict)

        BilingualTooltip(btn,
                         text_dict=text_dict,
                         bg=master['bg'],
                         waittime=300)

        bind_image_to_widget(btn,
                             os.path.join(config.ICONS_ROOT, image_name),
                             (100, 100))

        bind_sound_to_widget(btn,
                             '<1>',
                             os.path.join(config.SOUNDS_ROOT, 'button-click.wav'))
        return btn


    def _init_game_frame(self):
        game_frame = tk.Frame(self,
                              height=self.winfo_reqheight() * 0.8,
                              background=self['bg'])

        self.game_canvas = GameCanvas(game_frame,
                                      width=config.GAME_CANVAS_WIDTH,
                                      height=config.GAME_CANVAS_HEIGHT,
                                      highlightbackground=config.HIGHLIGHT_BG)

        button_frame = tk.Frame(game_frame)

        self.settings_btn = self._create_button(button_frame,
                                                {'eng': 'Settings', 'rus': 'Настройки'},
                                                'settings.png')

        self.map_btn = self._create_button(button_frame,
                                           {'eng': 'Map', 'rus': 'Карта'},
                                           'map.png')

        self.inventory_btn = self._create_button(button_frame,
                                                 {'eng': 'Inventory', 'rus': 'Инвентарь'},
                                                 'inventory.png')
        # self.inventory_btn.configure(state='disabled')

        self.market_btn = self._create_button(button_frame,
                                              {'eng': 'Market', 'rus': 'Магазин'},
                                              'market.png')
        # self.market_btn.configure(state='disabled')

        self.market_btn = self._create_button(button_frame,
                                              {'eng': 'Bank', 'rus': 'Банк'},
                                              'bank.png')
        # self.bank_btn.configure(state='disabled')

        self.market_btn = self._create_button(button_frame,
                                              {'eng': 'Smith', 'rus': 'Кузнец'},
                                              'smith.png')
        # self.smith_btn.configure(state='disabled')

        game_frame.pack(fill='both')
        self.game_canvas.pack(side='left', fill='both')
        button_frame.pack(side='left', fill='both')

        for btn in button_frame.winfo_children():
            btn.pack(fill='both', expand=True)

    def _init_dialogue_frame(self):
        dialogue_frame = tk.Frame(self)

        self.dialogue_canvas = DialogueCanvas(dialogue_frame,
                                              width=self.winfo_reqwidth() * 0.16,
                                              height=self.winfo_reqheight() * 0.2,
                                              background=self['bg'],
                                              borderwidth=self.BD,
                                              highlightbackground=config.HIGHLIGHT_BG,
                                              relief='raised')

        choice_frame = tk.Frame(dialogue_frame,
                                background=self['bg'],
                                borderwidth=self.BD)

        self.dialogue_lbl = BilingualLabel(choice_frame,
                                           style='GF.TLabel',
                                           text_dict={'eng': 'Question', 'rus': 'Вопрос'})

        common_attrs = {
            'bg':                  self['bg'],
            'activebackground':    self['bg'],
            'highlightbackground': self['bg'],
            'compound':            'center',
            'relief': 'raised',
            'borderwidth': 5,
        }

        btn1 = BilingualRadiobutton(choice_frame,
                                    text_dict={'eng': 'Yes', 'rus': 'Да'},
                                    value=1,
                                    variable=self.choice_var,
                                    **common_attrs)

        btn2 = BilingualRadiobutton(choice_frame,
                                    text_dict={'eng': 'No', 'rus': 'Нет'},
                                    value=2,
                                    variable=self.choice_var,
                                    **common_attrs)

        for btn in (btn1, btn2):
            bind_image_to_widget(btn,
                                 os.path.join(config.ICONS_ROOT, 'choice.png'),
                                 (180, 90))

        dialogue_frame.pack(fill='both')
        self.dialogue_canvas.pack(side='left', fill='both')

        choice_frame.pack(side='left', fill='both', expand=True)
        self.dialogue_lbl.pack(fill='both')

        btn1.pack(side='left', expand=True)
        btn2.pack(side='left', expand=True)
