import os
import tkinter as tk

import config
from widgets import ImageButton, BilingualLabel, Combobox
from widgets_behavior import Bilingual
from utils import get_all_widget_children


class SettingsFrame(tk.Frame):

    FONT_NAME = 'Dejavu Serif'
    PADY = 50
    PADX = 25
    BORDERWIDTH = 5
    WIDGET_WIDTH = 350
    LABEL_WIDTH = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Variables.
        self.lang_var = tk.StringVar(self)
        self.lang_var.set('English')

        # Comboboxes.
        self.lang_combobox = None

        self._init_top_frame()
        self._init_lang_frame()
        self._init_scale_frame()

    def switch_lang(self, event):
        for child in get_all_widget_children(self.master):
            if isinstance(child, Bilingual):
                child.switch_lang(self.lang_var.get())

    def show(self, event):
        for child in self.master.winfo_children():
            child.forget()
        self.pack(fill=tk.BOTH, expand=True)

    def hide(self, event):
        for child in self.master.winfo_children():
            child.pack(fill=tk.BOTH)
        self.forget()

    def _init_top_frame(self):
        """
            Handles construction of the top frame.
        """
        top_frame = tk.Frame(self)
        top_frame.pack(fill=tk.BOTH)

        return_btn = ImageButton(
            top_frame,
            file=os.path.join('assets', 'return-icon.png'),
        )
        return_btn.pack(side=tk.LEFT)
        return_btn.bind('<Button-1>', self.hide)

        settings_lbl = BilingualLabel(
            top_frame,
            text_dict={
                'eng': 'Settings',
                'rus': 'Настройки',
            },
            background=self['background'],
            font=(self.FONT_NAME, '32', 'bold italic'),
            width=100,
        )
        settings_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        top_right_frame = tk.Frame(
            top_frame,
            width=return_btn.winfo_reqwidth(),
            background=self['background']
        )
        top_right_frame.pack(side=tk.LEFT, fill=tk.BOTH)

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
            text_dict={
                'eng': 'Language',
                'rus': 'Язык',
            },
            foreground='#000',
            background=self['background'],
            font=(self.FONT_NAME, '24', 'bold'),
            width=self.LABEL_WIDTH,
            anchor=tk.NW,
        )
        lang_lbl.pack(side=tk.LEFT)

        self.lang_combobox = Combobox(
            lang_frame,
            values=[
                'Русский',
                'English',
            ],
            textvariable=self.lang_var,
            state='readonly',
            background=self['background'],
            font=(self.FONT_NAME, '20'),
        )

        self.lang_combobox.pack(side=tk.LEFT)
        self.lang_combobox.bind('<<ComboboxSelected>>', self.switch_lang)

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
            font=(self.FONT_NAME, '24', 'bold'),
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
