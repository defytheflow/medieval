import os
import tkinter as tk

import config
import utils


class DialogueCanvas(tk.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.background_image = utils.create_photo_image(
            os.path.join(config.ASSETS_ROOT, 'witch.png'),
            (self.winfo_reqwidth(), self.winfo_reqheight()))
        self.create_image(0, 0, image=self.background_image, anchor='nw')


class MapCanvas(tk.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.background_image = utils.create_photo_image(
            os.path.join(config.ASSETS_ROOT, 'map.png'),
            (self.winfo_reqwidth(), self.winfo_reqheight()))
        self.create_image(0, 0, image=self.background_image, anchor='nw')
