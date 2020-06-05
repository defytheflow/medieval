from tkinter import ttk

from canvases import MapCanvas

from config import (
    ColorsConfig,
)

from widgets import (
    MouseBoundWidget,
    StyledWidget,
    TitleFrame,
    get_widget_parent,
)


class MapFrame(ttk.Frame, MouseBoundWidget, StyledWidget):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.title_frame = TitleFrame(self, text_dict={'eng': 'Map', 'rus': 'Карта'})

        self.canvas = MapCanvas(self,
                                width=self.winfo_reqwidth(),
                                height=self.winfo_reqheight() - self.title_frame.winfo_reqheight(),
                                background=ColorsConfig.bg,
                                highlightbackground=ColorsConfig.bg)

        self.title_frame.pack(fill='both')
        self.canvas.pack(fill='both', expand=True)

    def init_mouse_binds(self):
        ' Overrides MouseBoundWidget. '
        self.title_frame.return_btn.bind('<1>',
                                         lambda e: get_widget_parent(self).show_frame('game'))

    def init_style(self):
        ' Overrides StyledWidget. '
