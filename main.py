#!/home/defytheflow/.envs/medieval/bin/python3

import os
import tkinter as tk

from PIL import Image, ImageTk

from widgets import ToolTip


def create_photo_image(path: str, size: tuple=None) -> tk.PhotoImage:
    """ Creates a new PhotoImage object. """
    image = Image.open(path)
    if size:
        image = image.resize(size)
    return ImageTk.PhotoImage(image)

# -----------------------------------------------------------------------------
# CONSTANTS.
# -----------------------------------------------------------------------------

WIN_WIDTH = 1200
WIN_HEIGHT = 900

BG_COLOR = '#c9b662'             # beige.
BD_COLOR = '#000'                # black.

BTN_WIDTH = 110
BTN_HEIGHT = 110
BTN_BD = 5
BTN_ACTIVE_BG_COLOR = '#7f6f28'  # dark beige.

LBL_PADX = 10
LBL_FG_COLOR = '#000'
LBL_BD = 5

# -----------------------------------------------------------------------------
# WINDOW.
# -----------------------------------------------------------------------------

window = tk.Tk()
window.title('Medieval')
window.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
window.resizable(0, 0)

# -----------------------------------------------------------------------------
# TOP FRAME.
# -----------------------------------------------------------------------------

top_frame = tk.Frame(window)
top_frame.pack(fill=tk.BOTH)

# -----------------------------------------------------------------------------
# HINT LABEL.
# -----------------------------------------------------------------------------

hint_lbl = tk.Label(
    top_frame,
    text='Hint: Pirates are bad!',
    bg=BG_COLOR,
    fg=LBL_FG_COLOR,
    bd=LBL_BD,
    padx=LBL_PADX,
    relief=tk.RAISED,
    anchor=tk.NW,
)
hint_lbl.pack(fill=tk.BOTH)

# -----------------------------------------------------------------------------
# MIDDLE FRAME.
# -----------------------------------------------------------------------------

middle_frame = tk.Frame(window)
middle_frame.pack()

# -----------------------------------------------------------------------------
# MAIN CANVAS.
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# MIDDLE RIGHT FRAME.
# -----------------------------------------------------------------------------

middle_right_frame = tk.Frame(middle_frame)
middle_right_frame.pack(side=tk.LEFT, fill=tk.BOTH)

# -----------------------------------------------------------------------------
# BUTTONS.
# -----------------------------------------------------------------------------

btn_attrs = {
    'bg': BG_COLOR,
    'bd': BTN_BD,
    'highlightbackground': BD_COLOR,
    'activebackground': BTN_ACTIVE_BG_COLOR,
}

settings_btn_image = create_photo_image(
    os.path.join('assets', 'settings-btn.png'),
    (BTN_WIDTH, BTN_HEIGHT),
)

map_btn_image = create_photo_image(
    os.path.join('assets', 'map-btn.png'),
    (BTN_WIDTH, BTN_HEIGHT),
)
inventory_btn_image = create_photo_image(
    os.path.join('assets', 'inventory-btn.png'),
    (BTN_WIDTH, BTN_HEIGHT),
)

settings_btn = tk.Button(middle_right_frame, image=settings_btn_image, **btn_attrs)
settings_btn.pack(fill=tk.BOTH)

settings_tooltip = ToolTip('Settings')
settings_btn.bind('<Enter>', settings_tooltip.show)
settings_btn.bind('<Leave>', settings_tooltip.hide)

map_btn = tk.Button(middle_right_frame, image=map_btn_image, **btn_attrs)
map_btn.pack(fill=tk.BOTH)

map_tooltip = ToolTip('Map')
map_btn.bind('<Enter>', map_tooltip.show)
map_btn.bind('<Leave>', map_tooltip.hide)

inventory_btn = tk.Button(middle_right_frame, image=inventory_btn_image, **btn_attrs)
inventory_btn.pack(fill=tk.BOTH)

inventory_tooltip = ToolTip('Inventory')
inventory_btn.bind('<Enter>', inventory_tooltip.show)
inventory_btn.bind('<Leave>', inventory_tooltip.hide)

btn4 = tk.Button(middle_right_frame, text='4', **btn_attrs)
btn4.pack(fill=tk.BOTH, expand=True)

btn5 = tk.Button(middle_right_frame, text='5', **btn_attrs)
btn5.pack(fill=tk.BOTH, expand=True)

btn6 = tk.Button(middle_right_frame, text='6', **btn_attrs)
btn6.pack(fill=tk.BOTH, expand=True)

# -----------------------------------------------------------------------------
# BOTTOM FRAME.
# -----------------------------------------------------------------------------

bottom_frame = tk.Frame(window)
bottom_frame.pack(fill=tk.BOTH)

# -----------------------------------------------------------------------------
# BOTTOM CANVAS.
# -----------------------------------------------------------------------------

bottom_canvas = tk.Canvas(
    bottom_frame,
    width=180,
    bg=BG_COLOR,
    bd=5,
    relief=tk.RAISED,
    highlightbackground=BD_COLOR,
)
bottom_canvas.pack(side=tk.LEFT, fill=tk.BOTH)

bottom_canvas_image = create_photo_image(
    os.path.join('assets', 'witch.png'),
    (200, 200),
)
bottom_canvas_image_id = bottom_canvas.create_image(
    0, 0, image=bottom_canvas_image, anchor=tk.NW
)

# -----------------------------------------------------------------------------
# BOTTOM RIGHT FRAME.
# -----------------------------------------------------------------------------

bottom_right_frame = tk.Frame(
    bottom_frame,
    width=WIN_WIDTH - bottom_canvas.winfo_reqwidth(),
    bg=BG_COLOR,
    bd=5,
    relief=tk.RAISED,
)
bottom_right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# -----------------------------------------------------------------------------
# DIALOGUE LABEL.
# -----------------------------------------------------------------------------

dialogue_lbl = tk.Label(
    bottom_right_frame,
    text='Do you want to start?',
    bg=BG_COLOR,
    fg=LBL_FG_COLOR,
    bd=LBL_BD,
    padx=LBL_PADX,
    relief=tk.RAISED,
    anchor=tk.NW,
)
dialogue_lbl.pack(fill=tk.BOTH)

# -----------------------------------------------------------------------------
# CHOICE BUTTONS.
# -----------------------------------------------------------------------------

choice_var = tk.IntVar()

choice_btn_image = create_photo_image(
    os.path.join('assets', 'choice-btn.png'),
    (180, 90),
)

choice_btn_attrs = {
    'variable': choice_var,
    'image': choice_btn_image,
    'bg': BG_COLOR,
    'activebackground': BG_COLOR,
    'highlightbackground': BG_COLOR,
    'compound': tk.CENTER,
}

choice_btn1 = tk.Radiobutton(
    bottom_right_frame,
    text='Yes',
    value=1,
    **choice_btn_attrs,
)
choice_btn1.pack(side=tk.LEFT, expand=True)

choice_btn2 = tk.Radiobutton(
    bottom_right_frame,
    text='No',
    value=2,
    **choice_btn_attrs,
)
choice_btn2.pack(side=tk.LEFT, expand=True)

if __name__ == '__main__':
    window.mainloop()

