#!/home/defytheflow/.envs/medieval/bin/python3

import os
import tkinter as tk

from utils import create_photo_image
from widgets import Button, Label, Radiobutton, ToolTip, SettingsFrame


WIN_WIDTH = 1200
WIN_HEIGHT = 900

BG_COLOR = '#c9b662'


window = tk.Tk()
window.title('Medieval')
window.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
window.resizable(0, 0)


top_frame = tk.Frame(window)
top_frame.pack(fill=tk.BOTH)

hint_lbl = Label(top_frame, text='Hint: Pirates are bad!')
hint_lbl.pack(fill=tk.BOTH)


middle_frame = tk.Frame(window)
middle_frame.pack()


main_canvas = tk.Canvas(
    middle_frame,
    width=WIN_WIDTH * 0.9,
    height=WIN_HEIGHT * 7 / 9,
    highlightbackground='#000',
    relief=tk.FLAT,
)
main_canvas.pack(side=tk.LEFT, fill=tk.BOTH)

main_canvas_image = create_photo_image(
    os.path.join('assets', 'bazaar.jpg'),
    (main_canvas.winfo_reqwidth(), main_canvas.winfo_reqheight()),
)
main_canvas_image_id = main_canvas.create_image(
    0, 0, image=main_canvas_image, anchor=tk.NW
)


middle_right_frame = tk.Frame(middle_frame)
middle_right_frame.pack(side=tk.LEFT, fill=tk.BOTH)


def create_settings_frame(master: tk.Tk):

    for child in master.winfo_children():
        child.forget()

    frame = SettingsFrame(master, background=BG_COLOR)
    frame.pack(fill=tk.BOTH, expand=True)


settings_btn = Button(
    middle_right_frame,
    file=os.path.join('assets', 'settings-icon.png'),
    tooltip='Settings',
)
settings_btn.pack(fill=tk.BOTH)
settings_btn.bind('<Button-1>', lambda e: create_settings_frame(window))

map_btn = Button(
    middle_right_frame,
    file=os.path.join('assets', 'map-icon.png'),
    tooltip='Map'
)
map_btn.pack(fill=tk.BOTH)

inventory_btn = Button(
    middle_right_frame,
    file=os.path.join('assets', 'inventory-icon.png'),
    tooltip='Inventory'
)
inventory_btn.pack(fill=tk.BOTH)

btn4 = Button(middle_right_frame)
btn4.pack(fill=tk.BOTH, expand=True)

btn5 = Button(middle_right_frame)
btn5.pack(fill=tk.BOTH, expand=True)

btn6 = Button(middle_right_frame)
btn6.pack(fill=tk.BOTH, expand=True)


bottom_frame = tk.Frame(window)
bottom_frame.pack(fill=tk.BOTH)


bottom_canvas = tk.Canvas(
    bottom_frame,
    width=180,
    background=BG_COLOR,
    borderwidth=5,
    highlightbackground='#000',
    relief=tk.RAISED,
)
bottom_canvas.pack(side=tk.LEFT, fill=tk.BOTH)

bottom_canvas_image = create_photo_image(
    os.path.join('assets', 'witch.png'),
    (200, 200),
)
bottom_canvas_image_id = bottom_canvas.create_image(
    0, 0, image=bottom_canvas_image, anchor=tk.NW
)


bottom_right_frame = tk.Frame(
    bottom_frame,
    width=WIN_WIDTH - bottom_canvas.winfo_reqwidth(),
    background=BG_COLOR,
    borderwidth=5,
    relief=tk.RAISED,
)
bottom_right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

dialogue_lbl = Label(bottom_right_frame, text='Do you want to start?')
dialogue_lbl.pack(fill=tk.BOTH)


choice_var = tk.IntVar()

choice_btn1 = Radiobutton(bottom_right_frame, text='Yes', value=1, variable=choice_var)
choice_btn1.pack(side=tk.LEFT, expand=True)

choice_btn2 = Radiobutton(bottom_right_frame, text='No', value=2, variable=choice_var)
choice_btn2.pack(side=tk.LEFT, expand=True)

if __name__ == '__main__':
    window.mainloop()

