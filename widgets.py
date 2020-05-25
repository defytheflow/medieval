import os
import tkinter as tk
import tkinter.ttk as ttk
from typing import Dict

from widgets_behavior import Bilingual
from utils import create_photo_image


class ToolTip:

    def __init__(self, text: str):
        self.text = text
        self.padx = 10
        self.toplevel = None

    def show(self, event):
        x = event.widget.winfo_rootx() - len(self.text) - self.padx
        y = event.widget.winfo_rooty()

        self.toplevel = tk.Toplevel(event.widget)
        self.toplevel.wm_geometry(f'+{x}+{y}')
        self.toplevel.wm_overrideredirect(1)

        label = tk.Label(
            self.toplevel,
            text=self.text,
            background='#c9b662',
            borderwidth=3,
            padx=self.padx,
            font=('DejaVu Serif', '12', 'italic'),
            relief=tk.RAISED
        )
        label.pack(fill=tk.BOTH, expand=True)

    def hide(self, event):
        if self.toplevel:
            self.toplevel.destroy()


class ImageButton(tk.Button):

    def __init__(self, master: tk.Widget, file: str, **kwargs):
        self.image = create_photo_image(file, (100, 100))
        super().__init__(
            master,
            image=self.image,
            background='#c9b662',
            borderwidth=5,
            highlightbackground='#000',
            activebackground='#7f6f28',
            relief=tk.RAISED,
            **kwargs
        )


class ToolTipButton(ImageButton, Bilingual):

    def __init__(self, master, file, text_dict: Dict[str, str], **kwargs):
        super().__init__(master, file)
        Bilingual.__init__(self, text_dict)

        self.tooltip = ToolTip(text_dict['eng'])
        self.bind('<Enter>', self.tooltip.show)
        self.bind('<Leave>', self.tooltip.hide)

    def switch_lang(self, lang: str):
        if lang == 'English':
            self.tooltip.text = self.text_dict['eng']
        elif lang == 'Русский':
            self.tooltip.text = self.text_dict['rus']


class BilingualLabel(tk.Label, Bilingual):

    def __init__(self, *args, text_dict: Dict[str, str], **kwargs):
        Bilingual.__init__(self, text_dict)
        super().__init__(*args, **kwargs, text=self.text_dict['eng'])

    def switch_lang(self, lang: str):
        if lang == 'English':
            self.configure(text=self.text_dict['eng'])
        elif lang == 'Русский':
            self.configure(text=self.text_dict['rus'])


class Combobox(ttk.Combobox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ttk.Style().map('TCombobox',
            background=[
                ('readonly', self['background'])
            ],
            fieldbackground=[
                ('readonly', self['background'])
            ],
            selectbackground=[
                ('readonly', self['background'])
            ],
            selectforeground=[
                ('readonly', self['foreground'])
            ],
            borderwidth=[
                ('readonly', 5)
            ],
            selectborderwidth=[
                ('readonly', 0)
            ],
            arrowsize=[
                ('readonly', 24)
            ],
        )

        self.master.option_add('*TCombobox*Listbox.background', self['background'])
        self.master.option_add('*TCombobox*Listbox.selectBackground', '#7f6f28')
        self.master.option_add('*TCombobox*Listbox.font', self['font'])


class Radiobutton(tk.Radiobutton):

    def __init__(self, *args, **kwargs):
        file = os.path.join('assets', 'choice-icon.png')
        self.image = create_photo_image(file, (180, 90))
        super().__init__(
            *args,
            **kwargs,
            image=self.image,
            background='#c9b662',
            activebackground='#c9b662',
            highlightbackground='#c9b662',
            compound=tk.CENTER
        )
