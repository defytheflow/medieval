import os
import abc
import tkinter as tk
import tkinter.ttk as ttk

import config
import utils

from .bilingual import BilingualLabel


class KeyboardBoundWidget(abc.ABC):

    @abc.abstractmethod
    def init_keyboard_binds(self):
        pass


class TitleFrame(tk.Frame):

    def __init__(self, *args, text_dict, font, **kwargs):
        super().__init__(*args, **kwargs)

        self.return_btn = tk.Button(self,
            width=40,
            height=40,
            background=self['background'],
            borderwidth=5,
            highlightbackground='#000',
            activebackground='#7f6f28',
            relief='raised')

        utils.bind_image(self.return_btn,
            os.path.join(config.ICONS_ROOT, 'return.png'), (40, 40))

        self.title_lbl = BilingualLabel(self,
            text_dict=text_dict,
            background=self['background'],
            font=font)

        self.return_btn.pack(side='left', fill='both')
        self.title_lbl.pack(side='left', fill='both', expand=True)


class Combobox(ttk.Combobox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ttk.Style().map(
            'TCombobox',
            background=[
                ('readonly', self['background'])
            ],
            fieldbackground=[
                ('readonly', self['background'])
            ],
            selectbackground=[
                ('readonly', self['background'])
            ],
            selectforeground=[
                ('readonly', self['foreground'])
            ],
            borderwidth=[
                ('readonly', 5)
            ],
            selectborderwidth=[
                ('readonly', 0)
            ],
            arrowsize=[
                ('readonly', 24)
            ],
        )

        self.master.option_add('*TCombobox*Listbox.background',
                                self['background'])
        self.master.option_add('*TCombobox*Listbox.selectBackground',
                                '#7f6f28')
        self.master.option_add('*TCombobox*Listbox.font', self['font'])
