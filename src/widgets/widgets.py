import os
import tkinter as tk
import tkinter.ttk as ttk
from typing import Dict, Tuple

import config
from utils import bind_image

from .bilingual import BilingualLabel


class TitleFrame(tk.Frame):

    def __init__(self,
                 master: tk.Frame,
                 text_dict: Dict[str, str],
                 font: Tuple[str, int, str],
                 **kwargs):

        super().__init__(master, **kwargs)

        self.return_btn = tk.Button(self,
            width=40,
            height=40,
            bg=self['bg'],
            bd=5,
            highlightbackground=config.HIGHLIGHT_BG,
            activebackground=config.ACTIVE_BG,
            relief='raised')

        bind_image(self.return_btn, os.path.join(config.ICONS_ROOT, 'return.png'),
                   (self.return_btn['width'], self.return_btn['height']))

        self.title_lbl = BilingualLabel(self, text_dict=text_dict, bg=self['bg'], font=font)

        self.return_btn.pack(side='left', fill='both')
        self.title_lbl.pack(side='left', fill='both', expand=True)


class Combobox(ttk.Combobox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ttk.Style().map('TCombobox',
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
