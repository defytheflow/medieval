import os
import tkinter as tk

import config
import utils


class ChoiceButton(tk.Radiobutton):

    def __init__(self, *args, **kwargs):
        file = os.path.join(config.ICONS_PATH, 'choice.png')
        self.image = utils.create_photo_image(file, (180, 90))
        super().__init__(
            *args,
            **kwargs,
            image=self.image,
            background='#c9b662',
            activebackground='#c9b662',
            highlightbackground='#c9b662',
            compound=tk.CENTER)
