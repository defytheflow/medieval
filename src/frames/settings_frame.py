import tkinter as tk

import config
from widgets import BilingualLabel, TitleFrame, Combobox


class SettingsFrame(tk.Frame):

    ACTIVE_BG = config.ACTIVE_BG
    FONT = ('Dejavu Serif', 20)
    LBL_WIDTH = 10
    WIDGET_WIDTH = 350

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title_frame = TitleFrame(self, bg=self['bg'],
            text_dict={'eng': 'Settings', 'rus': 'Настройки'},
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

    @property
    def return_btn(self):
        return self.title_frame.return_btn

    @property
    def lang(self):
        return self.lang_var.get()

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
            activebackground=self.ACTIVE_BG,
            font=self.FONT,
            troughcolor=self['background'])

        self.scale_frame.pack()
        scale_lbl.pack(side='left')
        scale.pack(side='left')
