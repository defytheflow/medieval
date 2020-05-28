import os
import abc
import tkinter as tk
import tkinter.ttk as ttk
from typing import Dict

from tooltip import Tooltip

import config
import utils


class BilingualWidget(abc.ABC):

    @abc.abstractmethod
    def switch_lang(self, lang):
        pass


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


class TitleFrame(tk.Frame):

    def __init__(self, *args, text_dict, font, **kwargs):
        super().__init__(*args, **kwargs)

        self.return_btn = tk.Button(self,
            width=40,
            height=40,
            background=self['background'],
            borderwidth=5,
            highlightbackground='#000',
            activebackground='#7f6f28',
            relief='raised')

        utils.bind_image(self.return_btn,
            os.path.join(config.ICONS_ROOT, 'return.png'), (40, 40))

        self.title_lbl = BilingualLabel(self,
            text_dict=text_dict,
            background=self['background'],
            font=font)

        self.return_btn.pack(side='left', fill='both')
        self.title_lbl.pack(side='left', fill='both', expand=True)


class Combobox(ttk.Combobox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ttk.Style().map(
            'TCombobox',
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

        self.master.option_add('*TCombobox*Listbox.background',
                                self['background'])
        self.master.option_add('*TCombobox*Listbox.selectBackground',
                                '#7f6f28')
        self.master.option_add('*TCombobox*Listbox.font', self['font'])
