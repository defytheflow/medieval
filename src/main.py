#!/home/defytheflow/.envs/medieval/bin/python3

import tkinter as tk

import config as conf

from frames import GameFrame, MapFrame, SettingsFrame
from utils import get_all_widget_children
from widgets import BilingualWidget

# Very bad
from backgrounds import GrassBackground
from level import Level  # Super bad
from sprites import Character


class MedievalApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Medieval')
        self.config(width=conf.WIDTH, height=conf.HEIGHT, bg=conf.BG_COLOR)
        self.geometry(f'{conf.WIDTH}x{conf.HEIGHT}')
        self.resizable(0, 0)

        self._current_frame = None  # type: tk.Frame
        self._frames = {}           # type: Dict[str, tk.Frame]

        self._init_frames()
        self._init_keyboard_binds()
        self._init_mouse_binds()
        self._init_level()

        self._show_frame('game')

    def _init_frames(self):
        common_attrs = {
            'bg':     self['bg'],
            'width':  self['width'],
            'height': self['height'],
        }

        self._frames['game'] = GameFrame(self, **common_attrs)
        self._frames['map'] = MapFrame(self, **common_attrs)
        self._frames['settings'] = SettingsFrame(self, **common_attrs)

    def _init_keyboard_binds(self):
        self.bind_all(conf.KEYBOARD_BINDS['game'],
                      lambda e: self._show_frame('game'))
        self.bind_all(conf.KEYBOARD_BINDS['map'],
                      lambda e: self._show_frame('map'))
        self.bind_all(conf.KEYBOARD_BINDS['settings'],
                      lambda e: self._show_frame('settings'))

    def _init_mouse_binds(self):
        self._frames['game'].settings_btn.bind('<1>',
            lambda e: self._show_frame('settings'))
        self._frames['game'].map_btn.bind('<1>',
            lambda e: self._show_frame('map'))
        self._frames['map'].return_btn.bind('<1>',
            lambda e: self._show_frame('game'))
        self._frames['settings'].return_btn.bind('<1>',
            lambda e: self._show_frame('game'))
        self._frames['settings'].lang_combobox.bind('<<ComboboxSelected>>',
            lambda e: self._notify_bilingual_children(self._frames['settings'].lang))

    def _init_level(self):
        """

        """
        self.bg = GrassBackground()  # FUCK !
        character = Character(tag='peasant',
                              size=(30, 30),
                              direction='south',
                              speed=3)
        level = Level(self._frames['game'].game_canvas, character, self.bg)
        level.play()

    def _show_frame(self, frame_tag: str):
        """

        """
        if self._current_frame:
            self._current_frame.forget()

        self._current_frame = self._frames[frame_tag]
        self._current_frame.pack(fill=tk.BOTH)


    def _notify_bilingual_children(self, lang: str):
        """

        """
        for child in get_all_widget_children(self):
            if isinstance(child, BilingualWidget):
                child.switch_lang(lang)


if __name__ == '__main__':
    app = MedievalApp()
    app.mainloop()
