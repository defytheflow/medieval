"""
    Custom widgets.
"""

import os
import tkinter as tk

from utils import create_photo_image


class Button(tk.Button):
    """
        Styled tk.Button.
    """

    def __init__(self, parent, file='', tooltip='', **kwargs):
        self.image = create_photo_image(file, (110, 110)) if file else None
        super().__init__(parent,
                         image=self.image,
                         background='#c9b662',
                         borderwidth=5,
                         highlightbackground='#000',
                         activebackground='#7f6f28',
                         relief=tk.RAISED,
                         **kwargs)
        if tooltip:
            self.tooltip = ToolTip(tooltip)
            self.bind('<Enter>', self.tooltip.show)
            self.bind('<Leave>', self.tooltip.hide)


class Label(tk.Label):
    """
        Styled tk.Label.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         **kwargs,
                         background='#c9b662',
                         foreground='#000',
                         borderwidth=5,
                         padx=10,
                         relief=tk.RAISED,
                         anchor=tk.NW)


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


class ToolTip:
    """
        Info box shown over a widget.
    """

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


class SettingsFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        top_frame = tk.Frame(self, background='#c9b662')
        top_frame.pack(side=tk.TOP, fill=tk.BOTH)

        back_btn = Button(top_frame, file=os.path.join('assets', 'back-icon.png'))
        back_btn.pack(side=tk.LEFT)
