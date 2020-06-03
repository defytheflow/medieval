import tkinter as tk
from tkinter import ttk

from .behavior import BilingualWidget
from .tooltip import Tooltip
from .utils import get_all_widget_children


class BilingualLabel(ttk.Label, BilingualWidget):

    def __init__(self, master, text_dict, **kwargs):
        super().__init__(master, text=text_dict['eng'], **kwargs)
        self.text_dict = text_dict

    def switch_lang(self, lang):
        ' Overrides BilingualWidget. '
        if lang == 'English':
            self.configure(text=self.text_dict['eng'])
        elif lang == 'Русский':
            self.configure(text=self.text_dict['rus'])


class BilingualButton(ttk.Button, BilingualWidget):

    def __init__(self, master, text_dict, **kwargs):
        super().__init__(master, **kwargs)
        self.text_dict = text_dict

    def switch_lang(self, lang):
        ' Overrides BilingualWidget. '
        if lang == 'English':
            self.configure(text=self.text_dict['eng'])
            if self.tooltip and isinstance(self.tooltip, BilingualWidget):
                self.tooltip.switch_lang(lang)
        elif lang == 'Русский':
            self.configure(text=self.text_dict['rus'])
            if self.tooltip and isinstance(self.tooltip, BilingualWidget):
                self.tooltip.switch_lang(lang)


class BilingualTooltip(Tooltip, BilingualWidget):

    def __init__(self, master, text_dict, **kwargs):
        super().__init__(master, text=text_dict['eng'], **kwargs)
        self.text_dict = text_dict

    def switch_lang(self, lang):
        ' Overrides BilingualWidget. '
        if lang == 'English':
            self.text = self.text_dict['eng']
        elif lang == 'Русский':
            self.text = self.text_dict['rus']


class BilingualRadiobutton(tk.Radiobutton, BilingualWidget):

    def __init__(self, master, text_dict, **kwargs):
        super().__init__(master, text=text_dict['eng'], **kwargs)
        self.text_dict = text_dict

    def switch_lang(self, lang):
        ' Overrides BilingualWidget. '
        if lang == 'English':
            self.configure(text=self.text_dict['eng'])
        elif lang == 'Русский':
            self.configure(text=self.text_dict['rus'])
