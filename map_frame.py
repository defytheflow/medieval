import os
import tkinter as tk

import utils
from widgets import TitleFrame


class MapFrame(TitleFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         text_dict={'eng': 'Map', 'rus': 'Карта'},
                         **kwargs)

        self.canvas = None
        self.canvas_image = None

        self._init_map_frame_components()

    def _init_map_frame_components(self):
        self.canvas = tk.Canvas(
            self,
            width=self['width'],
            height=self['height'] - self.return_btn.winfo_reqheight(),
            background=self['background'],
            highlightbackground=self['background'],
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas_image = utils.create_photo_image(
            os.path.join('assets', 'map.png'),
            (int(self.canvas['width']), int(self.canvas['height']))
        )
        self.canvas.create_image(0, 0, image=self.canvas_image, anchor=tk.NW)
