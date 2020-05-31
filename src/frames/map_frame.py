import tkinter as tk

from widgets import TitleFrame
from canvases import MapCanvas


class MapFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title_frame = TitleFrame(
            self,
            text_dict={'eng': 'Map', 'rus': 'Карта'},
            background=self['background'],
            font=('DejaVu Serif', 32, 'bold italic'))

        self.canvas = MapCanvas(
            self,
            width=self.winfo_reqwidth(),
            height=self.winfo_reqheight() - self.title_frame.return_btn.winfo_reqheight(),
            background=self['background'],
            highlightbackground=self['background'])

        self.title_frame.pack(fill='both')
        self.canvas.pack(fill='both', expand=True)

    @property
    def return_btn(self):
        return self.title_frame.return_btn
