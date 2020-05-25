import os
import tkinter as tk

from widgets import ImageButton, BilingualLabel, Combobox
from widgets_behavior import Bilingual
from utils import get_all_widget_children


class SettingsFrame(tk.Frame):

    FONT_NAME = 'Dejavu Serif'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Variables.
        self.lang_var = tk.StringVar(self)
        self.lang_var.set('English')

        self._init_top_frame()
        self._init_lang_frame()

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
            font=(self.FONT_NAME, '32', 'bold italic')
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
        lang_frame = tk.Frame(self, background=self['background'])
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
            padx=20,
        )
        lang_lbl.pack(side=tk.LEFT)

        lang_combobox = Combobox(
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

        lang_combobox.pack(side=tk.LEFT)
        lang_combobox.bind('<<ComboboxSelected>>', self.switch_lang)
