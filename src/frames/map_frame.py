import tkinter as tk

import config
from canvases import MapCanvas

from widgets import (
    TitleFrame,
)

from widgets.behavior import (
    KeyboardBoundWidget,
    MouseBoundWidget,
)

from widgets.utils import get_widget_parent


class MapFrame(tk.Frame, MouseBoundWidget):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.title_frame = TitleFrame(self,
                                      background=self['bg'],
                                      font=config.H_FONT,
                                      text_dict={'eng': 'Map', 'rus': 'Карта'})

        self.canvas = MapCanvas(self,
                                width=self.winfo_reqwidth(),
                                height=self.winfo_reqheight() - self.title_frame.winfo_reqheight(),
                                background=self['bg'],
                                highlightbackground=self['bg'])

        self.title_frame.pack(fill='both')
        self.canvas.pack(fill='both', expand=True)

    # Overrides MouseBoundWidget.
    def init_mouse_binds(self) -> None:
        self.title_frame.return_btn.bind('<1>', lambda e: get_widget_parent(self).show_frame('game'))
