import os
from tkinter import ttk

import config

from .behavior import StyledWidget
from .bilingual import BilingualLabel
from .utils import bind_image_to_widget


class TitleFrame(ttk.Frame, StyledWidget):

    def __init__(self, master, text_dict, **kwargs):
        super().__init__(master, **kwargs)

        self.title_lbl = BilingualLabel(self, style='T.TLabel', text_dict=text_dict)
        self.title_lbl.pack(side='left', fill='both', expand=True)

        self.return_btn = ttk.Button(self, style='T.TButton')
        self.return_btn.pack(side='left', fill='both')

        bind_image_to_widget(self.return_btn,
                             os.path.join(config.ICONS_ROOT, 'return.png'),
                             (40, 40))

    def init_style(self):
        ' Overrides StyledWidget. '
        self.style = ttk.Style()

        self.style.configure('T.TButton',
                             background=config.BG,
                             borderwidth=5,
                             relief='raised')

        self.style.map('T.TButton',
                        background=[('active', config.ACTIVE_BG)])

        self.style.configure('T.TLabel',
                             background=config.BG,
                             font=config.H_FONT,
                             anchor='center')
