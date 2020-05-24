import os
import tkinter as tk
from tkinter import ttk

from widgets import Button, Label
from interfaces import Bilingual
from utils import get_all_children


class SettingsFrame(tk.Frame):

    BG_COLOR = '#c9b662'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.top_frame = tk.Frame(self, background='#0f0')
        self.top_frame.pack(fill=tk.BOTH)

        return_btn = Button(self.top_frame,
                            file=os.path.join('assets', 'return-icon.png'),
                            command=self.hide)
        return_btn.pack(side=tk.LEFT)

        settings_lbl = tk.Label(self.top_frame,
                                text='Settings Menu',
                                background=self.BG_COLOR,
                                font=('DejaVu Serif', '32', 'bold italic'))
        settings_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.top_right_frame = tk.Frame(self.top_frame,
                                        width=return_btn.winfo_reqwidth(),
                                        background=self.BG_COLOR)
        self.top_right_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        lang_frame = tk.Frame(self, background=self.BG_COLOR)
        lang_frame.pack()

        lang_lbl = Label(lang_frame,
                         text_dict={
                            'eng': 'Language',
                            'rus': 'Язык',
                         },
                         font=('DejaVu Serif', '24', 'bold'))
        lang_lbl.pack(side=tk.LEFT)

        style = ttk.Style()
        style.map('TCombobox',
                  background=[('readonly', self.BG_COLOR)],
                  fieldbackground=[('readonly', self.BG_COLOR)],
                  selectbackground=[('readonly', self.BG_COLOR)],
                  selectforeground=[('readonly', '#000')],
                  borderwidth=[('readonly', '5')])

        lang_var = tk.StringVar()
        lang_var.set('English')

        lang_combobox = ttk.Combobox(lang_frame,
                                     values=[
                                         'Русский',
                                         'English',
                                     ],
                                     state='readonly',
                                     font=('Timew New Roman', '20'),
                                     textvariable=lang_var)
        lang_combobox.pack(side=tk.LEFT)
        lang_combobox.bind('<<ComboboxSelected>>',
                           lambda e: self.switch_lang(lang_var))

    def switch_lang(self, var: tk.StringVar):
        for child in get_all_children(self.master):
            if isinstance(child, Bilingual):
                child.switch_lang(var.get())

    def show(self, event):
        for child in self.master.winfo_children():
            child.forget()
        self.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        for child in self.master.winfo_children():
            child.pack(fill=tk.BOTH)
        self.forget()
