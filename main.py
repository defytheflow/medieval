#!/usr/bin/python3

import tkinter as tk

import config
from main_frame import MainFrame
from settings_frame import SettingsFrame


window = tk.Tk()
window.title('Medieval')
window.geometry(f'{config.WIDTH}x{config.HEIGHT}')
window.resizable(0, 0)

settings_frame = SettingsFrame(
    window,
    background=config.BG_COLOR
)

main_frame = MainFrame(
    window,
    width=config.WIDTH,
    height=config.HEIGHT,
    background=config.BG_COLOR,
)

main_frame.settings_btn.bind('<Button-1>', settings_frame.show)
main_frame.pack(fill=tk.BOTH)


if __name__ == '__main__':
    window.mainloop()
