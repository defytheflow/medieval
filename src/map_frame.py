import os
import tkinter as tk
from tkinter import ttk

from config import AssetsConfig, ColorsConfig
from utils import create_photo_image
from widgets import MouseBoundWidget, StyledWidget, TitleFrame


class MapFrame(ttk.Frame, MouseBoundWidget, StyledWidget):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = master

        self.title_frame = TitleFrame(self, text='Map')
        self.title_frame.pack(fill='both')

        self.canvas = MapCanvas(self,
                                width=self.winfo_reqwidth(),
                                height=self.winfo_reqheight() - self.title_frame.winfo_reqheight(),
                                background=ColorsConfig.bg,
                                highlightbackground=ColorsConfig.bg)
        self.canvas.pack(fill='both', expand=True)

    def init_mouse_binds(self):
        self.title_frame.return_btn.bind('<1>', lambda e: self.controller.show_frame('game'))

    def init_style(self):
        pass


class MapCanvas(tk.Canvas):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.map_image = create_photo_image(os.path.join(AssetsConfig.assets, 'map.png'),
                                            (self.winfo_reqwidth(), self.winfo_reqheight()))
        self.create_image(0, 0, image=self.map_image, anchor='nw')
