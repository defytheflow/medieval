#!/usr/bin/python3

import tkinter as tk

import config
import utils
from main_frame import MainFrame
from map_frame import MapFrame
from settings_frame import SettingsFrame


window = tk.Tk()
window.title('Medieval')
window.geometry(f'{config.WIDTH}x{config.HEIGHT}')
window.resizable(0, 0)

settings_frame = SettingsFrame(window, background=config.BG_COLOR)
settings_frame.return_btn.bind(
    '<Button-1>',
    lambda e: utils.set_current_frame(main_frame, settings_frame))

map_frame = MapFrame(window, background=config.BG_COLOR)
map_frame.return_btn.bind(
    '<Button-1>',
    lambda e: utils.set_current_frame(main_frame, map_frame))

main_frame = MainFrame(
    window,
    width=config.WIDTH,
    height=config.HEIGHT,
    background=config.BG_COLOR,
)
main_frame.settings_btn.bind(
    '<Button-1>',
    lambda e: utils.set_current_frame(settings_frame, main_frame))
main_frame.map_btn.bind(
    '<Button-1>',
    lambda e: utils.set_current_frame(map_frame, main_frame))
main_frame.pack(fill=tk.BOTH)


if __name__ == '__main__':
    window.mainloop()
