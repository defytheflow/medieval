import os
import tkinter as tk

import config
import utils


class MapCanvas(tk.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.background_image = utils.create_photo_image(
            os.path.join(config.IMAGES_PATH, 'map.png'),
            (int(self['width']), int(self['height'])))

        self.create_image(0, 0, image=self.background_image, anchor=tk.NW)
