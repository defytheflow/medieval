import tkinter as tk

import config
from widgets import TitleFrame, BilingualLabel

from .widgets import Combobox


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
