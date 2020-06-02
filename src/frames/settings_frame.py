import tkinter as tk
from tkinter import ttk

import config

from widgets import (
    TitleFrame,
)

from widgets.behavior import (
    KeyboardBoundWidget,
    MouseBoundWidget,
)

from widgets.bilingual import BilingualLabel
from widgets.notifiers import notify_bilingual_widgets
from widgets.utils import get_widget_parent


class SettingsFrame(tk.Frame, KeyboardBoundWidget, MouseBoundWidget):

    LBL_WIDTH = 10
    WIDGET_WIDTH = 350

    def __init__(self, master: tk.Tk, **kwargs):
        super().__init__(master, **kwargs)

        self.title_frame = TitleFrame(self,
                                      bg=self['bg'],
                                      font=config.H_FONT,
                                      text_dict={'eng': 'Settings', 'rus': 'Настройки'})
        self.title_frame.pack(fill='both')

        self.lang_var = tk.StringVar(self)
        self.lang_var.set('English')

        self._init_lang_frame()
        self._init_scale_frame()

    # Overrides KeyboardBoundWidget.
    def init_keyboard_binds(self) -> None:
        self.bind(config.KEY_BINDS['settings-switch-lang'], lambda e: self._toggle_lang())

    # Overrides MouseBoundWidget.
    def init_mouse_binds(self) -> None:
        self.title_frame.return_btn.bind('<1>', lambda e: get_widget_parent(self).show_frame('game'))
        self.lang_combobox.bind('<<ComboboxSelected>>',
            lambda e: notify_bilingual_widgets(get_widget_parent(self), self.lang_var.get()))

    def _toggle_lang(self) -> None:
        if self.lang_var.get() == 'English':
            self.lang_var.set('Русский')
        else:
            self.lang_var.set('English')
        notify_bilingual_widgets(self.master, self.lang_var.get())

    def _init_lang_frame(self):
        lang_frame = tk.Frame(self,
                              bg=self['bg'],
                              pady=100)

        lang_lbl = BilingualLabel(lang_frame,
                                  bg=self['bg'],
                                  text_dict={'eng': 'Language', 'rus': 'Язык'},
                                  width=self.LBL_WIDTH,
                                  font=config.P_FONT + ('bold',),
                                  anchor='nw')

        ttk.Style().map('SF.TCombobox',
                        background=[('readonly', self['bg'])],
                        fieldbackground=[('readonly', self['bg'])],
                        selectbackground=[('readonly', self['bg'])],
                        selectforeground=[('readonly', config.FG)],
                        borderwidth=[('readonly', 5)],
                        selectborderwidth=[('readonly', 0)],
                        arrowsize=[('readonly', 24)],
                        arrowcolor=[('readonly', config.FG)],
                        foreground=[('readonly', config.FG)])

        self.option_add('*TCombobox*Listbox.background', self['bg'])
        self.option_add('*TCombobox*Listbox.foreground', config.FG)
        self.option_add('*TCombobox*Listbox.selectBackground', config.ACTIVE_BG)
        self.option_add('*TCombobox*Listbox.font', config.P_FONT)

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
        scale_frame = tk.Frame(self, bg=self['bg'])

        scale_lbl = BilingualLabel(scale_frame, bg=self['bg'],
                                   text_dict={'eng': 'Scroller', 'rus': 'Ползунок'},
                                   width=self.LBL_WIDTH,
                                   font=config.P_FONT + ('bold',),
                                   anchor='nw')

        scale = tk.Scale(scale_frame,
                         orient='horizontal',
                         length=self.WIDGET_WIDTH + 15,
                         background=self['bg'],
                         borderwidth=5,
                         font=config.P_FONT,
                         troughcolor=self['bg'],
                         highlightbackground=self['bg'],
                         activebackground=config.ACTIVE_BG,
                         relief='sunken')

        scale_frame.pack()
        scale_lbl.pack(side='left')
        scale.pack(side='left')
