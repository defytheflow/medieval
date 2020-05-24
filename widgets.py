"""
    Custom widgets.
"""

import os
import tkinter as tk

from widget_behavior import Bilingual
from utils import create_photo_image


class ToolTip:

    def __init__(self, text):
        self.text = text
        self.padx = 10
        self.toplevel = None

    def show(self, event):
        x = event.widget.winfo_rootx() - len(self.text) - self.padx
        y = event.widget.winfo_rooty()

        self.toplevel = tk.Toplevel(event.widget)
        self.toplevel.wm_geometry(f'+{x}+{y}')
        self.toplevel.wm_overrideredirect(1)

        label = tk.Label(self.toplevel,
                         text=self.text,
                         background='#c9b662',
                         borderwidth=3,
                         padx=self.padx,
                         font=('DejaVu Serif', '12', 'italic'),
                         relief=tk.RAISED)
        label.pack(fill=tk.BOTH, expand=True)

    def hide(self, event):
        if self.toplevel:
            self.toplevel.destroy()


class ToolTipButton(tk.Button, Bilingual):

    def __init__(self, master, file, text_dict, **kwargs):
        self.image = create_photo_image(file, (110, 110)) if file else None
        super().__init__(master,
                         image=self.image,
                         background='#c9b662',
                         borderwidth=5,
                         highlightbackground='#000',
                         activebackground='#7f6f28',
                         relief=tk.RAISED,
                         **kwargs)
        self.text_dict = text_dict
        self.tooltip = ToolTip(text_dict['eng'])
        self.bind('<Enter>', self.tooltip.show)
        self.bind('<Leave>', self.tooltip.hide)

    def switch_lang(self, lang):
        if lang == 'English':
            self.tooltip.text = self.text_dict['eng']
        elif lang == 'Русский':
            self.tooltip.text = self.text_dict['rus']


class BilingualLabel(tk.Label, Bilingual):

    def __init__(self, *args, text_dict, **kwargs):
        self.text_dict = text_dict
        super().__init__(*args,
                         **kwargs,
                         text=self.text_dict['eng'])
                         # background='#c9b662',
                         # foreground='#000',
                         # borderwidth=5,
                         # padx=10,
                         # relief=tk.RAISED,
                         # anchor=tk.NW)

    def switch_lang(self, lang):
        if lang == 'English':
            self.configure(text=self.text_dict['eng'])
        elif lang == 'Русский':
            self.configure(text=self.text_dict['rus'])


class Radiobutton(tk.Radiobutton):
    """
        Styled tk.Radiobutton.
    """

    def __init__(self, *args, **kwargs):
        file = os.path.join('assets', 'choice-icon.png')
        self.image = create_photo_image(file, (180, 90))
        super().__init__(*args,
                         **kwargs,
                         image=self.image,
                         background='#c9b662',
                         activebackground='#c9b662',
                         highlightbackground='#c9b662',
                         compound=tk.CENTER)


