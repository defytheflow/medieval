#!/usr/bin/python3

import tkinter as tk

import config
import utils

from game.frames import GameFrame
from map.frames import MapFrame
from settings.frames import SettingsFrame


window = tk.Tk()
window.title('Medieval')
window.geometry(f'{config.WIDTH}x{config.HEIGHT}')
window.resizable(0, 0)

settings_frame = SettingsFrame(window, background=config.BG_COLOR)
settings_frame.return_btn.bind(
    '<Button-1>',
    lambda e: utils.set_current_frame(game_frame, settings_frame))
settings_frame.lang_combobox.bind(
    '<<ComboboxSelected>>',
    lambda e: utils.notify_bilingual_children(window, settings_frame.lang_var.get())
)

map_frame = MapFrame(
    window,
    width=config.WIDTH,
    height=config.HEIGHT,
    background=config.BG_COLOR
)
map_frame.return_btn.bind(
    '<Button-1>',
    lambda e: utils.set_current_frame(game_frame, map_frame))

game_frame = GameFrame(
    window,
    width=config.WIDTH,
    height=config.HEIGHT,
    background=config.BG_COLOR,
)
game_frame.settings_btn.bind(
    '<Button-1>',
    lambda e: utils.set_current_frame(settings_frame, game_frame))
game_frame.map_btn.bind(
    '<Button-1>',
    lambda e: utils.set_current_frame(map_frame, game_frame))
game_frame.pack(fill=tk.BOTH)


if __name__ == '__main__':
    window.mainloop()
