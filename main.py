#!/usr/bin/python3

import tkinter as tk

from main_frame import MainFrame
from settings_frame import SettingsFrame


window = tk.Tk()
window.title('Medieval')
window.geometry('1200x900')
window.resizable(0, 0)

settings_frame = SettingsFrame(window, background='#c9b662')

main_frame = MainFrame(window, width=1200, height=900)
main_frame.settings_btn.bind('<Button-1>', settings_frame.show)
main_frame.pack(fill=tk.BOTH)


if __name__ == '__main__':
    window.mainloop()
