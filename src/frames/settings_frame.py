import tkinter as tk
from tkinter import ttk

import config

from widgets import TitleFrame
from widgets.bilingual import BilingualLabel

from widgets.behavior import (
    BilingualWidget,
    KeyboardBoundWidget,
    MouseBoundWidget,
    StyledWidget,
)

from widgets.utils import (
    get_widget_parent,
    notify_widget_class,
)


class SettingsFrame(ttk.Frame,
                    KeyboardBoundWidget,
                    MouseBoundWidget,
                    StyledWidget):

    WIDGET_WIDTH = 350

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.title_frame = TitleFrame(self,
                                      bg=config.BG,
                                      font=config.H_FONT,
                                      text_dict={'eng': 'Settings',
                                                 'rus': 'Настройки'})
        self.title_frame.pack(fill='both')

        self.lang_var = tk.StringVar(self)
        self.lang_var.set('English')

        self._init_lang_frame()
        self._init_scale_frame()

    def init_keyboard_binds(self):
        ' Overrides KeyboardBoundWidget. '
        self.bind(config.KEY_BINDS['settings-switch-lang'],
                  lambda e: self._toggle_lang())

    def init_mouse_binds(self):
        ' Overrides MouseBoundWidget. '
        self.title_frame.return_btn.bind('<1>',
            lambda e: get_widget_parent(self).show_frame('game'))
        self.lang_combobox.bind('<<ComboboxSelected>>',
            lambda e: notify_widget_class(get_widget_parent(self), BilingualWidget, 'switch_lang', self.lang_var.get()))

    def init_style(self):
        ' Overrides StyledWidget. '
        self.style = ttk.Style()

        self.style.configure('SF.TFrame', background=config.BG)

        self.style.configure('SF.TLabel',
                             background=config.BG,
                             font=config.P_FONT + ('bold',),
                             width=10,
                             anchor='nw')

        self.style.configure('SF.TCombobox')

        self.style.map('SF.TCombobox',
                        background=[('readonly', config.BG)],
                        fieldbackground=[('readonly', config.BG)],
                        selectbackground=[('readonly', config.BG)],
                        selectforeground=[('readonly', config.FG)],
                        borderwidth=[('readonly', 5)],
                        selectborderwidth=[('readonly', 0)],
                        arrowsize=[('readonly', 24)],
                        arrowcolor=[('readonly', config.FG)],
                        foreground=[('readonly', config.FG)])

        self.option_add('*TCombobox*Listbox.background', config.BG)
        self.option_add('*TCombobox*Listbox.foreground', config.FG)
        self.option_add('*TCombobox*Listbox.selectBackground', config.ACTIVE_BG)
        self.option_add('*TCombobox*Listbox.font', config.P_FONT)

    def _toggle_lang(self):
        if self.lang_var.get() == 'English':
            self.lang_var.set('Русский')
        else:
            self.lang_var.set('English')
        notify_widget_class(get_widget_parent(self),
                            BilingualWidget,
                            'switch_lang',
                            self.lang_var.get())


    def _init_lang_frame(self):
        lang_frame = ttk.Frame(self, style='SF.TFrame', padding=100)

        lang_lbl = BilingualLabel(lang_frame,
                                  style='SF.TLabel',
                                  text_dict={'eng': 'Language',
                                             'rus': 'Язык'})

        self.lang_combobox = ttk.Combobox(lang_frame,
                                          style='SF.TCombobox',
                                          font=config.P_FONT,
                                          values=['Русский', 'English'],
                                          textvariable=self.lang_var,
                                          state='readonly')

        lang_frame.pack()
        lang_lbl.pack(side='left')
        self.lang_combobox.pack(side='left')

    def _init_scale_frame(self):
        scale_frame = ttk.Frame(self, style='SF.TFrame')

        scale_lbl = BilingualLabel(scale_frame,
                                   style='SF.TLabel',
                                   text_dict={'eng': 'Scroller',
                                              'rus': 'Ползунок'})

        scale = tk.Scale(scale_frame,
                         orient='horizontal',
                         length=self.WIDGET_WIDTH + 15,
                         background=config.BG,
                         borderwidth=5,
                         font=config.P_FONT,
                         troughcolor=config.BG,
                         highlightbackground=config.BG,
                         activebackground=config.ACTIVE_BG,
                         relief='sunken')

        scale_frame.pack()
        scale_lbl.pack(side='left')
        scale.pack(side='left')
