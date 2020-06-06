import os
from tkinter import ttk

from config import AssetsConfig, ColorsConfig, FontsConfig

from .interfaces import StyledWidget
from .utils import bind_image_to_widget


class TitleFrame(ttk.Frame, StyledWidget):

    def __init__(self, master, text, **kwargs):
        super().__init__(master, **kwargs)

        self.return_btn = ttk.Button(self, style='T.TButton')
        self.return_btn.pack(side='left', fill='both')

        bind_image_to_widget(self.return_btn,
                             os.path.join(AssetsConfig.icons, 'return.png'),
                             (40, 40))

        self.title_lbl = ttk.Label(self, style='T.TLabel', text=text)
        self.title_lbl.pack(side='left', fill='both', expand=True)

    def init_style(self):
        ' Overrides StyledWidget. '
        self.style = ttk.Style()

        self.style.configure('T.TButton',
                             background=ColorsConfig.bg,
                             borderwidth=5,
                             relief='raised')

        self.style.map('T.TButton',
                        background=[('active', ColorsConfig.active_bg)])

        self.style.configure('T.TLabel',
                             background=ColorsConfig.bg,
                             font=FontsConfig.h,
                             anchor='center')
