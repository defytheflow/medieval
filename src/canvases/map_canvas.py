import os
import tkinter as tk

import config
from utils import create_photo_image


class MapCanvas(tk.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.background_image = create_photo_image(
            os.path.join(config.ASSETS_ROOT, 'map.png'),
            (self.winfo_reqwidth(), self.winfo_reqheight()))
        self.create_image(0, 0, image=self.background_image, anchor='nw')
