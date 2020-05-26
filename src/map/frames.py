import tkinter as tk

from widgets import TitleFrame

from .canvases import MapCanvas


class MapFrame(TitleFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, text_dict={'eng': 'Map', 'rus': 'Карта'},
                         **kwargs)

        self.canvas = MapCanvas(
            self,
            width=self['width'],
            height=self['height'] - self.return_btn.winfo_reqheight(),
            background=self['background'],
            highlightbackground=self['background'])

        self.canvas.pack(fill=tk.BOTH, expand=True)
