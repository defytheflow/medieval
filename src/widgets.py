import os
import abc

import tkinter as tk
import tkinter.ttk as ttk

import config
import utils


class BilingualWidget(abc.ABC):

    @abc.abstractmethod
    def __init__(self, text_dict):
        self.text_dict = text_dict

    @abc.abstractmethod
    def switch_lang(self, lang):
        raise NotImplementedError


class ToolTip:

    def __init__(self, text, background, font, borderwidth):
        self._toplevel = None
        self._text = text
        self._background = background
        self._font = font
        self._borderwidth = borderwidth
        self._padx = 10

    def show(self, event):
        x = event.widget.winfo_rootx() - len(self._text) - self._padx
        y = event.widget.winfo_rooty()

        self._toplevel = tk.Toplevel(event.widget)
        self._toplevel.wm_geometry(f'+{x}+{y}')
        self._toplevel.wm_overrideredirect(1)

        label = tk.Label(
            self._toplevel,
            text=self._text,
            background=self._background,
            borderwidth=self._borderwidth,
            padx=self._padx,
            font=self._font,
            relief='raised')

        label.pack(fill='both', expand=True)

    def hide(self, event):
        if self._toplevel:
            self._toplevel.destroy()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        self._text = new_text


class ImageButton(tk.Button):

    def __init__(self, *args, image_file, **kwargs):

        if kwargs.get('width') and kwargs.get('height'):
            width, height = kwargs.get('width'), kwargs.get('height')
        else:
            width, height = 100, 100

        self.image = utils.create_photo_image(image_file, (width, height))

        super().__init__(*args, image=self.image, **kwargs)


class SoundButton(tk.Button):

    def __init__(self, *args, sound_file, **kwargs):
        super().__init__(*args, **kwargs)

        # self.bind('<ButtonRelease>', lambda e: utils.play_sound(sound_file))


class ToolTipButton(ImageButton, SoundButton, BilingualWidget):

    def __init__(self, *args, image_file, sound_file, text_dict, **kwargs):

        super().__init__(*args, image_file=image_file, sound_file=sound_file, **kwargs)
        BilingualWidget.__init__(self, text_dict)

        self.tooltip = ToolTip(
            text_dict['eng'],
            background=self['background'],
            font=('DejaVu Serif', '12', 'italic'),
            borderwidth=3)

        self.bind('<Enter>', self.tooltip.show)
        self.bind('<Leave>', self.tooltip.hide)

    def switch_lang(self, lang: str):
        if lang == 'English':
            self.tooltip.text = self.text_dict['eng']
        elif lang == 'Русский':
            self.tooltip.text = self.text_dict['rus']


class BilingualLabel(tk.Label, BilingualWidget):

    def __init__(self, *args, text_dict, **kwargs):

        BilingualWidget.__init__(self, text_dict)
        super().__init__(*args, **kwargs, text=self.text_dict['eng'])

    def switch_lang(self, lang: str):
        if lang == 'English':
            self.configure(text=self.text_dict['eng'])
        elif lang == 'Русский':
            self.configure(text=self.text_dict['rus'])


class TitleFrame(tk.Frame, BilingualWidget):

    def __init__(self, *args, text_dict, font, **kwargs):

        BilingualWidget.__init__(self, text_dict)
        super().__init__(*args, **kwargs)

        self.return_btn = ImageButton(
            self,
            image_file=os.path.join(config.ICONS_ROOT, 'return.png'),
            width=40,
            height=40,
            background=self['background'],
            borderwidth=5,
            highlightbackground='#000',
            activebackground='#7f6f28',
            relief='raised')

        self.title_lbl = BilingualLabel(
            self,
            text_dict=self.text_dict,
            background=self['background'],
            font=font)

        self.return_btn.pack(side='left', fill='both')
        self.title_lbl.pack(side='left', fill='both', expand=True)

    def switch_lang(self, lang):
        if lang == 'English':
            self.title_lbl.configure(text=self.text_dict['eng'])
        elif lang == 'Русский':
            self.title_lbl.configure(text=self.text_dict['rus'])


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


class ChoiceButton(tk.Radiobutton):

    def __init__(self, *args, **kwargs):
        file = os.path.join(config.ICONS_ROOT, 'choice.png')
        self.image = utils.create_photo_image(file, (180, 90))
        super().__init__(
            *args,
            **kwargs,
            image=self.image,
            background='#c9b662',
            activebackground='#c9b662',
            highlightbackground='#c9b662',
            compound=tk.CENTER)
