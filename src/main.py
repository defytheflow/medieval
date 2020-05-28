#!/home/defytheflow/.envs/medieval/bin/python3

import tkinter as tk

import config
import utils

from frames import MainFrame, SettingsFrame, MapFrame


window = tk.Tk()
window.title('Medieval')
window.geometry(f'{config.WIDTH}x{config.HEIGHT}')
window.resizable(0, 0)

settings_frame = SettingsFrame(window, background=config.BG_COLOR)

settings_frame.title_frame.return_btn.bind(
    '<Button-1>',
    lambda e: utils.set_current_frame(main_frame, settings_frame))

settings_frame.lang_combobox.bind(
    '<<ComboboxSelected>>',
    lambda e: utils.notify_bilingual_children(window, settings_frame.lang_var.get()))

map_frame = MapFrame(
    window,
    width=config.WIDTH,
    height=config.HEIGHT,
    background=config.BG_COLOR)

map_frame.title_frame.return_btn.bind(
    '<Button-1>',
    lambda e: utils.set_current_frame(main_frame, map_frame))

main_frame = MainFrame(
    window,
    width=config.WIDTH,
    height=config.HEIGHT,
    background=config.BG_COLOR)

main_frame.settings_btn.bind(
    '<Button-1>',
    lambda e: utils.set_current_frame(settings_frame, main_frame))
main_frame.map_btn.bind(
    '<Button-1>',
    lambda e: utils.set_current_frame(map_frame, main_frame))

main_frame.pack(fill=tk.BOTH)

main_frame.game_canvas.generate_level(1)


if __name__ == '__main__':
    window.mainloop()
