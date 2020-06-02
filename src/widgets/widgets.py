import os
import tkinter as tk
from typing import Dict, Tuple

import config

from .bilingual import BilingualLabel
from .utils import bind_image_to_widget


class TitleFrame(tk.Frame):

    def __init__(self,
                 master:    tk.Frame,
                 text_dict: Dict[str, str],
                 font:      Tuple[str, int, str],
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
        self.return_btn.pack(side='left', fill='both')

        bind_image_to_widget(self.return_btn,
                   os.path.join(config.ICONS_ROOT, 'return.png'), (40, 40))

        self.title_lbl = BilingualLabel(self,
                                        text_dict=text_dict,
                                        bg=self['bg'],
                                        font=font)
        self.title_lbl.pack(side='left', fill='both', expand=True)
