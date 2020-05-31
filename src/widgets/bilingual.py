import tkinter as tk

from typing import Dict

from .behavior import BilingualWidget
from .tooltip import Tooltip
from .utils import get_all_widget_children


def notify_bilingual_widgets(root: tk.Tk, lang: str) -> None:
    for widget in get_all_widget_children(root):
        if isinstance(widget, BilingualWidget):
            widget.switch_lang(lang)


class BilingualLabel(tk.Label, BilingualWidget):

    def __init__(self, *args, text_dict, **kwargs):
        super().__init__(*args, **kwargs)
        self._text_dict: Dict[str, str] = text_dict
        self.configure(text=self._text_dict['eng'])

    def switch_lang(self, lang):
        if lang == 'English':
            self.configure(text=self._text_dict['eng'])
        elif lang == 'Русский':
            self.configure(text=self._text_dict['rus'])


class BilingualButton(tk.Button, BilingualWidget):

    def __init__(self, *args, text_dict, **kwargs):
        super().__init__(*args, **kwargs)
        self._text_dict: Dict[str, str] = text_dict

    def switch_lang(self, lang):
        if lang == 'English':
            self.configure(text=self._text_dict['eng'])
            if self.tooltip and isinstance(self.tooltip, BilingualWidget):
                self.tooltip.switch_lang(lang)
        elif lang == 'Русский':
            self.configure(text=self._text_dict['rus'])
            if self.tooltip and isinstance(self.tooltip, BilingualWidget):
                self.tooltip.switch_lang(lang)


class BilingualTooltip(Tooltip, BilingualWidget):

    def __init__(self, *args, text_dict, **kwargs):
        super().__init__(*args, text=text_dict['eng'], **kwargs)
        self._text_dict: Dict[str, str] = text_dict

    def switch_lang(self, lang):
        if lang == 'English':
            self.text = self._text_dict['eng']
        elif lang == 'Русский':
            self.text = self._text_dict['rus']


class BilingualRadiobutton(tk.Radiobutton, BilingualWidget):

    def __init__(self, *args, text_dict, **kwargs):
        super().__init__(*args, text=text_dict['eng'], **kwargs)
        self._text_dict: Dict[str, str] = text_dict

    def switch_lang(self, lang):
        if lang == 'English':
            self.configure(text=self._text_dict['eng'])
        elif lang == 'Русский':
            self.configure(text=self._text_dict['rus'])
