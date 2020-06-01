#!/home/defytheflow/.envs/medieval/bin/python3

import tkinter as tk

import config

from frames import (
    GameFrame,
    MapFrame,
    SettingsFrame,
)

from widgets.notifiers import (
    notify_keyboardbound_widgets,
    notify_mousebound_widgets,
)

from backgrounds import VillageBackground
from sprites import Character


class MedievalApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Medieval')
        self.config(width=config.WIDTH, height=config.HEIGHT, bg=config.BG)
        self.geometry(f'{config.WIDTH}x{config.HEIGHT}')
        self.resizable(0, 0)

        self._current_frame = None  # type: tk.Frame
        self._frames = {}           # type: Dict[str, tk.Frame]

        self._init_frames()
        self._init_level()

        notify_keyboardbound_widgets(self)
        notify_mousebound_widgets(self)

        self.show_frame('game')

    def show_frame(self, frame_tag: str):
        if self._current_frame:
            self._current_frame.forget()

        self._current_frame = self._frames[frame_tag]
        self._current_frame.pack(fill=tk.BOTH)
        self._current_frame.focus_set()

    def _init_frames(self):
        common_attrs = {
            'bg':     self['bg'],
            'width':  self['width'],
            'height': self['height'],
        }
        self._frames['game'] = GameFrame(self, **common_attrs)
        self._frames['map'] = MapFrame(self, **common_attrs)
        self._frames['settings'] = SettingsFrame(self, **common_attrs)

    def _init_level(self):
        game_canvas = self._frames['game'].game_canvas

        background = VillageBackground(
            name='village',
            canvas=game_canvas,
            block_size=config.BLOCK_SIZE)

        character = Character(
            name='peasant',
            canvas=game_canvas,
            size=(config.BLOCK_SIZE, config.BLOCK_SIZE),
            speed=3)

        background.draw_on_canvas()
        character.draw_on_canvas(0, 0)


if __name__ == '__main__':
    app = MedievalApp()
    app.mainloop()
