import os
import tkinter as tk

import utils
from widgets import TitleFrame


class MapFrame(TitleFrame):

    PREVIEW_WIDTH = 300
    PREVIEW_HEIGHT = 150

    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         text_dict={'eng': 'Map', 'rus': 'Карта'},
                         **kwargs)

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
            (int(self.canvas['width']), int(self.canvas['height'])))

        self.bazaar_image = utils.create_photo_image(
            os.path.join('assets', 'bazaar-preview.png'),
            (self.PREVIEW_WIDTH, self.PREVIEW_HEIGHT))

        self.canvas.create_image(0, 0, image=self.canvas_image, anchor=tk.NW)
        self.canvas.create_image(110, 170, image=self.bazaar_image, anchor=tk.NW)
